import streamlit as st
import pandas as pd
import numpy as np

# Titling
st.title('Demo')

# Streamlit writing
st.write("Writing in streamlit!")

# Streamlit magic
"Magic!"

# Sliders + widget updating
val = st.slider("Slider", 10, 200, 50, 2)

val

# pandas integration

df = pd.DataFrame({"Name": ["D", "A", "C"], "Pos": [1, 2, 3]})

df

# charts

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

foo = st.checkbox('Show dataframe')
if foo:
    "Hello!"

# sidebar
st.sidebar.title("Test")
st.sidebar.write("D")
