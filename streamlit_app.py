import streamlit as st
import requests

FLASK_API_URL_GET = "http://127.0.0.1:8000/api/get_data"
FLASK_API_URL_POST = "http://127.0.0.1:8000/api/send_data"

st.title("Flask + Streamlit Hybrid App")

# Fetch Data from Flask API
if st.button("Get Data from Flask API"):
    try:
        response = requests.get(FLASK_API_URL_GET)
        if response.status_code == 200:
            data = response.json()
            st.success(f"Received: {data['message']}")
        else:
            st.error(f"Error fetching data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

# Send Data to Flask API
st.subheader("Send Data to Flask API:")
user_input = st.text_input("Enter new message:", "")

if st.button("Send Message"):
    try:
        response = requests.post(FLASK_API_URL_POST, json={"message": user_input})
        if response.status_code == 200:
            data = response.json()
            st.success(data["response"])
        else:
            st.error(f"Error updating data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
