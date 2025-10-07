"""
Pipeline Configuration
"""

SPARK_CONFIG = {
    "app_name": "ChicagoCrimePipeline",
    "trigger_interval": "5 seconds",
    "max_files_per_trigger": 1
}

DATA_CONFIG = {
    "streaming_path": "./data/streaming/",
    "output_path": "./output/",
    "checkpoint_path": "./checkpoint/"
}
