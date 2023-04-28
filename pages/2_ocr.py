
from streamlit_drawable_canvas import st_canvas
import streamlit as st
import pandas as pd
import numpy as np

import io

import requests
import json

from PIL import Image

st.title("OCR")

canvas_result = st_canvas(background_color="#FFFFFF")

API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-small-handwritten"


API_TOKEN = st.secrets["hf_api"]

headers = {"Authorization": f"Bearer {API_TOKEN}"}


@st.cache_data
def query(data):
    response = requests.request(
        "POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


if canvas_result.image_data is not None:
    img = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')

    output = io.BytesIO()
    img.save(output, 'PNG')
    st.write(query(output.getvalue()))
    # st.write(query(canvas_result.image_data))
