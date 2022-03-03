import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

DATE_TIME = "Year"

@st.experimental_memo
def load_data(nrows):
    data = pd.read_csv("JerseyCollege.csv", nrows=nrows)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME]) 
    return data

data = load_data(192)


def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "ColumnLayer",
                data=data,
                get_position= ["Longitude", "Latitude"],
                get_elevation = "Enrollment",
                elevationScale = 1,
                getFillColor = [235, "52 + (230-52) * 30000/ Enrollment", 52, 255],
                radius=4000,
                pickable=True,
                extruded=True,
            ),
        ]
    ))

st.title("Student Enrollment at Popular New Jersey Universities, 1996 - 2019")
st.markdown("**You can look at data from Rutgers-New Brunswick, Rutgers-Camden, Rutgers-Newark, TCNJ, Stockton University, Montclair State University, and Rowan University**")
year_selected = st.slider("Use the slider to select a specific year to analyze.", 1996, 2019)
data = data[data[DATE_TIME].dt.year == year_selected]

map(data, 40.3573, -74.6672, 6)




