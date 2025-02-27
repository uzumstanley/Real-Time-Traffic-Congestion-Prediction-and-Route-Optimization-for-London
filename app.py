import pandas as pd
import streamlit as st
import plotly.express as px

# Load dataset
@st.cache
def load_data():
    # Corrected file path for downloading as CSV
    file_path = 'https://raw.githubusercontent.com/uzumstanley/Real-Time-Traffic-Congestion-Prediction-and-Route-Optimization-for-London/refs/heads/main/Strategic%20Monitoring%20Areas/Strategic_Monitoring_Areas.csv'
    return pd.read_csv(file_path)

# Load data
data = load_data()

# Remove duplicates
data = data.drop_duplicates()

# Sidebar filters
st.sidebar.title("Filter Options")
selected_zones = st.sidebar.multiselect("Select ZONE(s):", options=data['ZONE'].unique(), default=data['ZONE'].unique())

# Apply filters
filtered_data = data[data['ZONE'].isin(selected_zones)]

# Dashboard Header
st.title("Strategic Monitoring Areas Dashboard")
st.markdown("""
Explore the Strategic Monitoring Areas data interactively. Use filters in the sidebar to customize your view.
""")

# Summary Statistics
st.subheader("Summary Statistics by Zone and Value")
summary_stats = filtered_data.groupby('ZONE')['VALUE'].describe()
st.write(summary_stats)

# Visualization: Bar Chart
st.subheader("Zone Counts")
zone_counts = filtered_data['ZONE'].value_counts().reset_index()
zone_counts.columns = ['ZONE', 'Count']
fig_bar = px.bar(zone_counts, x='ZONE', y='Count', color='ZONE', title="Count of Monitoring Areas by Zone")
st.plotly_chart(fig_bar)

# Visualization: Pie Chart
st.subheader("Area Distribution by Zone")
area_distribution = filtered_data.groupby('ZONE')['VALUE'].sum().reset_index()
fig_pie = px.pie(area_distribution, values='VALUE', names='ZONE', title="Area Distribution by Zone")
st.plotly_chart(fig_pie)

# Data Table
st.subheader("Filtered Dataset")
st.write(filtered_data)
