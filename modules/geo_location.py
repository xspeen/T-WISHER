#!/usr/bin/env python3
"""
Geolocation Module for T-WISHER
Handles location data processing
"""

import json
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

class GeoLocation:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="t-wisher")
    
    def reverse_geocode(self, latitude, longitude):
        """Convert coordinates to address"""
        try:
            location = self.geolocator.reverse(f"{latitude}, {longitude}")
            return location.address if location else "Unknown"
        except GeocoderTimedOut:
            return "Geocoding timeout"
        except Exception as e:
            return f"Error: {e}"
    
    def get_city_country(self, latitude, longitude):
        """Extract city and country from coordinates"""
        try:
            location = self.geolocator.reverse(f"{latitude}, {longitude}")
            if location:
                address = location.raw.get('address', {})
                city = address.get('city') or address.get('town') or address.get('village')
                country = address.get('country')
                return city, country
            return None, None
        except:
            return None, None
    
    def generate_maps_link(self, latitude, longitude):
        """Generate Google Maps link"""
        return f"https://www.google.com/maps?q={latitude},{longitude}"
    
    def format_location(self, data):
        """Format location data for display"""
        lat = data.get('latitude', 'Unknown')
        lon = data.get('longitude', 'Unknown')
        acc = data.get('accuracy', 'Unknown')
        
        return {
            'coordinates': f"{lat}, {lon}",
            'accuracy': f"{acc} meters",
            'maps_link': self.generate_maps_link(lat, lon),
            'timestamp': data.get('timestamp', 'Unknown')
        }
