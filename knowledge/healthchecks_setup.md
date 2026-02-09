
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
