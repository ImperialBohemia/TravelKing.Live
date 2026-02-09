#!/home/q/TravelKing.Live/venv/bin/python3
"""
Enterprise MAX Monitoring - 100% FREE TIER
Triple Redundancy: Google Apps Script + UptimeRobot + Internal Guardian
"""

import json
import os
import sys
import requests
from loguru import logger

class FreeMonitoringStack:
    """Zero-cost Enterprise monitoring with triple redundancy"""
    
    def __init__(self):
        self.root = "/home/q/TravelKing.Live"
        sys.path.append(self.root)
        
        vault_path = os.path.join(self.root, "config/access_vault.json")
        with open(vault_path, 'r') as f:
            self.vault = json.load(f)
    
    def generate_apps_script_monitor(self):
        """
        Generates Google Apps Script code for 24/7 monitoring.
        This runs in Google's infrastructure for FREE, forever.
        """
        logger.info("📝 Generating Google Apps Script Monitor...")
        
        script = """
/**
 * TravelKing.Live - Enterprise Monitoring (Google Apps Script)
 * AUTO-RUNS EVERY MINUTE - 100% FREE FOREVER
 * 
 * Setup Instructions:
 * 1. Open Google Sheets → Extensions → Apps Script
 * 2. Paste this code
 * 3. Click "Triggers" (clock icon) → Add Trigger
 * 4. Choose: monitorSystem, Time-driven, Minutes timer, Every 1 minute
 * 5. Save and you're done!
 */

const ENDPOINTS = {
  website: "https://www.travelking.live",
  cpanel: "https://server707.web-hosting.com:2083",
  backup: "https://imperialbohe mia.github.io"
};

const SHEET_NAME = "SYSTEM_STATUS";
const ALERT_EMAIL = "valachman@gmail.com";

function monitorSystem() {
  const sheet = getOrCreateSheet();
  const timestamp = new Date();
  let allHealthy = true;
  
  // Check each endpoint
  for (const [name, url] of Object.entries(ENDPOINTS)) {
    try {
      const response = UrlFetchApp.fetch(url, {
        muteHttpExceptions: true,
        followRedirects: false,
        validateHttpsCertificates: false
      });
      
      const status = response.getResponseCode();
      const isHealthy = status >= 200 && status < 400;
      
      // Log to sheet
      sheet.appendRow([
        timestamp,
        name,
        status,
        isHealthy ? "✅ ONLINE" : "🔴 DOWN",
        url
      ]);
      
      if (!isHealthy) {
        allHealthy = false;
        sendAlert(name, url, status);
      }
      
    } catch (error) {
      sheet.appendRow([timestamp, name, "ERROR", "🔴 FAILED", error.toString()]);
      allHealthy = false;
      sendAlert(name, url, error.toString());
    }
  }
  
  // Keep sheet clean (max 1000 rows)
  if (sheet.getLastRow() > 1000) {
    sheet.deleteRows(2, 100);
  }
  
  // Update dashboard cell
  const dashboardSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Dashboard");
  if (dashboardSheet) {
    dashboardSheet.getRange("B2").setValue(allHealthy ? "🟢 ALL SYSTEMS OPERATIONAL" : "🔴 CRITICAL ALERT");
    dashboardSheet.getRange("B3").setValue(timestamp);
  }
}

function getOrCreateSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow(["Timestamp", "Service", "Status Code", "Health", "URL"]);
    sheet.getRange("A1:E1").setFontWeight("bold").setBackground("#000000").setFontColor("#ffffff");
  }
  
  return sheet;
}

function sendAlert(service, url, error) {
  const subject = `🚨 TravelKing ALERT: ${service} DOWN`;
  const body = `
CRITICAL SYSTEM ALERT
=====================

Service: ${service}
URL: ${url}
Error: ${error}
Time: ${new Date()}

This is an automated alert from your TravelKing.Live monitoring system.
Action required: Check the service immediately.

---
Powered by OMEGA Guardian Protocol
  `;
  
  try {
    MailApp.sendEmail(ALERT_EMAIL, subject, body);
  } catch (e) {
    Logger.log("Failed to send alert email: " + e);
  }
}

function setupDashboard() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let dashboard = ss.getSheetByName("Dashboard");
  
  if (!dashboard) {
    dashboard = ss.insertSheet("Dashboard", 0);
  }
  
  dashboard.getRange("A1").setValue("TravelKing.Live - SYSTEM HEALTH").setFontSize(18).setFontWeight("bold");
  dashboard.getRange("A2").setValue("Status:");
  dashboard.getRange("A3").setValue("Last Check:");
  dashboard.getRange("B2").setValue("🟢 INITIALIZING...");
  
  dashboard.setColumnWidth(1, 150);
  dashboard.setColumnWidth(2, 300);
}
""".replace("imperialbohe mia", "imperialbohemia")
        
        script_path = os.path.join(self.root, "knowledge/google_apps_script_monitor.js")
        with open(script_path, 'w') as f:
            f.write(script)
        
        logger.success(f"✅ Apps Script generated: {script_path}")
        return script_path
    
    def setup_uptimerobot_guide(self):
        """Creates setup guide for UptimeRobot (backup monitoring)"""
        logger.info("📝 Generating UptimeRobot Setup Guide...")
        
        guide = """
# UptimeRobot Setup Guide (FREE Tier)

## Why UptimeRobot?
- **50 monitors FREE** (we need only 3)
- **5-minute interval** checks
- **Email/SMS/Webhook alerts**
- **99.9% uptime** of monitoring itself
- **Public status page** (optional)

## Setup Steps:

### 1. Create Account
- Go to: https://uptimerobot.com/signUp
- Use email: valachman@gmail.com
- Verify email

### 2. Add Monitors

#### Monitor 1: TravelKing.Live Website
- **Monitor Type:** HTTP(s)
- **Friendly Name:** TravelKing - Main Website
- **URL:** https://www.travelking.live
- **Monitoring Interval:** 5 minutes
- **Alert Contacts:** Your email

#### Monitor 2: cPanel Infrastructure  
- **Monitor Type:** Port
- **Friendly Name:** cPanel Server707
- **URL:** server707.web-hosting.com
- **Port:** 2083
- **Monitoring Interval:** 5 minutes

#### Monitor 3: GitHub Pages (Backup)
- **Monitor Type:** HTTP(s)
- **Friendly Name:** GitHub Backup Site
- **URL:** https://imperialbohemia.github.io
- **Monitoring Interval:** 5 minutes

### 3. Configure Alerts
- Go to "My Settings" → "Alert Contacts"
- Add your email
- Enable alerts for: Down, Up
- Optional: Add webhook to call our Guardian API

### 4. API Integration (Optional)
Once set up, get your API key and add to:
```
/home/q/TravelKing.Live/config/access_vault.json
```

Add this section:
```json
"uptimerobot": {
  "api_key": "YOUR_API_KEY_HERE"
}
```

## Result:
✅ External monitoring from 10+ global locations
✅ Instant email alerts on downtime
✅ Historical uptime statistics
✅ 100% FREE forever
"""
        
        guide_path = os.path.join(self.root, "knowledge/uptimerobot_setup.md")
        with open(guide_path, 'w') as f:
            f.write(guide)
        
        logger.success(f"✅ UptimeRobot guide created: {guide_path}")
        return guide_path
    
    def create_healthchecks_io_monitor(self):
        """Creates Healthchecks.io configuration for heartbeat monitoring"""
        logger.info("📝 Setting up Healthchecks.io configuration...")
        
        guide = """
# Healthchecks.io Setup (FREE Cron/Heartbeat Monitoring)

## Why Healthchecks.io?
- **20 checks FREE**
- **Heartbeat monitoring** - detects if OUR scripts stop running
- **Cron monitoring** - perfect for Guardian Protocol
- **Dead man's switch** - alerts if no ping received

## Setup:

### 1. Create Account
- URL: https://healthchecks.io/signup/
- Email: valachman@gmail.com

### 2. Create Check
- **Name:** TravelKing Guardian Heartbeat
- **Period:** 5 minutes
- **Grace Time:** 2 minutes
- **Description:** Internal Guardian Protocol health

### 3. Get Ping URL
After creating, you'll get a URL like:
```
https://hc-ping.com/YOUR-UUID-HERE
```

### 4. Add to Our Guardian
We'll modify Guardian to ping this URL every 3 minutes.
If Guardian dies/crashes, Healthchecks.io will alert you.

### 5. Add to Crontab
```bash
*/3 * * * * curl -fsS --retry 3 https://hc-ping.com/YOUR-UUID-HERE > /dev/null
```

This ensures even if our Python scripts fail, the server itself is monitored.

## Triple Protection:
1. ✅ Google Apps Script monitors external endpoints
2. ✅ UptimeRobot monitors from 10+ locations
3. ✅ Healthchecks.io monitors that our monitors are running!
"""
        
        hc_path = os.path.join(self.root, "knowledge/healthchecks_setup.md")
        with open(hc_path, 'w') as f:
            f.write(guide)
        
        logger.success(f"✅ Healthchecks.io guide created: {hc_path}")
        return hc_path
    
    def deploy_free_monitoring_stack(self):
        """Deploys complete free monitoring infrastructure"""
        logger.info("🚀 Deploying FREE Enterprise Monitoring Stack...")
        
        results = {
            "apps_script": self.generate_apps_script_monitor(),
            "uptimerobot_guide": self.setup_uptimerobot_guide(),
            "healthchecks_guide": self.create_healthchecks_io_monitor()
        }
        
        logger.success("💎 FREE Monitoring Stack: READY TO DEPLOY")
        logger.info("")
        logger.info("=" * 60)
        logger.info("NEXT STEPS:")
        logger.info("=" * 60)
        logger.info("1. Open your TravelKing Google Sheet")
        logger.info("2. Extensions → Apps Script → Paste the code")
        logger.info(f"   (Located at: {results['apps_script']})")
        logger.info("")
        logger.info("3. Setup UptimeRobot account (5 min)")
        logger.info(f"   (Guide: {results['uptimerobot_guide']})")
        logger.info("")
        logger.info("4. Setup Healthchecks.io (2 min)")
        logger.info(f"   (Guide: {results['healthchecks_guide']})")
        logger.info("=" * 60)
        logger.info("")
        logger.success("✅ Total Cost: $0.00/month")
        logger.success("✅ Monitoring Locations: 10+ global")
        logger.success("✅ Check Frequency: Every 1-5 minutes")
        logger.success("✅ Redundancy Level: TRIPLE")
        
        return results

if __name__ == "__main__":
    monitor = FreeMonitoringStack()
    result = monitor.deploy_free_monitoring_stack()
