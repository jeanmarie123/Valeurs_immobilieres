import streamlit as st
import pandas as pd
import plotly.express as px
from workflow.manip import *
import os 
import warnings
warnings.filterwarnings('ignore')


# Titre de la page via le web
st.set_page_config(page_title = "Dashboad imo France", page_icon = ":bar_chart:", layout = "wide")

st.subheader(" :bar_chart: Tendance de l'immobilier en France ")

tab1, tab2 = st.tabs(["Cat", "Dog"])

with tab1:
    input_text = st.text_area(label = "entrez votre input")
    st.write(input_text)
    st.dataframe(data())


with tab2:
    input_v = st.text_area(label = "entrez votre code")
    st.write(input_v)
    st.dataframe(data())
