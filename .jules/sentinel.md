## 2026-02-10 - [Critical SSL Vulnerability in cPanel Connector]
**Vulnerability:** The cPanel connector was using `verify=False` for all requests, exposing credentials and data to MITM attacks.
**Learning:** This was likely a workaround for self-signed certificates in early development but persisted into production code.
**Prevention:** Default to `verify=True` in all connectors. Allow explicit opt-out via configuration (`verify_ssl=False`) only when necessary, but never hardcode it.
