# Clock Lobster Lambda Deployment Script
# Deploys the form handler to AWS using only AWS CLI (no SAM required)
# Run from the lambda/ directory

$ErrorActionPreference = "Stop"

$Region = "ca-west-1"
$FunctionName = "clocklobster-form-handler"
$SecretName = "ClockLobster/Site/Secrets"
$SecretKey = "ATTIO_WEB_FORM1_KEY"
$AccountId = (aws sts get-caller-identity --query Account --output text --region $Region)

Write-Host "=== Clock Lobster Lambda Deployment ===" -ForegroundColor Cyan
Write-Host "Region: $Region"
Write-Host "Account: $AccountId"
Write-Host ""

# ─── Step 1: Create deployment package ───
Write-Host "Step 1: Creating deployment package..." -ForegroundColor Yellow
Compress-Archive -Path "index.mjs" -DestinationPath "deployment.zip" -Force
Write-Host "  ✓ deployment.zip created" -ForegroundColor Green

# ─── Step 2: Create IAM Role (if not exists) ───
Write-Host ""
Write-Host "Step 2: Checking IAM role..." -ForegroundColor Yellow

$RoleName = "clocklobster-lambda-role"
$RoleArn = $null

try {
    $RoleArn = aws iam get-role --role-name $RoleName --query 'Role.Arn' --output text 2>$null
    Write-Host "  ✓ Role already exists: $RoleArn" -ForegroundColor Green
} catch {
    Write-Host "  Creating new role..." -ForegroundColor Gray

    $TrustPolicy = @'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "lambda.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
'@
    $TrustPolicy | Out-File -FilePath "trust-policy.json" -Encoding utf8

    aws iam create-role `
        --role-name $RoleName `
        --assume-role-policy-document file://trust-policy.json `
        --query 'Role.Arn' --output text | Set-Variable RoleArn

    # Attach basic execution policy (CloudWatch Logs)
    aws iam attach-role-policy `
        --role-name $RoleName `
        --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

    # Attach Secrets Manager read policy
    $SecretPolicy = @"
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:$Region`:$AccountId`:secret:$SecretName`*"
    }
  ]
}
"@
    $SecretPolicy | Out-File -FilePath "secret-policy.json" -Encoding utf8

    aws iam put-role-policy `
        --role-name $RoleName `
        --policy-name SecretsManagerRead `
        --policy-document file://secret-policy.json

    Write-Host "  ✓ Role created and policies attached" -ForegroundColor Green

    # Wait for role propagation
    Write-Host "  Waiting for IAM role propagation (15s)..." -ForegroundColor Gray
    Start-Sleep -Seconds 15
}

# ─── Step 3: Create or Update Lambda Function ───
Write-Host ""
Write-Host "Step 3: Deploying Lambda function..." -ForegroundColor Yellow

$FunctionExists = $false
try {
    aws lambda get-function --function-name $FunctionName --region $Region >$null 2>&1
    $FunctionExists = $true
} catch { }

