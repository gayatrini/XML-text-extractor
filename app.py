import os
import xml.etree.ElementTree as ET
import re
import string
import unicodedata
from bs4 import BeautifulSoup
import streamlit as st

# Change to your working directory (ensure this path is correct)
os.chdir(r"C:\Users\shree\Desktop\FSDS&AI\May Month\29th- webscrapping\XML Project")

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg with a blur effect.
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://www.neatshape.com/wp-content/uploads/revslider/technologies/Technologies-v4.jpg");
             background-size: cover;

         }}
         .stFileUploader label {{
             font-size: 20px; /* Adjust the font size as needed */
             color: white;  /* Optional: Change the text color */
             font-weight: bold;  /* Optional: Make the text bold */
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()

def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    return ET.tostring(root, encoding='utf8')

def strip_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub(r'\[[^]]*\]', '', text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text.strip()

# Creating the frontend for the application
st.title("XML Text Extractor")

# File uploader

uploaded_file = st.file_uploader("Upload XML file here for extraction:", type='xml')

# Adding space after the file uploader
st.write('<br>', unsafe_allow_html=True)

if uploaded_file is not None:
    raw_xml = parse_xml(uploaded_file)
    raw_text = raw_xml.decode('utf-8')
    denoised_text = denoise_text(raw_text)

    # Display the extracted and cleaned text
    st.subheader('Extracted Text')

    # Adding space before displaying the text area
    st.write('<br>', unsafe_allow_html=True)
    st.write('<br>', unsafe_allow_html=True)

    st.text_area("Text", denoised_text, height=500)
