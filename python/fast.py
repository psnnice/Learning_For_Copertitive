import streamlit as st
import pandas as pd
import numpy as np
import requests
import streamlit as st
import datetime

# ตัวแปรทีใช้ใน toggle at side bar
show_chart = 1
show_DataFrame = 1
# เรียก API จาก FastAPI
# fastapi_base_url = "http://192.168.43.28:8000"
# response = requests.get("http://192.168.43.28:8000/water_level")
# data = response.json()
data = {
    "address": ["Phayao" ,"Phayao" ,"Phayao" ,"Ubon"  ,"Ubon" ,"Ubon" ,"Ubon" ,"Bangkok" ,"Bangkok" ,"Bangkok" ],
    "water_level": [20.5 ,22.0 ,10.5 ,17.0 ,28.5 ,10.5 ,27.0 ,15.5 ,12.0 ,10.7 ],
    "timestamp": ["2023-11-20T21:00:00","2023-11-20T20:00:00","2023-11-20T20:00:00","2023-11-20T20:00:00"
                  ,"2023-11-20T21:00:00","2023-11-20T20:00:00","2023-11-20T20:00:00","2023-11-20T21:00:00"
                  ,"2023-11-20T20:00:00","2023-11-20T20:00:00"]
}
df = pd.DataFrame(data)

# ใน sidebar
with st.sidebar:
    st.header("Country")
    option_c = st.selectbox("Select country", ["Bangkok","Phayao", "Ubon"])
    st.header('Select date')
    # filter date
    selected_date = st.text_input("Enter timestamp (format: YYYY-MM-DD):", "2023-11-20")
    filtered_date = df["timestamp"].str.startswith(selected_date)
    # กำหนดปุ่ม toggle ให้ show ค่าหรือไม่
    st.header('Hide data')
    on = st.toggle('Data frame water level')
    on1 = st.toggle('Data Chart')
    if on:
        show_DataFrame = 0
    if on1:
        show_chart = 0

#######################################################################
def main():
    # ใช้ HTML เพื่อจัดตำแหน่งข้อความ
    st.markdown(f"<h1 style='text-align: center;'>Water level At {option_c}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Date {selected_date}</p>", unsafe_allow_html=True)
    # ส่วนอื่น ๆ ของโปรแกรม

if __name__ == "__main__":
    main()
        
# ชื่อ title  
# filter address
    latest_data = df.groupby('address').apply(lambda group: group[group['timestamp'] == group['timestamp'].max()])
    # แสดง DataFrame ตัวล่าสุด
    # กำหนดค่าของข้อมูลตัวล่าสุดในตัวแปร
    latest_data_Ubon = latest_data[latest_data['address'].str.contains("Ubon")]
    latest_data_Phayao = latest_data[latest_data['address'].str.contains("Phayao")]
    latest_data_Bangkok = latest_data[latest_data['address'].str.contains("Bangkok")]

    # ในทำนองเดียวกัน, คุณสามารถกำหนดค่าของแต่ละประเภทในตัวแปรที่คุณต้องการ
    # ยกตัวอย่างเช่น:
    # latest_data_TypeX = latest_data[latest_data['address'].str.contains("TypeX")]
    # ในที่นี้คือตัวอย่างที่กำหนดค่าของ Ubon, Phayao, และ Bangkok ในตัวแปร
    latest_data_Ubon_values = latest_data_Ubon['water_level'].values[0]
    latest_data_Phayao_values = latest_data_Phayao['water_level'].values[0]
    latest_data_Bangkok_values = latest_data_Bangkok['water_level'].values[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("M.182 อ.กันทรารมย์ อุบล", latest_data_Ubon_values, "1.2 m")
    col2.metric("M.7 อ.เมืองอุบล พะเยา", latest_data_Phayao_values, "-0.8 m ")
    col3.metric("E.98 อ.เขื่องใน กรุง", latest_data_Bangkok_values, "0.4 m ") 



if option_c == "Ubon" :
    filtered_df = df["address"].str.contains("Ubon")

elif option_c == "Phayao" :
    filtered_df = df["address"].str.contains("Phayao")

elif option_c == "Bangkok" :
    filtered_df = df["address"].str.contains("Bangkok")
    
 # ผูกเงื่อนไข  
fill = df[filtered_date & filtered_df]  
fill = fill.reset_index(drop=True)
fill_sorted_by_timestamp = fill.sort_values('timestamp')

# แสดงข้อมูลใน Streamlit
if show_DataFrame == 1:
    st.table(fill_sorted_by_timestamp.T)

if show_chart == 1:
    st.area_chart(fill_sorted_by_timestamp["water_level"])

