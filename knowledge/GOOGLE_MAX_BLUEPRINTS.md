# ☁️ OMEGA GOOGLE-MAX ENTERPRISE BLUEPRINTS

This document defines the "Gold Standard" implementation for the TravelKing OMEGA integration with Google Cloud and Workspace.

## 🏗️ THE SERVICE FACTORY PATTERN
All Google API interactions are centralized via `core/google/factory.py`.
- **Official SDKs:** We use the official `google-api-python-client` and `google-cloud-secret-manager` libraries.
- **Discovery Service:** Services are built dynamically to ensure compatibility with the latest API versions.
- **Quota Protection:** Atomic operations (BatchRequests) are prioritized to maximize throughput within free-tier limits.

## 🔐 SECURITY & SECRET MANAGEMENT
We follow the **Zero-Leak Policy**:
1. **Google Secret Manager:** Sensitive keys (Refresh Tokens, Client Secrets) are stored in the cloud.
2. **Local Fallback:** Non-sensitive or local-dev config resides in `access_vault.json`.
3. **IAM Least Privilege:** The system uses Service Accounts (`travelking@...`) with scoped access only to required resources.

## 📈 INTELLIGENCE LAYER (GA4)
- **Data-Driven Strikes:** The `AnalyticsClient` fetches real-time engagement metrics from GA4.
- **ROI Optimization:** Sniper strikes are prioritized for routes with high "activeUsers" and "screenPageViews" signals.

## 🛡️ RELIABILITY (EXPONENTIAL BACKOFF)
Every official Google API call is wrapped in the `@google_api_backoff` decorator.
- **Error Handling:** Automatically handles 429 (Rate Limit) and 5xx (Server) errors.
- **Jitter Logic:** Prevents "Thundering Herd" issues during concurrent bot operations.

---
**GOOGLE-MAX | DATA SOVEREIGNTY | 2026**
