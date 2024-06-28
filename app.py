import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile

# Page title
st.set_page_config(page_title='ML model builder', page_icon='🏗️')
st.title('🏗️ ML model builder')

with st.expander('About this app'):
    st.markdown('**What can this app do?**')
    st.info('This app allows users to build a machine learning (ML) model in an end-to-end workflow.')

# Sidebar for accepting input parameters
with st.sidebar:
    st.header('1. Input data')
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Main content area
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Rest of your model building and evaluation code goes here

    st.write("Data loaded successfully.")

else:
    st.warning('Upload a CSV file to get started.')

