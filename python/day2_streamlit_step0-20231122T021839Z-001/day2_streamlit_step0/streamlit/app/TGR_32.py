from collections import namedtuple
import altair as alt
import streamlit.components.v1 as components
import folium
import streamlit as st
import pandas as pd
import numpy as np
import requests
import pymongo
import time
from pymongo import MongoClient
import asyncio
import paho.mqtt.subscribe as publish

st.set_page_config(
    page_title="Water Level Reporter",  # กำหนดชื่อของหน้าแอป
    page_icon="🌫️",  # กำหนดไอคอนของหน้าแอป
    layout="wide",  # กำหนด Layout ให้กับหน้าแอป
    initial_sidebar_state="collapsed",  # กำหนดสถานะเริ่มต้นของ sidebar
)


# fastapi_base_url = "http://localhost:80"
# response = requests.get("http://localhost:80/")
# item = response.json()

MONGO_DETAILS = "mongodb://tesarally:contestor@mongoDB:27017"
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(MONGO_DETAILS)

client = init_connection()

def get_data():
    db = client.local
    items = db.water_data.find()
    items = list(items)
    return items

items = get_data()
df = pd.DataFrame(items)

@st.cache
def connect_to_database(MONGO_DETAILS):
    return MongoClient(MONGO_DETAILS)
# ตัวแปรทีใช้ใน toggle at side bar
# ใน sidebar

M_DAYS = [0, 32, 29, 32, 31, 32, 31, 32, 32, 31, 32, 31, 32]
day=[]
mon=[]*11    
with st.sidebar :
    st.header("Select Month & Day")
    month = st.selectbox("Select month", [1,2,3,4,5,6,7,8,9,10,11,12])
    for date in range(1,M_DAYS[month],1):
        da = day.append(date)
    if date == M_DAYS[month]:
        month += 1
    show = st.toggle('Select day')
    if show:
        day_select = st.selectbox("Select day", day)
        filtered_df = df[(df['month'] == month) & (df['date'] == day_select)]
        if day_select == 1:
            ls = 'st'
        elif day_select == 2:
            ls = 'nd'
        elif day_select == 3:
            ls = 'rd'
        else:
            ls = 'th'
        
    else:
        filtered_df = df[(df['month'] == month)]
# ใน main page
st.markdown(f"<h1 style='text-align: center;'>Water level At Huana</h1>", unsafe_allow_html=True)

if show:
    st.markdown(f"<p style='text-align: center;'> Days: {day_select} {ls} &nbsp;Month: {month}</p>", unsafe_allow_html=True)            
else:
    st.markdown(f"<p style='text-align: center;'> Mounth: {month}</p>", unsafe_allow_html=True)


selected_columns = ['date', 'month', 'water_level','water_flow_rate']
fill_call = filtered_df[selected_columns]
char_fr_ba = ['date','water_level','water_flow_rate']
tab1, tab2, = st.tabs(["Data" ,"Map information"])

def chart ():
            fill_ch = filtered_df[char_fr_ba]
            st.line_chart(fill_ch.set_index('date'))

def gen ():
    sp1,sp2,sp3,sp4,sp5,sp6,sp7,sp8,sp9,sp10 = st.columns(10)
    with sp9:generate = st.button("Generate Chart","primary")
    with sp10:gennerate_on = st.toggle('Show All time')
    if generate :
        progress_text = "Generating . .  .  ."
        my_bar = st.progress(20, text=progress_text)
        for percent_complete in range(100):
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(0.3)
        my_bar.empty()
        chart()
    elif gennerate_on:
        chart()

with tab1:
    st.header("Water Level")
    st.table(fill_call.astype(str).reset_index(drop=True).T)
    mqtt_broker = "mqtt.eclipse.org"
    mqtt_port = 1883
    mqtt_topic = "your/topic"

# Streamlit app

# Input field for the message
    message = st.text_input("Enter Message:", "Hello, MQTT!")

# Button to publish the message
    if st.button("Publish Message"):
        try:
            # Publish the message to the MQTT broker
            publish.single(mqtt_topic, message, hostname=mqtt_broker, port=mqtt_port)

            # Display success message
        except Exception as e:
            # Display failure message
            st.error(f"Error: {e}")
            
    if show:
        st.warning("Cant Generate Chart")
    else:
        gen()
   

with tab2:
    map1st = pd.DataFrame({
        'lat': [15.22642079914576,15.225868431822311,15.227406],  # replace with your latitudes
        'lon': [104.87186971658166,104.8704481517055,104.869970],  # replace with your longitudes
    })

    # Create a Folium map object
    m = folium.Map(location=[15.22642079914576, 104.87186971658166], zoom_start=13)

    # Add custom markers to the map
    c1,c2,c3 = st.columns(3)
    with c1:
        for idx, row in map1st.iterrows():
            folium.Marker([row['lat'], row['lon']], popup='<i>พื้นที่น้ำท่วมไวที่สุด</i>', icon=folium.Icon(color='red')).add_to(m)

        # Convert the Folium map to HTML
        html = m._repr_html_()

        # Display the HTML in Streamlit
        components.html(html, width=1000, height=1000)
    with c3:
        st.header("ระดับน้ำที่ 112.5 เมตร")
        st.warning("พื้นที่ที่เสี่ยงอันตรายที่สุด")

