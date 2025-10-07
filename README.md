# Chicago Crime Data Pipeline

Real-time crime analytics using Apache Spark Streaming and public Chicago crime data.

## Features

- 🔥 **Real-time Streaming**: Process crime data as it arrives
- 📊 **Live Analytics**: Crime patterns, risk assessment, arrest rates
- 🚀 **Spark Powered**: Scalable distributed processing
- 🎯 **Risk Scoring**: Automatic HIGH/MEDIUM/LOW risk classification
- 📈 **District Analysis**: Performance metrics by police district

## Quick Start

```bash
# Setup environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run pipeline
python src/main.py
```

## Architecture

```
src/
├── main.py              # Main pipeline runner
├── streaming/
│   ├── pipeline.py      # Core streaming logic
│   └── analytics.py     # Crime analytics engine
├── data/
│   └── generator.py     # Sample data generator
└── config/
    └── settings.py      # Configuration
```

## Sample Output

```
📊 Real-time Crime Analytics:
+------------+--------+-----------+----------+
|primary_type|district|crime_count|risk_level|
+------------+--------+-----------+----------+
|BATTERY     |017     |3          |🔴 HIGH   |
|THEFT       |019     |2          |🟡 MEDIUM |
+------------+--------+-----------+----------+
```

## Requirements

- Python 3.8+
- Apache Spark 4.0+
- Java 17+
