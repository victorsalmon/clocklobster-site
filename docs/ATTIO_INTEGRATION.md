# Attio CRM Integration

## Overview

Attio is an AI-native CRM platform. There is no direct WordPress → Attio plugin, so we use WP Webhooks (or Fluent Forms Pro webhooks) to bridge the gap.

**Data Flow:**
```
WordPress Form Submission
    ↓
WP Webhooks captures event
    ↓
Data is formatted and sent to Attio REST API
    ↓
Attio creates/updates Person, Company, and Note records
```

## Attio API Basics

**Base URL:** `https://api.attio.com/v2/`
**Authentication:** Bearer token in Authorization header
**Content-Type:** `application/json`

**Getting your API token:**
1. Log in to Attio
2. Settings → Developers → API Keys
3. Generate new key with appropriate scopes

## Webhook Payload Examples

### Create/Update a Person

**Endpoint:** `POST /v2/objects/people/records`

```json
{
  "data": {
    "values": {
      "email_addresses": [
        {
          "email_address": "{{email}}"
        }
      ],
      "first_name": "{{first_name}}",
      "last_name": "{{last_name}}"
    }
  }
}
```

### Create/Update a Company

**Endpoint:** `POST /v2/objects/companies/records`

```json
{
  "data": {
    "values": {
      "name": "{{company}}",
      "domains": [
        {
          "domain": "{{email_domain}}"
        }
      ]
    }
  }
}
```

### Create a Note

**Endpoint:** `POST /v2/notes`

```json
{
  "data": {
    "parent_object": "people",
    "parent_record_id": "{{attio_person_id}}",
    "title": "Contact form submission from {{first_name}} {{last_name}}",
    "content": "{{message}}\n\nBudget Range: {{budget_range}}"
  }
}
```

### Create a Task (Follow-up Reminder)

**Endpoint:** `POST /v2/tasks`

```json
{
  "data": {
    "name": "Follow up with {{first_name}} from {{company}}",
    "content": "Contact form submission. Budget: {{budget_range}}. Message: {{message}}",
    "deadline_at": "{{+2days}}",
    "assigned_to": [
      {
        "workspace_member_id": "{{your_member_id}}"
      }
    ]
  }
}
```

## Field Mapping Reference

| WordPress Form Field | Attio Object | Attio Field |
|---------------------|--------------|-------------|
| Name | Person | `first_name`, `last_name` |
| Email | Person | `email_addresses` |
| Company | Company | `name` |
| Message | Note | `content` |
| Budget Range | Note / Custom | `content` or custom field |
| Submission Date | Note | `created_at` (auto) |
| Page Source | Note | `content` (append metadata) |

## WP Webhooks Configuration Steps

### Step 1: Install WP Webhooks Integration for Fluent Forms
WP Webhooks has a built-in integration for Fluent Forms. Enable it in WP Webhooks → Integrations.

### Step 2: Create Automation Flow
1. WP Webhooks → Automations → Add New
2. **Name:** "Contact Form to Attio"
3. **Trigger:** Fluent Forms → "Form submitted"
4. **Select Form:** Your contact form ID

### Step 3: Add Condition (Optional)
Only send to Attio if email is valid:
- Condition: `email` is not empty
- This prevents empty test submissions from creating records

### Step 4: Add Action — Create Person
1. Action: "Send webhook"
2. URL: `https://api.attio.com/v2/objects/people/records`
3. Method: POST
4. Headers:
   ```
   Authorization: Bearer YOUR_API_TOKEN
   Content-Type: application/json
   ```
5. Body: JSON payload (see example above)
6. Use WP Webhooks dynamic variables to map form fields: `{{fluent_forms_email}}`, `{{fluent_forms_first_name}}`, etc.

### Step 5: Add Action — Create Note
1. Add second action to same flow
2. Action: "Send webhook"
3. URL: `https://api.attio.com/v2/notes`
4. Method: POST
5. Headers: same as above
6. Body: Note JSON with message content

### Step 6: Test
1. Submit test contact form
2. Check WP Webhooks → Logs for response codes
3. Verify in Attio that Person and Note were created
4. Check for errors and adjust payload if needed

## Handling Duplicates

Attio's API is upsert-based for records with unique identifiers (like email). If you send a Person with an email that already exists, Attio will update the existing record rather than create a duplicate.

For Companies, Attio matches on domain name. If `company.com` already exists, it updates rather than duplicates.

## Error Handling

**Common Issues:**

| Error | Cause | Fix |
|-------|-------|-----|
| 401 Unauthorized | Invalid API token | Regenerate token in Attio settings |
| 400 Bad Request | Malformed JSON | Validate JSON syntax in payload |
| 422 Unprocessable | Missing required field | Ensure `email_addresses` array format is correct |
| 429 Too Many | Rate limiting | Add delay between actions in WP Webhooks |

**WP Webhooks Logs:**
Check WP Webhooks → Logs for full request/response details. Enable "Debug mode" temporarily if needed.

## Alternative: Fluent Forms Pro Webhooks

If you prefer not to use WP Webhooks, Fluent Forms Pro has native webhook support:

1. Fluent Forms → Forms → Edit Contact Form
2. Settings & Integrations → Webhooks
3. Add webhook URL: `https://api.attio.com/v2/objects/people/records`
4. Set method, headers, and payload
5. Map fields using Fluent Forms smart tags

**Pros:** Simpler setup, no extra plugin
**Cons:** Less flexible data transformation, no conditional logic, no retry on failure

## Attio Object Structure Recommendations

### Recommended Custom Objects
Consider creating these custom objects in Attio to track automation opportunities:

| Object | Purpose |
|--------|---------|
| Opportunities | Track consultation bookings and proposals |
| Automations | Log deployed automations per client |
| Interactions | All touchpoints (calls, emails, meetings) |

### Recommended Lists
- **Pipeline:** Opportunities → stages: New Lead, Consultation Booked, Proposal Sent, Closed Won, Closed Lost
- **Leads:** People who submitted forms but haven't booked yet
- **Clients:** Active customers with deployed automations

## Security Notes

- Store Attio API token securely. Never commit it to version control.
- Use WordPress `wp-config.php` constants or environment variables for the token.
- In WP Webhooks, the token is stored in the database (encrypted if possible).
- Restrict Attio API token permissions to minimum required scopes.
- Rotate API tokens every 90 days.

## Testing Checklist

- [ ] Submit contact form → Person created in Attio
- [ ] Submit with existing email → Person updated (not duplicated)
- [ ] Note attached to correct Person
- [ ] Company created/linked if provided
- [ ] Task created for follow-up (if configured)
- [ ] Error logs are clean
- [ ] Webhook response time < 3 seconds
- [ ] Form still shows success message to user even if webhook fails

## Resources

- Attio REST API Docs: https://docs.attio.com/rest-api/overview
- Attio Objects & Lists: https://docs.attio.com/docs/objects-and-lists
- WP Webhooks Docs: https://wp-webhooks.com/docs
- Attio Pricing: https://attio.com/pricing