if ($FunctionExists) {
    Write-Host "  Updating existing function..." -ForegroundColor Gray
    aws lambda update-function-code `
        --function-name $FunctionName `
        --zip-file fileb://deployment.zip `
        --region $Region | Out-Null

    aws lambda update-function-configuration `
        --function-name $FunctionName `
        --environment "Variables={SECRET_NAME=$SecretName,SECRET_KEY=$SecretKey}" `
        --region $Region | Out-Null

    Write-Host "  ✓ Function updated" -ForegroundColor Green
} else {
    Write-Host "  Creating new function..." -ForegroundColor Gray
    aws lambda create-function `
        --function-name $FunctionName `
        --runtime nodejs20.x `
        --role $RoleArn `
        --handler index.handler `
        --zip-file fileb://deployment.zip `
        --region $Region `
        --timeout 15 `
        --memory-size 128 `
        --environment "Variables={SECRET_NAME=$SecretName,SECRET_KEY=$SecretKey}" | Out-Null

    Write-Host "  ✓ Function created" -ForegroundColor Green
}

# ─── Step 4: Create API Gateway (HTTP API) ───
Write-Host ""
Write-Host "Step 4: Creating API Gateway..." -ForegroundColor Yellow

$ApiId = $null
try {
    # Try to find existing API by name
    $ApiList = aws apigatewayv2 get-apis --region $Region --query "Items[?Name=='$FunctionName-api'].ApiId" --output text 2>$null
    if ($ApiList -and $ApiList -ne "None") {
        $ApiId = $ApiList.Trim()
        Write-Host "  ✓ Existing API found: $ApiId" -ForegroundColor Green
    }
} catch { }

if (-not $ApiId) {
    Write-Host "  Creating new HTTP API..." -ForegroundColor Gray
    $ApiId = aws apigatewayv2 create-api `
        --name "$FunctionName-api" `
        --protocol-type HTTP `
        --target "arn:aws:lambda:$Region`:$AccountId`:function:$FunctionName" `
        --cors-configuration "AllowOrigins=https://clocklobster.com,https://www.clocklobster.com,https://victorsalmon.github.io,AllowMethods=POST,OPTIONS,AllowHeaders=Content-Type,MaxAge=86400" `
        --region $Region `
        --query "ApiId" --output text

    Write-Host "  ✓ API created: $ApiId" -ForegroundColor Green
}

# ─── Step 5: Create Integration ───
Write-Host ""
Write-Host "Step 5: Creating integration..." -ForegroundColor Yellow

$IntegrationId = aws apigatewayv2 get-integrations `
    --api-id $ApiId `
    --region $Region `
    --query "Items[?IntegrationType=='AWS_PROXY'].IntegrationId" --output text 2>$null

if (-not $IntegrationId -or $IntegrationId -eq "None" -or $IntegrationId -eq "") {
    Write-Host "  Creating new integration..." -ForegroundColor Gray
    $IntegrationId = aws apigatewayv2 create-integration `
        --api-id $ApiId `
        --integration-type AWS_PROXY `
        --integration-uri "arn:aws:lambda:$Region`:$AccountId`:function:$FunctionName" `
        --payload-format-version 2.0 `
        --region $Region `
        --query "IntegrationId" --output text
    Write-Host "  ✓ Integration created: $IntegrationId" -ForegroundColor Green
} else {
    Write-Host "  ✓ Integration already exists: $IntegrationId" -ForegroundColor Green
}

# ─── Step 6: Create Route ───
Write-Host ""
Write-Host "Step 6: Creating route..." -ForegroundColor Yellow

$RouteExists = aws apigatewayv2 get-routes `
    --api-id $ApiId `
    --region $Region `
    --query "Items[?RouteKey=='POST /submit']" --output text 2>$null

if (-not $RouteExists -or $RouteExists -eq "None" -or $RouteExists -eq "") {
    Write-Host "  Creating POST /submit route..." -ForegroundColor Gray
    aws apigatewayv2 create-route `
        --api-id $ApiId `
        --route-key "POST /submit" `
        --target "integrations/$IntegrationId" `
        --region $Region | Out-Null
    Write-Host "  ✓ Route created" -ForegroundColor Green
} else {
    Write-Host "  ✓ Route already exists" -ForegroundColor Green
}

# ─── Step 7: Create Stage ───
Write-Host ""
Write-Host "Step 7: Creating stage..." -ForegroundColor Yellow

try {
    aws apigatewayv2 get-stage --api-id $ApiId --stage-name prod --region $Region >$null 2>&1
    Write-Host "  ✓ Stage 'prod' already exists" -ForegroundColor Green
} catch {
    Write-Host "  Creating prod stage..." -ForegroundColor Gray
    aws apigatewayv2 create-stage `
        --api-id $ApiId `
        --stage-name prod `
        --auto-deploy `
        --default-route-settings "ThrottlingBurstLimit=20,ThrottlingRateLimit=10" `
        --region $Region | Out-Null
    Write-Host "  ✓ Stage created" -ForegroundColor Green
}

# ─── Step 8: Add Lambda Permission ───
Write-Host ""
Write-Host "Step 8: Adding Lambda permission..." -ForegroundColor Yellow

try {
    aws lambda add-permission `
        --function-name $FunctionName `
        --statement-id apigateway-invoke `
        --action lambda:InvokeFunction `
        --principal apigateway.amazonaws.com `
        --source-arn "arn:aws:execute-api:$Region`:$AccountId`:$ApiId`/*" `
        --region $Region | Out-Null
    Write-Host "  ✓ Permission added" -ForegroundColor Green
} catch {
    Write-Host "  Permission already exists (or other error, safe to ignore)" -ForegroundColor Gray
}

# ─── Step 9: Output ───
Write-Host ""
Write-Host "=== Deployment Complete ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "API Endpoint URL:" -ForegroundColor Yellow
Write-Host "  https://$ApiId`.execute-api.$Region`.amazonaws.com/prod/submit" -ForegroundColor White
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Copy the API URL above" -ForegroundColor White
Write-Host "  2. Paste it into js/main.js → FORM_API_URL" -ForegroundColor White
Write-Host "  3. Commit and push to GitHub" -ForegroundColor White
Write-Host ""
Write-Host "Test with:" -ForegroundColor Yellow
Write-Host "  curl -X POST https://$ApiId`.execute-api.$Region`.amazonaws.com/prod/submit `" -ForegroundColor Gray
Write-Host "    -H 'Content-Type: application/json' `" -ForegroundColor Gray
Write-Host "    -d '{`"name`":`"Test`",`"email`":`"test@example.com`"}'" -ForegroundColor Gray

# Cleanup
Remove-Item -Path "deployment.zip" -ErrorAction SilentlyContinue
Remove-Item -Path "trust-policy.json" -ErrorAction SilentlyContinue
Remove-Item -Path "secret-policy.json" -ErrorAction SilentlyContinue
