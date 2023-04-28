import streamlit as st
import pandas as pd
import numpy as np

import requests
import json


# Titling
st.title('Sentimental Analysis')

API_TOKEN = st.secrets["hf_api"]

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"


text_inputs = st.text_input("Enter a phrase to analyze:")


@st.cache_data
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


data = query({"inputs": text_inputs})

st.write(data)
