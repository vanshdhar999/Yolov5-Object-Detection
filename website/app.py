import streamlit as st
import cv2 as cv
import os
import sys

from process.model import run
x  = run()
# Add the parent directory of 'yolov5' to the Python path
# yolov5_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'yolov5'))
# if yolov5_parent_dir not in sys.path:
#     sys.path.append(yolov5_parent_dir)
# else:
#     print(f"Directory {yolov5_parent_dir} already in sys.path")

# # Now you can import the 'run' function from 'model.py'
# try:
#     from yolov5.model import run
# except ImportError as e:
#     print(f"Failed to import 'run' function from 'model.py': {e}")


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
        x('yolov5s.pt', file)

if choice == 'Download':
    pass