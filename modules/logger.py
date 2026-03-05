#!/usr/bin/env python3
"""
Logger Module for T-WISHER
Handles all logging operations
"""

import os
import logging
from datetime import datetime

class Logger:
    def __init__(self, log_dir='logs'):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        
        # Setup main log file
        log_file = os.path.join(log_dir, 't-wisher.log')
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger('T-WISHER')
    
    def log_event(self, message):
        """Log an event"""
        self.logger.info(message)
    
    def log_error(self, message):
        """Log an error"""
        self.logger.error(message)
    
    def log_warning(self, message):
        """Log a warning"""
        self.logger.warning(message)
    
    def log_victim(self, victim_id, data):
        """Log victim specific data"""
        victim_file = os.path.join(self.log_dir, f'victim_{victim_id}.log')
        with open(victim_file, 'a') as f:
            f.write(f"[{datetime.now()}] {data}\n")
