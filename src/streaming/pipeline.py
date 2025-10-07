"""
Core Streaming Pipeline
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from .analytics import CrimeAnalytics
from config.settings import SPARK_CONFIG

class CrimePipeline:
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName(SPARK_CONFIG["app_name"]) \
            .config("spark.sql.adaptive.enabled", "true") \
            .getOrCreate()
        
        self.analytics = CrimeAnalytics()
    
    def get_schema(self):
        return StructType([
            StructField("case_number", StringType(), True),
            StructField("primary_type", StringType(), True),
            StructField("district", StringType(), True),
            StructField("arrest", BooleanType(), True),
            StructField("hour", IntegerType(), True)
        ])
    
    def run(self):
        print("📊 Starting streaming pipeline...")
        
        # Create streaming DataFrame
        streaming_df = self.spark.readStream \
            .format("json") \
            .schema(self.get_schema()) \
            .option("maxFilesPerTrigger", 1) \
            .load("./data/streaming/")
        
        # Process analytics
        analytics_df = self.analytics.process(streaming_df)
        
        # Start streaming
        query = analytics_df.writeStream \
            .outputMode("update") \
            .format("console") \
            .option("truncate", False) \
            .trigger(processingTime='5 seconds') \
            .start()
        
        print("🔥 Pipeline running - Press Ctrl+C to stop")
        query.awaitTermination(30)
        
        print("✅ Pipeline completed")
        self.spark.stop()
