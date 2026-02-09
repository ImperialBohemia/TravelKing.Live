
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
  backup: "https://imperialbohemia.github.io"
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
