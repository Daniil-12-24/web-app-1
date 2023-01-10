import streamlit as st
from PIL import Image

with st.expander('Start Camera'):
    # star the camera
    camera_image = st.camera_input('Camera')

# preventing the error on the page
if camera_image:
    # create pillow image
    img = Image.open(camera_image)

    # convert the pillow image to grayscale
    gray_img = img.convert('L')

    # render the grayscale image on web-page
    st.image(gray_img)