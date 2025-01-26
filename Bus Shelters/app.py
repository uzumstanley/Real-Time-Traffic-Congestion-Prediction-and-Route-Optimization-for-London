# app.py
from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
import folium
from pyproj import Transformer

app = Flask(__name__)

def create_map():
    # Load data and convert coordinates
    conn = sqlite3.connect('shelters.db')
    df = pd.read_sql_query("SELECT * FROM shelters", conn)
    conn.close()
    
    # Create base map
    m = folium.Map(location=[51.5074, -0.1278], zoom_start=12)
    
    # Add clusters and heatmap
    from folium.plugins import MarkerCluster, HeatMap
    marker_cluster = MarkerCluster().add_to(m)
    
    heat_data = [[row['LATITUDE'], row['LONGITUDE']] for _, row in df.iterrows()]
    HeatMap(heat_data, radius=15).add_to(m)
    
    # Add interactive markers
    for _, row in df.iterrows():
        popup = folium.Popup(f"""
            <b>{row['ROAD_NAME']}</b><br>
            Status: {row['STATUS']}<br>
            Last Cleaned: {row['LAST_CLEANED']}<br>
            <button onclick="reportIssue('{row['SHELTER_CODE']}')">Report Issue</button>
        """)
        folium.Marker(
            [row['LATITUDE'], row['LONGITUDE']],
            popup=popup,
            icon=folium.Icon(color='green' if row['STATUS'] == 'A' else 'red')
        ).add_to(marker_cluster)
    
    return m._repr_html_()

@app.route('/')
def index():
    map_html = create_map()
    return render_template('index.html', map_html=map_html)

@app.route('/report', methods=['POST'])
def report_issue():
    data = request.json
    # Store reports in SQLite (add your logic here)
    return jsonify({"status": "Report received!"})

if __name__ == '__main__':
    app.run(debug=True)