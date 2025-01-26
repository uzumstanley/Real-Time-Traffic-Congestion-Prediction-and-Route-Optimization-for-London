# data_processing.py
import pandas as pd
from pyproj import Transformer

# Load data
df = pd.read_csv('Bus_Shelters.csv')

# Convert OSGB36 (EPSG:27700) to WGS84 (EPSG:4326)
transformer = Transformer.from_crs('EPSG:27700', 'EPSG:4326')
df['LONGITUDE'], df['LATITUDE'] = transformer.transform(df['OS_EASTING'], df['OS_NORTHING'])

# Clean data: Drop rows with missing critical fields
df = df.dropna(subset=['LATITUDE', 'LONGITUDE', 'LAST_CLEANED'])
df['LAST_CLEANED'] = pd.to_datetime(df['LAST_CLEANED'], errors='coerce')
df = df.dropna(subset=['LAST_CLEANED'])

# Save to SQLite
import sqlite3
conn = sqlite3.connect('shelters.db')
df.to_sql('shelters', conn, if_exists='replace', index=False)
conn.close()