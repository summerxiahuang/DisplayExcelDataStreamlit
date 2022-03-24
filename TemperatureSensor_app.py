# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:51:44 2022

@author: Summer
"""

import pandas as pd
#import plotly.express as px
import streamlit as st
#import numpy as np

st.set_page_config(page_title = "Cable Length Dashboard",
                   page_icon = ":telescope:",
                   layout = "wide"
                   )
# ---- READ EXCEL ----
@st.cache
def get_data_from_excel(filename,datasheet):
    
    df = pd.read_excel(
        io = filename,
        engine = 'openpyxl',
        sheet_name = datasheet,
        )

    
    #df.colums = ['Cable Length','Theta','No.']
    #df["hour"] = pd.to_datetime(df["Time"],format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel('SensorLocation.xlsx','Sheet1')
df = df.drop(index = 0)
df = df[["Description","X","Y","Z","R","Theta"]]
#df1 = get_data_from_excel('Trayectoria 14 marzo.xlsx','Hoja1')
#st.dataframe(df)

# ----SIDEBAR----
st.sidebar.header('Please Choose Sensor Position Here:')
description = st.sidebar.multiselect(
     "Select the sensor position:",
     options = df["Description"].unique(),
     default = df["Description"][2]
    )



# ---- MAINPAGE ----
st.title(":telescope: Table of the sensor position")
st.markdown("""##""")

df_selection = df.query(" Description== @description")
st.dataframe(df_selection)


# ---- HIDE STREAMLIT STYLE ----

hide_st_style = """
                <style>
                #MainMenu{visibility: hidden;}
                footer{visibility: hidden;}
                header{visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style,unsafe_allow_html = True)       
