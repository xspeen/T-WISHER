#!/usr/bin/env python3
"""
Tunnel Manager Module for T-WISHER
Handles all tunneling operations
"""

import os
import subprocess
import threading
import time
import socket
import requests
import platform

class TunnelManager:
    def __init__(self):
        self.system = platform.system()
        self.tunnels = {}
    
    def start_ngrok(self, port):
        """Start ngrok tunnel"""
        try:
            # Check if ngrok is installed
            if self.system == "Windows":
                ngrok_cmd = "ngrok.exe"
            else:
                ngrok_cmd = "ngrok"
            
            # Start ngrok in background
            def run_ngrok():
                subprocess.Popen(
                    [ngrok_cmd, "http", str(port)],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            
            thread = threading.Thread(target=run_ngrok)
            thread.daemon = True
            thread.start()
            
            # Wait for ngrok to start
            time.sleep(3)
            
            # Get public URL
            try:
                response = requests.get("http://localhost:4040/api/tunnels")
                if response.status_code == 200:
                    data = response.json()
                    public_url = data['tunnels'][0]['public_url']
                    self.tunnels['ngrok'] = public_url
                    return public_url
            except:
                pass
            
            return None
        except Exception as e:
            print(f"[!] Ngrok error: {e}")
            return None
    
    def start_serveo(self, port):
        """Start serveo.net tunnel"""
        try:
            # Generate random subdomain
            import random
            import string
            subdomain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            
            # SSH command
            if self.system == "Windows":
                # Windows needs additional setup
                print("[!] Serveo.net on Windows requires SSH client")
                ssh_cmd = f"ssh -R {subdomain}:80:localhost:{port} serveo.net"
            else:
                ssh_cmd = f"ssh -o StrictHostKeyChecking=no -R {subdomain}:80:localhost:{port} serveo.net"
            
            def run_serveo():
                subprocess.Popen(
                    ssh_cmd.split(),
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            
            thread = threading.Thread(target=run_serveo)
            thread.daemon = True
            thread.start()
            
            time.sleep(3)
            public_url = f"https://{subdomain}.serveo.net"
            self.tunnels['serveo'] = public_url
            return public_url
            
        except Exception as e:
            print(f"[!] Serveo.net error: {e}")
            return None
    
    def start_cloudflared(self, port):
        """Start cloudflared tunnel"""
        try:
            if self.system == "Windows":
                cf_cmd = "cloudflared.exe"
            else:
                cf_cmd = "cloudflared"
            
            # Check if cloudflared exists
            import shutil
            if not shutil.which(cf_cmd):
                print("[!] Cloudflared not found. Please install it first.")
                return None
            
            # Start cloudflared
            def run_cloudflared():
                process = subprocess.Popen(
                    [cf_cmd, "tunnel", "--url", f"http://localhost:{port}"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True
                )
                
                # Try to extract URL
                for line in process.stderr:
                    if "trycloudflare.com" in line:
                        import re
                        url_match = re.search(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com', line)
                        if url_match:
                            self.tunnels['cloudflared'] = url_match.group()
                            break
            
            thread = threading.Thread(target=run_cloudflared)
            thread.daemon = True
            thread.start()
            
            time.sleep(5)
            
            # Wait for URL
            timeout = 30
            while timeout > 0 and 'cloudflared' not in self.tunnels:
                time.sleep(1)
                timeout -= 1
            
            return self.tunnels.get('cloudflared')
            
        except Exception as e:
            print(f"[!] Cloudflared error: {e}")
            return None
    
    def start_ssh_local(self, port):
        """Start SSH Localhost.run tunnel"""
        try:
            if self.system == "Windows":
                print("[!] SSH Localhost.run on Windows requires SSH client")
                ssh_cmd = f"ssh -R 80:localhost:{port} ssh.localhost.run"
            else:
                ssh_cmd = f"ssh -o StrictHostKeyChecking=no -R 80:localhost:{port} ssh.localhost.run"
            
            def run_ssh_local():
                process = subprocess.Popen(
                    ssh_cmd.split(),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True
                )
                
                for line in process.stdout:
                    if "https://" in line:
                        import re
                        url_match = re.search(r'https://[a-zA-Z0-9.-]+', line)
                        if url_match:
                            self.tunnels['sshlocal'] = url_match.group()
                            break
            
            thread = threading.Thread(target=run_ssh_local)
            thread.daemon = True
            thread.start()
            
            time.sleep(5)
            
            timeout = 30
            while timeout > 0 and 'sshlocal' not in self.tunnels:
                time.sleep(1)
                timeout -= 1
            
            return self.tunnels.get('sshlocal')
            
        except Exception as e:
            print(f"[!] SSH Localhost.run error: {e}")
            return None
