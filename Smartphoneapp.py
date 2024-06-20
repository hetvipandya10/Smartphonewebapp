import streamlit as st

st.title("Welcome to Smartphone App")

brand_name=st.slider("Select Brand_name=",0,20)
price=st.slider("Select price=",6699,23999)
rating=st.slider("Select rating=",60,89)
has_5g=st.slider("Select has_5g=",0,1)
has_nfc=st.slider("Select has_nfc=",0,1)
has_ir_blaster=st.slider("Select has_ir_blaster=",0,1)
num_cores=st.slider("Select num_cores=",4,8)
processor_speed=st.slider("Select processor_speed=",1.6,3.2)
battery_capacity=st.slider("Select battery_capacity=",3100,22000)
fast_charging_available=st.slider("Select fast_charging_available=",0,1)
fast_charging=st.slider("Select fast_charging=",10,210)               
ram_capacity=st.slider("Select ram_capacity=",2,12)                
internal_memory=st.slider("Select internal_memory=",32,512)             
screen_size=st.slider("Select screen_size=",5.9,6.95)                 
refresh_rate=st.slider("Select refresh_rate=",60,144)                   
num_rear_cameras=st.slider("Select num_rear_cameras=",1,4)               
num_front_cameras=st.slider("Select num_front_cameras=",1,2)           
primary_camera_rear=st.slider("Select primary_camera_rear=",8,200)         
primary_camera_front=st.slider("Select primary_camera_front=",5,60)        
extended_memory_available=st.slider("Select extended_memory_available=",0,1)
extended_upto=st.slider("Select extended_upto=",128,2048)              
resolution_width=st.slider("Select resolution_width=",720,2408)               
resolution_height=st.slider("Select resolution_height=",720,3200)

import pickle
model=pickle.load(open("Smartphone.pkl","rb"))
if st.button("Predict"):
    prd=model.predict([[brand_name,price,rating,has_5g,has_nfc,has_ir_blaster,num_cores,processor_speed,battery_capacity,fast_charging_available,fast_charging,ram_capacity,internal_memory,screen_size,refresh_rate,num_rear_cameras,num_front_cameras,primary_camera_rear,primary_camera_front,extended_memory_available,extended_upto,resolution_width,resolution_height]])           
    st.success("The Smartphone is "+ prd[0])