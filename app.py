import streamlit as st
import os
import sys
# Add the project root directory to the Python path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)

import process.model as model

with st.sidebar:
    st.image("./icon.png")
    st.title('Traffic Image Processor')
    choice = st.radio("Navigation", ["Home", "Download"])
    st.info(" This web application helps you process traffic related images and gives the inference such as number of vehicles and types of vehicles")

# Structure 
if os.path.exists('./images/test.jpg'):
    print("Image found")
    
if choice == 'Home':
    model_run = False
    st.title('Upload Image and Run Model')
    file = st.file_uploader(type= ['jpg', 'jpeg', 'png'], label='Upload Image')
    if file:
        st.image(file, width=500, use_column_width=True)
        with open("./images/test.jpg", "wb") as f:
            f.write(file.getbuffer())
    if st.button('Run Model'):
        if os.path.exists('./images/test.jpg'):
            with st.spinner('Processing...'):
                model_run = True 
                results = model.run()
                os.remove('./images/test.jpg')
        else:
            st.error('No image uploaded')
    st.title('Results')
    if model_run:
        st.image('./process/runs/detect/exp/test.jpg', width=500, use_column_width=True)
        with st.container(height=300, border=True):
            parts = results.split()
            st.write(f"Image size: {parts[3]}")
            parts = parts[4:]
            for i in range (0, len(parts), 2):
                st.write(f"{parts[i]} {parts[i+1]} Detected")
    else:
        AssertionError('Model not run')

downloaded = False
if choice == 'Download':
    st.title('Download Image')
    if os.path.exists('./process/runs/detect/exp/test.jpg'):
        st.image('./process/runs/detect/exp/test.jpg', width=500, use_column_width=True)
        st.download_button(
        label="Download Image",
        data='./process/runs/detect/exp/test.jpg',
        file_name='result.jpeg')
        downloaded = True
    else:
        st.error('No results to download')
if downloaded:
    os.remove('./process/runs/detect/exp/test.jpg')