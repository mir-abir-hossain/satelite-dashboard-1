import streamlit as st
import folium
from streamlit_folium import st_folium  # For integrating Folium maps in Streamlit

# Function to create a map with the selected latitude and longitude
def create_map(lat, lon, zoom=12, layer="Satellite"):
    # Create a folium map centered on the given latitude and longitude
    m = folium.Map(location=[lat, lon], zoom_start=zoom, tiles=None)
    
    # Add different map layers
    folium.TileLayer(
        tiles="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        attr="OpenStreetMap contributors",
        name="OpenStreetMap",
    ).add_to(m)
    
    folium.TileLayer(
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attr="ESRI World Imagery",
        name="Satellite",
    ).add_to(m)
    
    # Add layer control to toggle between layers
    folium.LayerControl().add_to(m)
    
    return m

# Initialize session state to store the map
if "map" not in st.session_state:
    st.session_state.map = None

if "snapshots" not in st.session_state:
    st.session_state.snapshots = []

# Streamlit interface
st.title("Satellite Image Dashboard")

# Inputs for latitude, longitude, and zoom level
lat = st.number_input("Enter Latitude", value=23.8103, format="%.6f")  # Default: Dhaka
lon = st.number_input("Enter Longitude", value=90.4125, format="%.6f")
zoom = st.slider("Select Zoom Level", min_value=1, max_value=20, value=12)
layer = st.radio("Choose Map Layer", options=["OpenStreetMap", "Satellite"])

# When the button is clicked, generate and store the map in session state
if st.button("Show Map"):
    st.session_state.map = create_map(lat, lon, zoom, layer)

# Display the map if it's stored in session state
if st.session_state.map:
    st.write("### Map Preview")
    st_folium(st.session_state.map, width=700, height=500)

st.write("Enter coordinates to explore satellite images or map layers!")
