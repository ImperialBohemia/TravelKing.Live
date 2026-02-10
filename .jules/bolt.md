
## 2026-02-10 - Persistence in Stateless Bots
**Learning:** Found a critical performance anti-pattern where a bot re-processed all historical data on every run because state was in-memory only.
**Action:** Always implement simple file-based persistence (JSON) for bots to track processed items, especially when API quotas (Gmail/Sheets) are involved. Prevents exponential cost growth.
