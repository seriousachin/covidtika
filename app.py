import datetime
import json
import numpy as np
import requests
import pandas as pd
import streamlit as st
from copy import deepcopy
from fake_useragent import UserAgent
from footer_utils import image, link, layout, footer

# browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
# browser_header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36'}

st.set_page_config(layout='wide',
                   #initial_sidebar_state='collapsed',
                   page_icon="https://students.iiserkol.ac.in/~sp13ip016/favicon.ico",
                   page_title="Covid Tika Daily Utilization Tracker Slot Availability")

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def dd():
    df = pd.read_csv("22.csv",index_col = False)
    return df


def filter_column(df, col, value):
    df_temp = deepcopy(df.loc[df[col] == value, :])
    return df_temp

def filter_capacity(df, col, value):
    df_temp = deepcopy(df.loc[df[col] > value, :])
    return df_temp
mappingdf=dd()
df= mappingdf.sort_values(by='slots', ascending=False)

@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

#mapping_df = load_mapping()

rename_mapping = {
    'date': 'Date',
    'min_age_limit': 'Minimum Age Limit',
    'available_capacity_dose1': 'Available Capacity',
    'vaccine': 'Vaccine',
    'Total doses til date': 'People vaccinated till date',
    'center': 'No of not fully utilized centers',
    'state' : 'State',
    'district' : 'District',
    'slots': 'Unutilized Doses',
    'today' : 'Doses Administered'
    }

st.title('Covid Tika Daily Utilization Tracker for 45+ Group: 22 May')
st.write('Tracking daily UnUtilization of Covid-19 vaccine doses for 45+ group. Status as on 22 May 2021 , 10:30-11:00PM from CoWIN ')

valid_states = list(np.unique(mappingdf["state"].values))
# numdays = st.sidebar.slider('Select Date Range', 0, 100, 10)
#unique_districts = list(mappingdf["district"].unique())
#unique_districts.sort()
left_column_1, right_column_1 = st.beta_columns(2)
with left_column_1:
    state_inp = st.selectbox('Select State', [""] + valid_states)
    if state_inp != "":
        df = filter_column(df, "state", state_inp)
        #with right_column_1:
            #dist_inp = st.selectbox('Select District', [""]+unique_districts)
            #if dist_inp != "":
                #df = filter_column(df, "district", dist_inp)





st.header('Total UNUTILIZED doses are '+str(sum(df['slots']))+'. Doses utilization % is just '+str(round(sum(df['today'])*100.00/ (sum(df['today'])+sum(df['slots'])),2))+'%.')
df.rename(columns=rename_mapping, inplace=True)
table = deepcopy(df[['District','Unutilized Doses','Doses Administered','People vaccinated till date']])
table.reset_index(inplace=True, drop=True)
st.table(table)

    

pageviews=Pageviews()
pageviews.append('dummy')
pg_views = len(pageviews)
footer(pg_views)
