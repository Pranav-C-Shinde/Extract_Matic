#pip install streamlit-option-menu
#pip install streamlit

# one single pip install
# pip install streamlit streamlit-option-menu pandas requests pytesseract opencv-python pillow ftfy


import streamlit as st
from streamlit_option_menu import option_menu
import time
import pandas as pd
import numpy as np
import requests
import io

import json
import pytesseract
import cv2
import sys
import re
import os
from PIL import Image
import ftfy

import pan_read           
import aadhaar_read



API_URL = "https://api-inference.huggingface.co/models/PCS/Extract-O-Matic"
headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}

def query(file_bytes):
    response = requests.post(API_URL, headers=headers, data=file_bytes)
    return response.json()

# Functions for each page
def home():
        st.markdown(
            """
            <style>
            .stApp {
            background-color: #2556DF;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100%25' height='100%25' viewBox='0 0 1200 800'%3E%3Cdefs%3E%3CradialGradient id='a' cx='0' cy='800' r='800' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' stop-color='%23d10086'/%3E%3Cstop offset='1' stop-color='%23d10086' stop-opacity='0'/%3E%3C/radialGradient%3E%3CradialGradient id='b' cx='1200' cy='800' r='800' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' stop-color='%23a84ebe'/%3E%3Cstop offset='1' stop-color='%23a84ebe' stop-opacity='0'/%3E%3C/radialGradient%3E%3CradialGradient id='c' cx='600' cy='0' r='600' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' stop-color='%23e4245d'/%3E%3Cstop offset='1' stop-color='%23e4245d' stop-opacity='0'/%3E%3C/radialGradient%3E%3CradialGradient id='d' cx='600' cy='800' r='600' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' stop-color='%232556DF'/%3E%3Cstop offset='1' stop-color='%232556DF' stop-opacity='0'/%3E%3C/radialGradient%3E%3CradialGradient id='e' cx='0' cy='0' r='800' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' stop-color='%23D40000'/%3E%3Cstop offset='1' stop-color='%23D40000' stop-opacity='0'/%3E%3C/radialGradient%3E%3CradialGradient id='f' cx='1200' cy='0' r='800' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' stop-color='%23D55A9D'/%3E%3Cstop offset='1' stop-color='%23D55A9D' stop-opacity='0'/%3E%3C/radialGradient%3E%3C/defs%3E%3Crect fill='url(%23a)' width='1200' height='800'/%3E%3Crect fill='url(%23b)' width='1200' height='800'/%3E%3Crect fill='url(%23c)' width='1200' height='800'/%3E%3Crect fill='url(%23d)' width='1200' height='800'/%3E%3Crect fill='url(%23e)' width='1200' height='800'/%3E%3Crect fill='url(%23f)' width='1200' height='800'/%3E%3C/svg%3E");
            background-attachment: fixed;
            background-size: cover;
            }
            </style>
            <h1 style='text-align: center;'>Extract-O-Matic</h1>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<p style='padding-top:80px'></p>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: left;'>Welcome to Extract-O-Matic</h1>",unsafe_allow_html=True)
        st.markdown("<p style='padding-top:5px'></p>", unsafe_allow_html=True)
        st.markdown(
            """
            <h6 style='text-align: left;'>
            In a digitally evolving landscape, the demand for efficient data extraction solutions has never been more pronounced. This project addresses the challenges associated with manual handling of diverse documents by developing an intelligent data extraction application. Focused on recognizing and extracting information from invoices, PDFs, and various textual images, the application offers a user-friendly interface for individuals and businesses. Leveraging Python technology, the system excels in document recognition, data extraction algorithms, and seamless integration with Excel for organized data storage.
            </h1>
            """
                    ,unsafe_allow_html=True)

def invoice():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0A0D33;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400' viewBox='0 0 800 800'%3E%3Cg fill='none' stroke='%231C3F44' stroke-width='1'%3E%3Cpath d='M769 229L1037 260.9M927 880L731 737 520 660 309 538 40 599 295 764 126.5 879.5 40 599-197 493 102 382-31 229 126.5 79.5-69-63'/%3E%3Cpath d='M-31 229L237 261 390 382 603 493 308.5 537.5 101.5 381.5M370 905L295 764'/%3E%3Cpath d='M520 660L578 842 731 737 840 599 603 493 520 660 295 764 309 538 390 382 539 269 769 229 577.5 41.5 370 105 295 -36 126.5 79.5 237 261 102 382 40 599 -69 737 127 880'/%3E%3Cpath d='M520-140L578.5 42.5 731-63M603 493L539 269 237 261 370 105M902 382L539 269M390 382L102 382'/%3E%3Cpath d='M-222 42L126.5 79.5 370 105 539 269 577.5 41.5 927 80 769 229 902 382 603 493 731 737M295-36L577.5 41.5M578 842L295 764M40-201L127 80M102 382L-261 269'/%3E%3C/g%3E%3Cg fill='%23553652'%3E%3Ccircle cx='769' cy='229' r='5'/%3E%3Ccircle cx='539' cy='269' r='5'/%3E%3Ccircle cx='603' cy='493' r='5'/%3E%3Ccircle cx='731' cy='737' r='5'/%3E%3Ccircle cx='520' cy='660' r='5'/%3E%3Ccircle cx='309' cy='538' r='5'/%3E%3Ccircle cx='295' cy='764' r='5'/%3E%3Ccircle cx='40' cy='599' r='5'/%3E%3Ccircle cx='102' cy='382' r='5'/%3E%3Ccircle cx='127' cy='80' r='5'/%3E%3Ccircle cx='370' cy='105' r='5'/%3E%3Ccircle cx='578' cy='42' r='5'/%3E%3Ccircle cx='237' cy='261' r='5'/%3E%3Ccircle cx='390' cy='382' r='5'/%3E%3C/g%3E%3C/svg%3E");
        }
        </style>
        <h1 style='text-align: center;'>Invoice Extraction</h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<p style='padding-top:100px'></p>", unsafe_allow_html=True)


    if 'show_level_1' not in st.session_state:
        st.session_state.show_level_1 = False
    if 'show_level_2' not in st.session_state:
        st.session_state.show_level_2 = False
    if 'show_level_3' not in st.session_state:
        st.session_state.show_level_3 = False
    if 'show_level_4' not in st.session_state:
        st.session_state.show_level_4 = False
    if 'show_level_5' not in st.session_state:
        st.session_state.show_level_5 = False
    if 'show_level_6' not in st.session_state:
        st.session_state.show_level_6 = False

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a file", key="upload_i_file", type=["png", "jpeg", "jpg", "docx"])

    if uploaded_file is not None:
        # Display file details
        st.write(f"Filename: {uploaded_file.name}")
        st.write(f"File type: {uploaded_file.type}")
        st.write(f"File size: {uploaded_file.size} bytes")

        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.session_state.show_level_1 = True


    if st.session_state.show_level_1:
        if st.button('Extract Invoice Data?'):
            st.session_state.show_level_2 = True
            st.session_state.show_level_5 = True
            st.session_state.show_level_3 = False
            st.session_state.show_level_4 = False
            st.session_state.show_level_6 = False

    cols = st.columns(2)
    # Add buttons to each column
    with cols[0]:
        if st.session_state.show_level_2:
            if st.button('Append Data in existing file'):
                st.session_state.show_level_3 = True
                st.session_state.show_level_6 = False
                st.session_state.show_level_5 = False

        if st.session_state.show_level_3:
            # File uploader widget with a unique key
            uploaded_file_append = st.file_uploader("Choose a file", key="append_i_file", type=["csv"])                

            if uploaded_file_append is not None:
                # Display file details
                st.write(f"Filename: {uploaded_file_append.name}")
                st.write(f"File type: {uploaded_file_append.type}")
                st.write(f"File size: {uploaded_file_append.size} bytes")

                existing_df = pd.read_csv(uploaded_file_append)
                st.session_state.show_level_4 = True

            ### -------------------------
                #Calling the API
                output = query(bytes_data)
                #st.write(output)

                # Extract the generated text
                generated_text = output[0]['generated_text']

                # Parse the generated text into a dictionary
                parsed_output = {}
                segments = generated_text.split('<s_')
                for segment in segments[1:]:  # Skip the first empty segment
                    key_value = segment.split('>', 1)
                    if len(key_value) == 2:
                        key = key_value[0].strip()
                        value = key_value[1].split('<')[0].strip()
                        parsed_output[key] = value

                # Print the dictionary
                #st.write(parsed_output)

                # Preparation for creating CSV file
                data = {
                    "Invoice No": [parsed_output.get('invoice_no', '')],
                    "Invoice Date": [parsed_output.get('invoice_date', '')],
                    "Seller": [parsed_output.get('seller', '')],
                    "Client": [parsed_output.get('client', '')],
                    "Seller Tax ID": [parsed_output.get('seller_tax_id', '')],
                    "Client Tax ID": [parsed_output.get('client_tax_id', '')],
                    "IBAN": [parsed_output.get('iban', '')],
                    "Item Description": [parsed_output.get('item_desc', '')],
                    "Item Quantity": [parsed_output.get('item_qty', '')],
                    "Item Net Price": [parsed_output.get('item_net_price', '')],
                    "Item Net Worth": [parsed_output.get('item_net_worth', '')],
                    "Item VAT": [parsed_output.get('item_vat', '')],
                    "Item Gross Worth": [parsed_output.get('item_gross_worth', '')],
                    "Total Net Worth": [parsed_output.get('total_net_worth', '')],
                    "Total VAT": [parsed_output.get('total_vat', '')],
                    "Total Gross Worth": [parsed_output.get('total_gross_worth', '')]
                }

                 # Create a DataFrame
                new_df = pd.DataFrame(data)

                # Append new data to the existing dataframe
                updated_df = pd.concat([existing_df, new_df], ignore_index=True)

                # Save the updated dataframe back to a CSV file
                updated_csv = updated_df.to_csv(index=False).encode('utf-8')

                st.download_button(
                    label="Download updated CSV",
                    data=updated_csv,
                    file_name=uploaded_file_append.name,
                    mime='text/csv'
                )

    with cols[1]:
        if st.session_state.show_level_5:
            if st.button('Extract in new Excel file'):
                st.write('Extracting...')

                #Calling the API
                output = query(bytes_data)
                # st.write("OUTPUT: ")
                # st.write(output)

                # Extract the generated text
                generated_text = output[0]['generated_text']

                # Parse the generated text into a dictionary
                parsed_output = {}
                segments = generated_text.split('<s_')
                for segment in segments[1:]:  # Skip the first empty segment
                    key_value = segment.split('>', 1)
                    if len(key_value) == 2:
                        key = key_value[0].strip()
                        value = key_value[1].split('<')[0].strip()
                        parsed_output[key] = value

                # Print the dictionary
                #st.write(parsed_output)

                # Preparation for creating CSV file
                data = {
                    "Invoice No": [parsed_output.get('invoice_no', '')],
                    "Invoice Date": [parsed_output.get('invoice_date', '')],
                    "Seller": [parsed_output.get('seller', '')],
                    "Client": [parsed_output.get('client', '')],
                    "Seller Tax ID": [parsed_output.get('seller_tax_id', '')],
                    "Client Tax ID": [parsed_output.get('client_tax_id', '')],
                    "IBAN": [parsed_output.get('iban', '')],
                    "Item Description": [parsed_output.get('item_desc', '')],
                    "Item Quantity": [parsed_output.get('item_qty', '')],
                    "Item Net Price": [parsed_output.get('item_net_price', '')],
                    "Item Net Worth": [parsed_output.get('item_net_worth', '')],
                    "Item VAT": [parsed_output.get('item_vat', '')],
                    "Item Gross Worth": [parsed_output.get('item_gross_worth', '')],
                    "Total Net Worth": [parsed_output.get('total_net_worth', '')],
                    "Total VAT": [parsed_output.get('total_vat', '')],
                    "Total Gross Worth": [parsed_output.get('total_gross_worth', '')]
                }

                # Create a DataFrame
                df = pd.DataFrame(data)
                # st.write(df.columns)

                csv = df.to_csv(index=False).encode('utf-8')

                st.download_button(
                    label="Download updated CSV",
                    data=csv,
                    file_name='invoice_data.csv',
                    mime='text/csv'
                )

                st.session_state.show_level_6 = True
                st.session_state.show_level_2 = False
                st.session_state.show_level_3 = False
                st.session_state.show_level_4 = False
        

def adhaar():
    st.markdown(
        """
        <style>
        .stApp {
        background-color: #73098F;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100%25' height='100%25' viewBox='0 0 1600 800'%3E%3Cg %3E%3Cpath fill='%237b0f86' d='M486 705.8c-109.3-21.8-223.4-32.2-335.3-19.4C99.5 692.1 49 703 0 719.8V800h843.8c-115.9-33.2-230.8-68.1-347.6-92.2C492.8 707.1 489.4 706.5 486 705.8z'/%3E%3Cpath fill='%237e157c' d='M1600 0H0v719.8c49-16.8 99.5-27.8 150.7-33.5c111.9-12.7 226-2.4 335.3 19.4c3.4 0.7 6.8 1.4 10.2 2c116.8 24 231.7 59 347.6 92.2H1600V0z'/%3E%3Cpath fill='%23761a6a' d='M478.4 581c3.2 0.8 6.4 1.7 9.5 2.5c196.2 52.5 388.7 133.5 593.5 176.6c174.2 36.6 349.5 29.2 518.6-10.2V0H0v574.9c52.3-17.6 106.5-27.7 161.1-30.9C268.4 537.4 375.7 554.2 478.4 581z'/%3E%3Cpath fill='%236e205b' d='M0 0v429.4c55.6-18.4 113.5-27.3 171.4-27.7c102.8-0.8 203.2 22.7 299.3 54.5c3 1 5.9 2 8.9 3c183.6 62 365.7 146.1 562.4 192.1c186.7 43.7 376.3 34.4 557.9-12.6V0H0z'/%3E%3Cpath fill='%2366254F' d='M181.8 259.4c98.2 6 191.9 35.2 281.3 72.1c2.8 1.1 5.5 2.3 8.3 3.4c171 71.6 342.7 158.5 531.3 207.7c198.8 51.8 403.4 40.8 597.3-14.8V0H0v283.2C59 263.6 120.6 255.7 181.8 259.4z'/%3E%3Cpath fill='%23742350' d='M1600 0H0v136.3c62.3-20.9 127.7-27.5 192.2-19.2c93.6 12.1 180.5 47.7 263.3 89.6c2.6 1.3 5.1 2.6 7.7 3.9c158.4 81.1 319.7 170.9 500.3 223.2c210.5 61 430.8 49 636.6-16.6V0z'/%3E%3Cpath fill='%2382214f' d='M454.9 86.3C600.7 177 751.6 269.3 924.1 325c208.6 67.4 431.3 60.8 637.9-5.3c12.8-4.1 25.4-8.4 38.1-12.9V0H288.1c56 21.3 108.7 50.6 159.7 82C450.2 83.4 452.5 84.9 454.9 86.3z'/%3E%3Cpath fill='%23911d4b' d='M1600 0H498c118.1 85.8 243.5 164.5 386.8 216.2c191.8 69.2 400 74.7 595 21.1c40.8-11.2 81.1-25.2 120.3-41.7V0z'/%3E%3Cpath fill='%23a11943' d='M1397.5 154.8c47.2-10.6 93.6-25.3 138.6-43.8c21.7-8.9 43-18.8 63.9-29.5V0H643.4c62.9 41.7 129.7 78.2 202.1 107.4C1020.4 178.1 1214.2 196.1 1397.5 154.8z'/%3E%3Cpath fill='%23B21437' d='M1315.3 72.4c75.3-12.6 148.9-37.1 216.8-72.4h-723C966.8 71 1144.7 101 1315.3 72.4z'/%3E%3C/g%3E%3C/svg%3E");
        background-attachment: fixed;
        background-size: cover;
        }
        </style>
        <h1 style='text-align: center;'>Adhaar Extraction</h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<p style='padding-top:100px'></p>", unsafe_allow_html=True)


    if 'show_level_1' not in st.session_state:
        st.session_state.show_level_1 = False
    if 'show_level_2' not in st.session_state:
        st.session_state.show_level_2 = False
    if 'show_level_3' not in st.session_state:
        st.session_state.show_level_3 = False
    if 'show_level_4' not in st.session_state:
        st.session_state.show_level_4 = False
    if 'show_level_5' not in st.session_state:
        st.session_state.show_level_5 = False
    if 'show_level_6' not in st.session_state:
        st.session_state.show_level_6 = False

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a file", key="upload_a_file", type=["png", "jpeg", "jpg"])

    if uploaded_file is not None:
        # Display file details
        st.write(f"Filename: {uploaded_file.name}")
        st.write(f"File type: {uploaded_file.type}")
        st.write(f"File size: {uploaded_file.size} bytes")
        st.session_state.show_level_1 = True


    if st.session_state.show_level_1:    
        
        if st.button('Extract Adhaar Data?'):
            st.session_state.show_level_2 = True
            st.session_state.show_level_5 = True
            st.session_state.show_level_3 = False
            st.session_state.show_level_4 = False
            st.session_state.show_level_6 = False
                
        
    cols = st.columns(2)
    # Add buttons to each column
    with cols[0]:
        if st.session_state.show_level_2:
            if st.button('Append Data in existing file'):
                st.session_state.show_level_3 = True
                st.session_state.show_level_6 = False
                st.session_state.show_level_5 = False

        if st.session_state.show_level_3:
            # File uploader widget with a unique key
            uploaded_file_append = st.file_uploader("Choose a file", key="append_a_file", type=["csv"])

            if uploaded_file_append is not None:
                # Display file details
                st.write(f"Filename: {uploaded_file_append.name}")
                st.write(f"File type: {uploaded_file_append.type}")
                st.write(f"File size: {uploaded_file_append.size} bytes")
                
                existing_df = pd.read_csv(uploaded_file_append)
                st.session_state.show_level_4 = True

                # Read the image file
                image = Image.open(uploaded_file)
                img = np.array(image)

                # Resize the image
                img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Calculate the variance of the Laplacian
                var = cv2.Laplacian(img, cv2.CV_64F).var()
                #st.write(f"Laplacian variance: {var}")

                if var < 50:
                    st.write("Image is Too Blurry....")
                else:
                    # Extract text using Tesseract OCR
                    text = pytesseract.image_to_string(image, lang='eng')
                    text = ftfy.fix_text(text)
                    text = ftfy.fix_encoding(text)
                        
                if "male" in text.lower():
                    data = aadhaar_read.adhaar_read_data(text)

                    # Create a DataFrame
                    new_df = pd.DataFrame([data])

                    # Append new data to the existing dataframe
                    updated_df = pd.concat([existing_df, new_df], ignore_index=True)

                    # Save the updated dataframe back to a CSV file
                    updated_csv = updated_df.to_csv(index=False).encode('utf-8')

                    st.download_button(
                        label="Download updated CSV",
                        data=updated_csv,
                        file_name=uploaded_file_append.name,
                        mime='text/csv'
                    )

                else:
                    st.write("ERROR: Provide an Adhaar card")

                # if data['ID Type'].lower() == 'pan':
                #     st.write("\n---------- PAN Details ----------")
                #     st.write(f"\nPAN Number: {data['PAN']}")
                #     st.write(f"\nName: {data['Name']}")
                #     st.write(f"\nFather's Name: {data['Father Name']}")
                #     st.write(f"\nDate Of Birth: {data['Date of Birth']}")
                #     st.write("\n---------------------------------")
                # elif data['ID Type'].lower() == 'adhaar':
                #     st.write("\n---------- ADHAAR Details ----------")
                #     st.write(f"\nADHAAR Number: {data['Adhaar Number']}")
                #     st.write(f"\nName: {data['Name']}")
                #     st.write(f"\nDate Of Birth: {data['Date of Birth']}")
                #     st.write(f"\nSex: {data['Sex']}")
                #     st.write("\n------------------------------------")


                



            

    with cols[1]:
        if st.session_state.show_level_5:
            if st.button('Extract in new Excel file'):
                st.write('Extracting...')

                # Read the image file
                image = Image.open(uploaded_file)
                img = np.array(image)

                # Resize the image
                img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Calculate the variance of the Laplacian
                var = cv2.Laplacian(img, cv2.CV_64F).var()
                #st.write(f"Laplacian variance: {var}")

                if var < 1:
                    st.write("Image is Too Blurry....")
                else:
                    # Extract text using Tesseract OCR
                    text = pytesseract.image_to_string(image, lang='eng')
                    text = ftfy.fix_text(text)
                    text = ftfy.fix_encoding(text)
                        
                if "male" in text.lower():
                    data = aadhaar_read.adhaar_read_data(text)

                    df = pd.DataFrame([data])
                    csv = df.to_csv(index=False).encode('utf-8')

                    st.download_button(
                        label="Download updated CSV",
                        data=csv,
                        file_name='document_data.csv',
                        mime='text/csv'
                    )

                else:
                    st.write("ERROR: Provide an Adhaar card")

                # if data['ID Type'].lower() == 'pan':
                #     st.write("\n---------- PAN Details ----------")
                #     st.write(f"\nPAN Number: {data['PAN']}")
                #     st.write(f"\nName: {data['Name']}")
                #     st.write(f"\nFather's Name: {data['Father Name']}")
                #     st.write(f"\nDate Of Birth: {data['Date of Birth']}")
                #     st.write("\n---------------------------------")
                # elif data['ID Type'].lower() == 'adhaar':
                #     st.write("\n---------- ADHAAR Details ----------")
                #     st.write(f"\nADHAAR Number: {data['Adhaar Number']}")
                #     st.write(f"\nName: {data['Name']}")
                #     st.write(f"\nDate Of Birth: {data['Date of Birth']}")
                #     st.write(f"\nSex: {data['Sex']}")
                #     st.write("\n------------------------------------")

                

                st.session_state.show_level_6 = True
                st.session_state.show_level_2 = False
                st.session_state.show_level_3 = False
                st.session_state.show_level_4 = False
        
                
def pancard():
    st.markdown(
        """
        <style>
        .stApp {
        background-color: #51788C;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100%25' height='100%25' viewBox='0 0 1600 800'%3E%3Cg %3E%3Cpath fill='%232b6d93' d='M486 705.8c-109.3-21.8-223.4-32.2-335.3-19.4C99.5 692.1 49 703 0 719.8V800h843.8c-115.9-33.2-230.8-68.1-347.6-92.2C492.8 707.1 489.4 706.5 486 705.8z'/%3E%3Cpath fill='%2300619a' d='M1600 0H0v719.8c49-16.8 99.5-27.8 150.7-33.5c111.9-12.7 226-2.4 335.3 19.4c3.4 0.7 6.8 1.4 10.2 2c116.8 24 231.7 59 347.6 92.2H1600V0z'/%3E%3Cpath fill='%2300529f' d='M478.4 581c3.2 0.8 6.4 1.7 9.5 2.5c196.2 52.5 388.7 133.5 593.5 176.6c174.2 36.6 349.5 29.2 518.6-10.2V0H0v574.9c52.3-17.6 106.5-27.7 161.1-30.9C268.4 537.4 375.7 554.2 478.4 581z'/%3E%3Cpath fill='%2300429f' d='M0 0v429.4c55.6-18.4 113.5-27.3 171.4-27.7c102.8-0.8 203.2 22.7 299.3 54.5c3 1 5.9 2 8.9 3c183.6 62 365.7 146.1 562.4 192.1c186.7 43.7 376.3 34.4 557.9-12.6V0H0z'/%3E%3Cpath fill='%23112C9A' d='M181.8 259.4c98.2 6 191.9 35.2 281.3 72.1c2.8 1.1 5.5 2.3 8.3 3.4c171 71.6 342.7 158.5 531.3 207.7c198.8 51.8 403.4 40.8 597.3-14.8V0H0v283.2C59 263.6 120.6 255.7 181.8 259.4z'/%3E%3Cpath fill='%23342896' d='M1600 0H0v136.3c62.3-20.9 127.7-27.5 192.2-19.2c93.6 12.1 180.5 47.7 263.3 89.6c2.6 1.3 5.1 2.6 7.7 3.9c158.4 81.1 319.7 170.9 500.3 223.2c210.5 61 430.8 49 636.6-16.6V0z'/%3E%3Cpath fill='%23482292' d='M454.9 86.3C600.7 177 751.6 269.3 924.1 325c208.6 67.4 431.3 60.8 637.9-5.3c12.8-4.1 25.4-8.4 38.1-12.9V0H288.1c56 21.3 108.7 50.6 159.7 82C450.2 83.4 452.5 84.9 454.9 86.3z'/%3E%3Cpath fill='%23571c8e' d='M1600 0H498c118.1 85.8 243.5 164.5 386.8 216.2c191.8 69.2 400 74.7 595 21.1c40.8-11.2 81.1-25.2 120.3-41.7V0z'/%3E%3Cpath fill='%23641489' d='M1397.5 154.8c47.2-10.6 93.6-25.3 138.6-43.8c21.7-8.9 43-18.8 63.9-29.5V0H643.4c62.9 41.7 129.7 78.2 202.1 107.4C1020.4 178.1 1214.2 196.1 1397.5 154.8z'/%3E%3Cpath fill='%236F0983' d='M1315.3 72.4c75.3-12.6 148.9-37.1 216.8-72.4h-723C966.8 71 1144.7 101 1315.3 72.4z'/%3E%3C/g%3E%3C/svg%3E");
        background-attachment: fixed;
        background-size: cover;
        }
        </style>
        <h1 style='text-align: center;'>Pancard Extraction</h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<p style='padding-top:100px'></p>", unsafe_allow_html=True)


    if 'show_level_1' not in st.session_state:
        st.session_state.show_level_1 = False
    if 'show_level_2' not in st.session_state:
        st.session_state.show_level_2 = False
    if 'show_level_3' not in st.session_state:
        st.session_state.show_level_3 = False
    if 'show_level_4' not in st.session_state:
        st.session_state.show_level_4 = False
    if 'show_level_5' not in st.session_state:
        st.session_state.show_level_5 = False
    if 'show_level_6' not in st.session_state:
        st.session_state.show_level_6 = False

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a file", key="upload_p_file", type=["png", "jpeg", "jpg"])

    if uploaded_file is not None:
        # Display file details
        st.write(f"Filename: {uploaded_file.name}")
        st.write(f"File type: {uploaded_file.type}")
        st.write(f"File size: {uploaded_file.size} bytes")
        st.session_state.show_level_1 = True


    if st.session_state.show_level_1:
        if st.button('Extract Pancard Data?'):
            st.session_state.show_level_2 = True
            st.session_state.show_level_5 = True
            st.session_state.show_level_3 = False
            st.session_state.show_level_4 = False
            st.session_state.show_level_6 = False

    cols = st.columns(2)
    # Add buttons to each column
    with cols[0]:
        if st.session_state.show_level_2:
            if st.button('Append Data in existing file'):
                st.session_state.show_level_3 = True
                st.session_state.show_level_6 = False
                st.session_state.show_level_5 = False

        if st.session_state.show_level_3:
            # File uploader widget with a unique key
            uploaded_file_append = st.file_uploader("Choose a file", key="append_p_file", type=["csv"])

            if uploaded_file_append is not None:
                # Display file details
                st.write(f"Filename: {uploaded_file_append.name}")
                st.write(f"File type: {uploaded_file_append.type}")
                st.write(f"File size: {uploaded_file_append.size} bytes")
                
                existing_df = pd.read_csv(uploaded_file_append)
                st.session_state.show_level_4 = True

                # Read the image file
                image = Image.open(uploaded_file)
                img = np.array(image)

                # Resize the image
                img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Calculate the variance of the Laplacian
                var = cv2.Laplacian(img, cv2.CV_64F).var()
                #st.write(f"Laplacian variance: {var}")

                if var < 50:
                    st.write("Image is Too Blurry....")
                else:
                    # Extract text using Tesseract OCR
                    text = pytesseract.image_to_string(image, lang='eng')
                    text = ftfy.fix_text(text)
                    text = ftfy.fix_encoding(text)
                        
                if "income" in text.lower() or "tax" in text.lower() or "department" in text.lower():
                    data = pan_read.pan_read_data(text)

                    # Create a DataFrame
                    new_df = pd.DataFrame([data])

                    # Append new data to the existing dataframe
                    updated_df = pd.concat([existing_df, new_df], ignore_index=True)

                    # Save the updated dataframe back to a CSV file
                    updated_csv = updated_df.to_csv(index=False).encode('utf-8')

                    st.download_button(
                        label="Download updated CSV",
                        data=updated_csv,
                        file_name=uploaded_file_append.name,
                        mime='text/csv'
                    )

                else:
                    st.write("ERROR: Provide an PAN card")

                # if data['ID Type'].lower() == 'pan':
                #     st.write("\n---------- PAN Details ----------")
                #     st.write(f"\nPAN Number: {data['PAN']}")
                #     st.write(f"\nName: {data['Name']}")
                #     st.write(f"\nFather's Name: {data['Father Name']}")
                #     st.write(f"\nDate Of Birth: {data['Date of Birth']}")
                #     st.write("\n---------------------------------")
                # elif data['ID Type'].lower() == 'adhaar':
                #     st.write("\n---------- ADHAAR Details ----------")
                #     st.write(f"\nADHAAR Number: {data['Adhaar Number']}")
                #     st.write(f"\nName: {data['Name']}")
                #     st.write(f"\nDate Of Birth: {data['Date of Birth']}")
                #     st.write(f"\nSex: {data['Sex']}")
                #     st.write("\n------------------------------------")


                

    with cols[1]:
        if st.session_state.show_level_5:
            if st.button('Extract in new Excel file'):
                st.write('Extracting...')

                # Read the image file
                image = Image.open(uploaded_file)
                img = np.array(image)

                # Resize the image
                img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Calculate the variance of the Laplacian
                var = cv2.Laplacian(img, cv2.CV_64F).var()
                #st.write(f"Laplacian variance: {var}")

                if var < 50:
                    st.write("Image is Too Blurry....")
                else:
                    # Extract text using Tesseract OCR
                    text = pytesseract.image_to_string(image, lang='eng')
                    text = ftfy.fix_text(text)
                    text = ftfy.fix_encoding(text)
                        
                if "income" in text.lower() or "tax" in text.lower() or "department" in text.lower():
                    data = pan_read.pan_read_data(text)
                    df = pd.DataFrame([data])
                    csv = df.to_csv(index=False).encode('utf-8')

                    st.download_button(
                        label="Download updated CSV",
                        data=csv,
                        file_name='document_data.csv',
                        mime='text/csv'
                    )

                    st.session_state.show_level_6 = True
                    st.session_state.show_level_2 = False
                    st.session_state.show_level_3 = False
                    st.session_state.show_level_4 = False
                    
                else:
                    st.write("ERROR: Provide an PAN card")

                # if data['ID Type'].lower() == 'pan':
                #     st.write("\n---------- PAN Details ----------")
                #     st.write(f"\nPAN Number: {data['PAN']}")
                #     st.write(f"\nName: {data['Name']}")
                #     st.write(f"\nFather's Name: {data['Father Name']}")
                #     st.write(f"\nDate Of Birth: {data['Date of Birth']}")
                #     st.write("\n---------------------------------")
                # elif data['ID Type'].lower() == 'adhaar':
                #     st.write("\n---------- ADHAAR Details ----------")
                #     st.write(f"\nADHAAR Number: {data['Adhaar Number']}")
                #     st.write(f"\nName: {data['Name']}")
                #     st.write(f"\nDate Of Birth: {data['Date of Birth']}")
                #     st.write(f"\nSex: {data['Sex']}")
                #     st.write("\n------------------------------------")

                

# Main function to handle navigation
def main():
    # Create the navigation bar
    selected = option_menu(
        menu_title=None,  # Hide the menu title
        options=["Home", "Invoice", "Adhaar", "Pancard"],  # Menu options
        icons=["house", "file-earmark", "file-earmark", "file-earmark", "file-earmark"],  # Icons for each menu option
        menu_icon="cast",  # Menu icon
        default_index=0,  # Default selected option
        orientation="horizontal",  # Orientation of the menu
        styles={
            "container": {"padding": "0!important", "background-color": "#0A0D33"},
            "icon": {"color": "#f2f2f2", "font-size": "17px"},
            "nav-link": {
                "font-size": "20px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#73098F",
            },
            "nav-link-selected": {"background-color": "#5622CA"},
        }
    )

    # Show the selected page
    if selected == "Home":
        home()
    elif selected == "Invoice":
        invoice()
    elif selected == "Adhaar":
        adhaar()
    elif selected == "Pancard":
        pancard()
    elif selected == "Driving":
        pancard()  

if __name__ == '__main__':
    main()
