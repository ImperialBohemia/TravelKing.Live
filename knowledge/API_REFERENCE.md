# OMEGA API REFERENCE: Official Documentation Links

## Google Cloud APIs (Free Tier)

| API | Documentation | Scope | Quota (Free) |
|-----|---------------|-------|--------------|
| Gmail API | [Reference](https://developers.google.com/gmail/api/reference/rest) | `gmail.send` | 500 emails/day |
| Sheets API | [Reference](https://developers.google.com/sheets/api/reference/rest) | `spreadsheets` | 60 req/min |
| Drive API | [Reference](https://developers.google.com/drive/api/reference/rest/v3) | `drive` | 1B queries/day |
| Indexing API | [Reference](https://developers.google.com/search/apis/indexing-api/v3/reference) | `indexing` | 200 URLs/day |
| Forms API | [Reference](https://developers.google.com/forms/api/reference/rest) | via Sheets | N/A |

## Bing / Microsoft

| API | Documentation | Quota |
|-----|---------------|-------|
| IndexNow | [Docs](https://www.indexnow.org/documentation) | Unlimited |
| Webmaster API | [Docs](https://docs.microsoft.com/en-us/bingwebmaster/) | High |

## Travelpayouts

| API | Documentation | Use |
|-----|---------------|-----|
| Aviasales | [API Docs](https://support.travelpayouts.com/hc/en-us/categories/200358578) | Flights |
| Hotellook | [API Docs](https://support.travelpayouts.com/hc/en-us/articles/115000343268) | Hotels |
| Statistics | [API Docs](https://support.travelpayouts.com/hc/en-us/articles/203956163) | Revenue |

## Authentication

All Google APIs use OAuth 2.0 with the Cloud SDK Client ID:
- **Client ID:** `764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com`
- **Token Refresh:** Standard `refresh_token` flow with `client_secret`
