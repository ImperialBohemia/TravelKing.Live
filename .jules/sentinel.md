## 2026-02-10 - [Critical SSL Vulnerability in cPanel Connector]
**Vulnerability:** The cPanel connector was using `verify=False` for all requests, exposing credentials and data to MITM attacks.
**Learning:** This was likely a workaround for self-signed certificates in early development but persisted into production code.
**Prevention:** Default to `verify=True` in all connectors. Allow explicit opt-out via configuration (`verify_ssl=False`) only when necessary, but never hardcode it.

## 2026-02-11 - [Eliminated Hardcoded SSL Verification Bypass]
**Vulnerability:** Multiple core connectors and deployment scripts had hardcoded `verify=False` for SSL requests, bypassing critical security checks.
**Learning:** While intended for local development with self-signed certificates, hardcoding this bypass in production code creates a permanent MITM vulnerability.
**Prevention:** Always use a configurable `verify_ssl` parameter with a default of `True`. Move warning suppression (urllib3) to be conditional based on this configuration.
