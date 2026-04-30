import { SecretsManagerClient, GetSecretValueCommand } from '@aws-sdk/client-secrets-manager';
import { SESClient, SendEmailCommand } from '@aws-sdk/client-ses';

var ALLOWED_ORIGINS = [
    'https://clocklobster.com',
    'https://www.clocklobster.com',
    'https://victorsalmon.github.io'
];

var ATTIO_API_BASE = 'https://api.attio.com/v2';
var secretsClient = new SecretsManagerClient({ region: 'ca-central-1' });
var sesClient = new SESClient({ region: 'ca-central-1' });
var cachedApiKey = null;

async function getAttioApiKey() {
    if (cachedApiKey) return cachedApiKey;

    var command = new GetSecretValueCommand({
        SecretId: process.env.SECRET_NAME || 'ClockLobster/Site/Secrets'
    });

    var response = await secretsClient.send(command);
    var secrets = JSON.parse(response.SecretString);
    cachedApiKey = secrets[process.env.SECRET_KEY || 'ATTIO_WEB_FORM1_KEY'];
    if (!cachedApiKey) {
        throw new Error('Attio API key not found in secret: ' + (process.env.SECRET_KEY || 'ATTIO_WEB_FORM1_KEY'));
    }
    return cachedApiKey;
}

async function attioPost(endpoint, body, apiKey) {
    var response = await fetch(ATTIO_API_BASE + endpoint, {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + apiKey,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    });

    if (!response.ok) {
        var errorText = await response.text();
        throw new Error('Attio ' + response.status + ': ' + errorText);
    }

    return response.json();
}

async function sendNotification(data) {
    try {
        var subject = 'New Clock Lobster form submission: ' + (data.source || 'website');
        var bodyLines = [
            'Name: ' + data.name,
            'Email: ' + data.email,
            'Company: ' + (data.company || 'N/A'),
            'Source: ' + (data.source || 'website'),
            'Budget: ' + (data.budget || 'N/A'),
            '',
            'Message:',
            data.message || 'No message provided'
        ];

        var command = new SendEmailCommand({
            Source: process.env.NOTIFY_FROM || 'hello@clocklobster.com',
            Destination: {
                ToAddresses: [(process.env.NOTIFY_TO || 'hello@clocklobster.com')]
            },
            Message: {
                Subject: { Data: subject },
                Body: {
                    Text: { Data: bodyLines.join('\n') }
                }
            }
        });

        await sesClient.send(command);
        console.log('Notification email sent');
    } catch (err) {
        console.error('Email notification failed (non-fatal):', err.message);
    }
}

function parseName(fullName) {
    if (!fullName) return { first_name: '', last_name: '' };
    var parts = fullName.trim().split(/\s+/);
    return {
        first_name: parts[0] || '',
        last_name: parts.slice(1).join(' ') || ''
    };
}

function getEmailDomain(email) {
    if (!email || !email.includes('@')) return null;
    return email.split('@')[1];
}

function buildCorsHeaders(origin) {
    var allowed = ALLOWED_ORIGINS.indexOf(origin) !== -1 ? origin : '';
    return {
        'Access-Control-Allow-Origin': allowed,
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    };
}

function jsonResponse(statusCode, body, corsHeaders) {
    return {
        statusCode: statusCode,
        headers: Object.assign({}, corsHeaders, { 'Content-Type': 'application/json' }),
        body: JSON.stringify(body)
    };
}

export var handler = async function(event) {
    var origin = (event.headers && (event.headers.origin || event.headers.Origin)) || '';
    var corsHeaders = buildCorsHeaders(origin);

    if (event.requestContext && event.requestContext.http && event.requestContext.http.method === 'OPTIONS') {
        return { statusCode: 204, headers: corsHeaders, body: '' };
    }

    try {
        var body;
        try {
            body = JSON.parse(event.body || '{}');
        } catch (e) {
            return jsonResponse(400, { error: 'Invalid request body' }, corsHeaders);
        }

        var name = (body.name || '').trim();
        var email = (body.email || '').trim().toLowerCase();
        var company = (body.company || '').trim();
        var message = (body.message || '').trim();
        var budget = (body.budget || '').trim();
        var source = (body.source || '').trim();

        if (!name || !email) {
            return jsonResponse(400, { error: 'Name and email are required' }, corsHeaders);
        }

        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            return jsonResponse(400, { error: 'Invalid email address' }, corsHeaders);
        }

        var apiKey = await getAttioApiKey();
        var parsed = parseName(name);

        var personResponse = await attioPost(
            '/objects/people/records?matching_attribute=email_addresses',
            {
                data: {
                    values: {
                        email_addresses: [{ email_address: email }]
                    }
                }
            },
            apiKey
        );

        var personId = personResponse.data && personResponse.data.id && personResponse.data.id.record_id;

        if (company) {
            var domain = getEmailDomain(email);
            try {
                await attioPost(
                    '/objects/companies/records' + (domain ? '?matching_attribute=domains' : ''),
                    {
                        data: {
                            values: {
                                name: company,
                                domains: domain ? [{ domain: domain }] : []
                            }
                        }
                    },
                    apiKey
                );
            } catch (err) {
                console.error('Company upsert failed (non-fatal):', err.message);
            }
        }

        if (personId) {
            try {
                var noteParts = [];
                if (source) noteParts.push('**Source:** ' + source);
                if (company) noteParts.push('**Company:** ' + company);
                if (budget) noteParts.push('**Budget:** ' + budget);
                if (message) noteParts.push('**Message:**\n' + message);

                await attioPost(
                    '/notes',
                    {
                        data: {
                            parent_object: 'people',
                            parent_record_id: personId,
                            title: 'Website form: ' + (source || 'submission'),
                            content: noteParts.join('\n\n') || 'No details provided'
                        }
                    },
                    apiKey
                );
            } catch (err) {
                console.error('Note creation failed (non-fatal):', err.message);
            }
        }

        await sendNotification({ name, email, company, source, budget, message });

        return jsonResponse(200, { success: true, personId: personId || null }, corsHeaders);

    } catch (error) {
        console.error('Form handler error:', error);
        return jsonResponse(500, { error: error.message || 'Internal error' }, corsHeaders);
    }
};
