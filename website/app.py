import streamlit as st
import cv2 as cv
import os
with st.sidebar:
    st.image("./icon.png")
    st.title('Traffic Image Processor')
    choice = st.radio("Navigation", ["Process", "Download"])
    st.info(" This web application helps you process traffic related images and gives the inference such as number of vehicles and types of vehicles")

# Structure 
    
if os.path.exists('../images/test.jpg'):
    print("Image found")
    
if choice == 'Process':
    st.title('Upload and Process your Image')
    st.title('Upload Image')
    file = st.file_uploader("Upload a valid .jpeg .jpg .png image")
    if file:
        st.image(file)
        with open("../images/test.jpg", "wb") as f:
            f.write(file.getbuffer())
    if st.button('Run Model'):
        pass
    

if choice == 'Download':
    pass