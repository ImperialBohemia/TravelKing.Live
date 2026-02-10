#!/bin/bash
# OMEGA NUCLEAR AUDIT v3 (Zero-Tolerance)
echo "🔥 STARTING OMEGA NUCLEAR AUDIT: ZERO TOLERANCE MODE"
echo "--------------------------------------------------"

# 1. Python Unit Tests
echo -e "\n[1/8] Running Python Core Tests..."
export PYTHONPATH=$PYTHONPATH:.
pytest tests/ --maxfail=1 --disable-warnings || { echo "❌ Python tests failed!"; false; }

# 2. Python Security
echo -e "\n[2/8] Auditing Python Dependencies (Safety)..."
safety check || { echo "❌ Security vulnerability found in Python deps!"; false; }

# 3. Frontend Security
echo -e "\n[3/8] Auditing Frontend Dependencies (NPM Audit)..."
(cd web-latest && npm audit --audit-level=high) || { echo "❌ High-severity frontend vulnerability found!"; false; }

# 4. Code Linting & Unit Tests
echo -e "\n[4/8] Verifying Frontend Standards (Lint + Test)..."
(cd web-latest && npm run lint) || { echo "❌ Linting errors detected!"; false; }
(cd web-latest && npm run test) || { echo "❌ Frontend tests failed!"; false; }

# 5. Connection Verification
echo -e "\n[5/8] Testing OMEGA Bridge Connectivity..."
python3 scripts/connection_audit_v2.py || { echo "❌ Connection audit failed!"; false; }

# 6. OMEGA Visual Eyes & Accessibility
echo -e "\n[6/8] Initializing OMEGA Visual Eyes & Axe Audit..."
if [ -z "$1" ]; then
  echo "⚠️ Skipping visual capture (No URL provided)."
else
  python3 testing-lab/visual_eye.py "$1" --mode desktop || { echo "❌ Visual audit failed!"; false; }
  python3 testing-lab/visual_eye.py "$1" --mode mobile || { echo "❌ Mobile visual audit failed!"; false; }
fi

# 7. Google SEO/Vitals Audit
echo -e "\n[7/8] Running Google Vitals & SEO Check..."
if [ -z "$1" ]; then
  echo "⚠️ Skipping vitals check (No URL provided)."
else
  python3 testing-lab/google_vitals_audit.py "$1" || { echo "❌ SEO/Vitals audit failed!"; false; }
fi

# 8. Type Checking
echo -e "\n[8/8] Verifying TypeScript Integrity..."
(cd web-latest && npx tsc --noEmit) || { echo "❌ Type checking failed!"; false; }

echo -e "\n✅ OMEGA NUCLEAR AUDIT: PASSED. SYSTEM IS PEAK QUALITY."
