# 🧪 OMEGA Testing Lab (v2026.MAX)

The OMEGA Testing Lab is the mandatory staging area for all system changes. Nothing enters production without passing the "Nuclear Audit" defined here.

## 🛠️ Tools Installed
- **Unit (Python)**: `pytest` - Testing core logic and connectors.
- **Unit (Next.js)**: `Jest` / `React Testing Library` - Testing UI components.
- **E2E**: `Playwright` - Full system flow verification.
- **Performance**: `Lighthouse` - Speed and SEO audit.
- **Security**: `Safety` & `npm audit` - Dependency vulnerability checks.

## 🚀 Running the Audit
To run a full system check, execute:
```bash
bash testing-lab/run_audit.sh
```

## 🔬 Lab Modules
- `unit/`: Scripted logic tests.
- `e2e/`: Browser-based user flow simulations.
- `performance/`: Speed metrics and hydration checks.
- `security/`: Credential leak detection and dependency audits.
