import streamlit as st
import time


i = 50

place = st.sidebar.container()

with place.empty():
    while True :
        for seconds in range(5):
            st.write(f"⏳ {seconds} seconds have passed")
            st.write(i)
            i=20
            time.sleep(5)
        