import streamlit as st

st.set_page_config(page_title="Health Coach", page_icon=":heart:", layout="wide" )

with st.container():
    st.title ("HealaaathCoach :heart: :running:")
    st.subheader("hey")

st.sidebar.success("select a page above")

from arcgis.gis import GIS
# Create a GIS object, as an anonymous user for this example
gis = GIS()

map1 = gis.map('Paris') # Passing a place name to the constructor
                        # will initialize the extent of the map.
map1
