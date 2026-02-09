/**
 * OMEGA Lead Magnet Trigger
 * Attached to Google Sheet: 1uvNvNKei8sgmrASHE5OpQKwEANcOFjxOCdIxMWBnOQc
 */

function onFormSubmit(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var lastRow = sheet.getLastRow();
  var range = sheet.getRange(lastRow, 1, 1, sheet.getLastColumn());
  var values = range.getValues()[0];

  // 1. DATA ENRICHMENT
  // Assume: Col 3 is Name, Col 4 is Email, Col 5 is Destination
  var name = values[2];
  var email = values[3];
  var destination = values[4];

  // 2. AUTO-VALIDATION
  if (!validateEmail(email)) {
    sheet.getRange(lastRow, 6).setValue("ERROR: INVALID_EMAIL");
    return;
  }

  // 3. SET STATUS FOR CONCIERGE BOT
  sheet.getRange(lastRow, 6).setValue("0_NEW");
  sheet.getRange(lastRow, 7).setValue("⚡ MEDIUM"); // Default priority

  // 4. INSTANT NOTIFICATION (Simple)
  MailApp.sendEmail("info@simplecode.space", "🔥 NEW LEAD: " + name, "Destination: " + destination + "\nEmail: " + email);

  // 5. COLOR CODING
  range.setBackground("#fff9db"); // Yellow highlight for new items
}

function validateEmail(email) {
  var re = /^(([^<>()\[\]\.,;:\s@"]+(\.[^<>()\[\]\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

/**
 * Setup trigger via script
 */
function createTrigger() {
  var sheet = SpreadsheetApp.getActive();
  ScriptApp.newTrigger('onFormSubmit')
    .forSpreadsheet(sheet)
    .onFormSubmit()
    .create();
}
