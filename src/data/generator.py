"""
Sample Crime Data Generator
"""

import json
import os
import time
import threading

class DataGenerator:
    def create_streaming_data(self):
        """Create sample streaming crime data"""
        print("📥 Generating sample crime data...")
        
        os.makedirs("./data/streaming", exist_ok=True)
        
        # Initial batch
        crimes_batch1 = [
            {"case_number": "JJ432740", "primary_type": "BATTERY", "district": "017", "arrest": True, "hour": 23},
            {"case_number": "JJ435616", "primary_type": "THEFT", "district": "019", "arrest": False, "hour": 22},
            {"case_number": "JJ432603", "primary_type": "ASSAULT", "district": "011", "arrest": False, "hour": 21}
        ]
        
        self._write_batch(crimes_batch1, "batch_1.json")
        
        # Schedule second batch
        threading.Thread(target=self._delayed_batch).start()
        
        print("✅ Sample data ready")
    
    def _write_batch(self, crimes, filename):
        """Write crime batch to file"""
        with open(f"./data/streaming/{filename}", "w") as f:
            for crime in crimes:
                f.write(json.dumps(crime) + "\n")
    
    def _delayed_batch(self):
        """Add second batch after delay"""
        time.sleep(10)
        
        crimes_batch2 = [
            {"case_number": "JJ432741", "primary_type": "BATTERY", "district": "017", "arrest": False, "hour": 20},
            {"case_number": "JJ435617", "primary_type": "MOTOR VEHICLE THEFT", "district": "019", "arrest": True, "hour": 19},
            {"case_number": "JJ432604", "primary_type": "THEFT", "district": "011", "arrest": False, "hour": 18}
        ]
        
        self._write_batch(crimes_batch2, "batch_2.json")
        print("📥 Added new crime batch...")
