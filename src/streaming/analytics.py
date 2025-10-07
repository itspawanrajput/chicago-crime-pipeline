"""
Crime Analytics Engine
"""

from pyspark.sql.functions import *

class CrimeAnalytics:
    def process(self, df):
        """Process streaming crime data"""
        return df \
            .groupBy("primary_type", "district") \
            .agg(
                count("*").alias("crime_count"),
                avg("hour").alias("avg_hour"),
                sum(when(col("arrest") == True, 1).otherwise(0)).alias("arrests")
            ) \
            .withColumn("arrest_rate", round(col("arrests") / col("crime_count"), 2)) \
            .withColumn("risk_level", 
                when(col("crime_count") >= 2, "🔴 HIGH")
                .when(col("crime_count") == 1, "🟡 MEDIUM")
                .otherwise("🟢 LOW")) \
            .orderBy(desc("crime_count"))
