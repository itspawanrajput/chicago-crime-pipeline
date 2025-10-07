#!/usr/bin/env python3
"""
Chicago Crime Data Pipeline - Main Runner
"""

from streaming.pipeline import CrimePipeline
from data.generator import DataGenerator

def main():
    print("🚀 Starting Chicago Crime Data Pipeline")
    
    # Generate sample data
    generator = DataGenerator()
    generator.create_streaming_data()
    
    # Run pipeline
    pipeline = CrimePipeline()
    pipeline.run()

if __name__ == "__main__":
    main()
