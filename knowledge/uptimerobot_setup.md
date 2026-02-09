
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
