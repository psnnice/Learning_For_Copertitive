# ##################################################################################
# # slider ให้เลือกค่าเวลาที่ต้องการดูข้อมูล
# string_options = [  "00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00",
#                     "08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00",
#                     "16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00" ]

# # แปลงเป็น NumPy array
# all_options = np.array(string_options)

# # st.select_slider() ในส่วนหลัก
# selected_range = st.select_slider("Select a range with select slider", options=all_options, value=(all_options[0], all_options[-1]))
# st.write(f"You selected with select slider: {selected_range}")

# # แสดงค่าที่เลือก
# st.write("Values selected:")
# for option in all_options[all_options.tolist().index(selected_range[0]): all_options.tolist().index(selected_range[1]) + 1]:
#     st.write(option)

# # นำค่าที่เก็บไว้มาใช้
# selected_values = all_options[all_options.tolist().index(selected_range[0]): all_options.tolist().index(selected_range[1]) + 1]
# st.write("Using values from main content:")
# st.write(f"Selected range: {selected_values}")

# ##################################################################################