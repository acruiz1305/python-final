import streamlit as st
import pandas as pd
import pydeck as pdk

#[MAP] a detailed map with colored dots and have text that hovers over

st.title('Location')

df = pd.read_csv("T2000.csv")

#[DA1] cleaning the data with missing coordinates long and lat
df = df.dropna(subset=["Latitude_final", "Longitude_final"])

df["Latitude_final"] = pd.to_numeric(df["Latitude_final"])
df["Longitude_final"] = pd.to_numeric(df["Longitude_final"])

#[ST1] streamlit slider for zoom level
zoom = st.slider("Zoom level", 1, 10, 6)

view_state = pdk.ViewState(
    latitude=42.3601,
    longitude=-71.0589,
    zoom=zoom,
    pitch=0,
)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[Longitude_final, Latitude_final]',
    get_color='[255, 112, 150]',
    get_radius=10000,
    pickable=True,
)

tooltip = {
    "html": "<b>Company:</b> {Company} <br/>"
            "<b>Sales:</b> ${Sales ($billion)}B <br/>"
            "<b>Profits:</b> ${Profits ($billion)}B",
    "style": {
        "backgroundColor": "rgb(255, 0, 110)",
        "color": "rgb(158, 240, 26)"
    }
}

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip
)

st.pydeck_chart(deck)