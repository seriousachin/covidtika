import datetime
import json
import numpy as np
import requests
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
#import chart_studio.plotly as py
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
    df = pd.read_csv("30.csv",index_col = False)
    return df


def filter_column(df, col, value):
    df_temp = deepcopy(df.loc[df[col] == value, :])
    return df_temp

def filter_capacity(df, col, value):
    df_temp = deepcopy(df.loc[df[col] > value, :])
    return df_temp
mappingdf=dd()
df= mappingdf.sort_values(by='avgdaily', ascending=False)

@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

#mapping_df = load_mapping()

rename_mapping = {
    'date': 'Date',
    'min_age_limit': 'Minimum Age Limit',
    'available_capacity_dose1': 'Available Capacity',
    'vaccine': 'Vaccine',
    'Total doses til date': 'People(45+) vaccinated till date',
    'center': 'No of not fully utilized centers',
    'state' : 'State',
    'district' : 'District',
    'slots': 'Unutilized Doses(45+)',
    'slots 18-44': 'Unutilized Doses(18-44)',
    'today' : 'Doses Administered(45+)',
    'avgdaily': 'Last 7 days Daily Avg Vaccination(45+)',
    'today 18' : 'Doses Administered(18-44)',
    'Total doses til date 18': 'People(18-44) vaccinated till date',
    'avgdaily 18-44': 'Last 7 days Daily Avg Vaccination(18-44)'
    }

st.title('Covid Tika Daily Utilization, Coveragae, Speed Tracker : 30 May')
st.write('Tracking daily (non) Utilization, Coverage, Speed, District variations of Covid-19 vaccine doses for 45+ and 18-44 group. Status as on 30 May 2021 , 7:40-8:20PM from CoWIN. ')
#dfg = pd.read_csv("map.csv")
#ff=df.sort_values(by='utilization %', ascending=True)
ff=[]
name_stat=np.unique(mappingdf["state"].values)
pp=[105669,15897000,372210,8113000,24447000,293781,6955000,141600,80500,5183000,401941,18165000,7177000,2264000,3279000,8395000,18903000,12782000,73245,18467,18965000,35159000,731563,796807,293638,533386,12778000,358310,8924000,17351000,163478,24993000,10372000,987290,47793000,2848000,28410000]
pp1=[181514,23656083,733996,15487657,48850895,503113,12712404,181600,
141500,7684565,687704,30700637,13392472,3259129,6122579,16526904,29901024,13879550,125328
,31506,36034217,56232043,1450455,1583181,579270,1054334,18597693,613176,13816067,34233274,323095,32664620,17373309,1949580,99009789,5206552,44278721]
uind={'Doses(45+) utilization %':round(sum(df['today'])*100.00/ (sum(df['today'])+sum(df['slots'])),2),
     '% of 45+ people vaccinated':round(100*sum(df['Total doses til date'])/sum(pp),2),
     'Last 7 days avg per 100 people(45+)':round(100*sum(df['avgdaily'])/sum(pp),2),
      'Doses(18-44) utilization %':round(sum(df['today 18'])*100.00/ (sum(df['today 18'])+sum(df['slots 18-44'])),2),
     '% of 18-44 people vaccinated':round(100*sum(df['Total doses til date 18'])/sum(pp1),2),
     'Last 7 days avg per 100 people(18-44)':round(100*sum(df['avgdaily 18-44'])/sum(pp1),2),
     'Today Dose wastage %':round(100*sum(df['wastage'])/(sum(df['today 18'])+sum(df['today'])),2)}
for i in range(0,37):
    dfs=df.loc[df['state'] == name_stat[i]]
    if sum(dfs['slots'])+sum(dfs['today'])==0 and sum(dfs['slots 18-44'])+sum(dfs['today 18'])==0:
        ff.append({'state':name_stat[i],'Doses(45+) utilization %':100,'vaccinated today':sum(dfs['today']),'Last 7 days avg per 100 people(45+)':round(100*sum(dfs['avgdaily'])/pp[i],2),'7 days daily avg':sum(dfs['avgdaily']),'% of 45+ people vaccinated':round(100*sum(dfs['Total doses til date'])/pp[i],2) ,'People vaccinated till date':sum(dfs['Total doses til date']),'Doses(18-44) utilization %':100,'vaccinated today 18-44':sum(dfs['today 18']),'Last 7 days avg per 100 people(18-44)':round(100*sum(dfs['avgdaily 18-44'])/pp1[i],2),'7 days daily avg 18-44':sum(dfs['avgdaily 18-44']),'% of 18-44 people vaccinated':round(100*sum(dfs['Total doses til date 18'])/pp1[i],2) ,'People(18-44) vaccinated till date':sum(dfs['Total doses til date 18'])})
    elif sum(dfs['slots'])+sum(dfs['today'])==0:
        ff.append({'state':name_stat[i],'Doses(45+) utilization %':100,'vaccinated today':sum(dfs['today']),'Last 7 days avg per 100 people(45+)':round(100*sum(dfs['avgdaily'])/pp[i],2),'7 days daily avg':sum(dfs['avgdaily']),'% of 45+ people vaccinated':round(100*sum(dfs['Total doses til date'])/pp[i],2) ,'People vaccinated till date':sum(dfs['Total doses til date']),'Doses(18-44) utilization %':round(sum(dfs['today 18'])*100.00/ (sum(dfs['today 18'])+sum(dfs['slots 18-44'])),2),'vaccinated today 18-44':sum(dfs['today 18']),'Last 7 days avg per 100 people(18-44)':round(100*sum(dfs['avgdaily 18-44'])/pp1[i],2),'7 days daily avg 18-44':sum(dfs['avgdaily 18-44']),'% of 18-44 people vaccinated':round(100*sum(dfs['Total doses til date 18'])/pp1[i],2) ,'People(18-44) vaccinated till date':sum(dfs['Total doses til date 18'])})
    elif sum(dfs['slots 18-44'])+sum(dfs['today 18'])==0:
        ff.append({'state':name_stat[i],'Doses(45+) utilization %':round(sum(dfs['today'])*100/(sum(dfs['slots'])+sum(dfs['today'])),2),'vaccinated today':sum(dfs['today']),'Last 7 days avg per 100 people(45+)':round(100*sum(dfs['avgdaily'])/pp[i],2),'7 days daily avg':sum(dfs['avgdaily']),'% of 45+ people vaccinated':round(100*sum(dfs['Total doses til date'])/pp[i],2) ,'People vaccinated till date':sum(dfs['Total doses til date']),'Doses(18-44) utilization %':100,'vaccinated today 18-44':sum(dfs['today 18']),'Last 7 days avg per 100 people(18-44)':round(100*sum(dfs['avgdaily 18-44'])/pp1[i],2),'7 days daily avg 18-44':sum(dfs['avgdaily 18-44']),'% of 18-44 people vaccinated':round(100*sum(dfs['Total doses til date 18'])/pp1[i],2) ,'People(18-44) vaccinated till date':sum(dfs['Total doses til date 18'])})
    else:
        ff.append({'state':name_stat[i],'Doses(45+) utilization %':round(sum(dfs['today'])*100/(sum(dfs['slots'])+sum(dfs['today'])),2),'vaccinated today':sum(dfs['today']),'Last 7 days avg per 100 people(45+)':round(100*sum(dfs['avgdaily'])/pp[i],2),'7 days daily avg':sum(dfs['avgdaily']),'% of 45+ people vaccinated':round(100*sum(dfs['Total doses til date'])/pp[i],2) ,'People vaccinated till date':sum(dfs['Total doses til date']),'Doses(18-44) utilization %':round(sum(dfs['today 18'])*100.00/ (sum(dfs['today 18'])+sum(dfs['slots 18-44'])),2),'vaccinated today 18-44':sum(dfs['today 18']),'Last 7 days avg per 100 people(18-44)':round(100*sum(dfs['avgdaily 18-44'])/pp1[i],2),'7 days daily avg 18-44':sum(dfs['avgdaily 18-44']),'% of 18-44 people vaccinated':round(100*sum(dfs['Total doses til date 18'])/pp1[i],2) ,'People(18-44) vaccinated till date':sum(dfs['Total doses til date 18'])})

dfg = pd.DataFrame(ff)
#table = deepcopy(dfg[['state','7 days daily avg','People vaccinated till date']])
#table.reset_index(inplace=True, drop=True)
#st.table(table)
for col in dfg.columns:
    dfg[col] = dfg[col].astype(str)

dfg['text'] = dfg['state'] + '<br>' +\
'Today Doses Utilization % : ' + dfg['Doses(45+) utilization %'] +  '<br>' +\
'Vaccinated today:' + dfg['vaccinated today'] +  '<br>' +\
'Last 7 days avg per 100 people(45+):' + dfg['Last 7 days avg per 100 people(45+)'] + '<br>' +\
'Last 7 days Daily Avg Vaccination:' + dfg['7 days daily avg'] + '<br>' +\
'% of 45+ people vaccinated:' + dfg['% of 45+ people vaccinated'] + '<br>' +\
'People vaccinated till date:' + dfg['People vaccinated till date']
dfg['text18'] = dfg['state'] + '<br>' +\
'Today Doses Utilization % : ' + dfg['Doses(18-44) utilization %'] +  '<br>' +\
'Vaccinated today 18-44:' + dfg['vaccinated today 18-44'] +  '<br>' +\
'Last 7 days avg per 100 people(18-44):' + dfg['Last 7 days avg per 100 people(18-44)'] + '<br>' +\
'Last 7 days Daily Avg Vaccination 18-44:' + dfg['7 days daily avg 18-44'] + '<br>' +\
'% of 18-44 people vaccinated:' + dfg['% of 18-44 people vaccinated'] + '<br>' +\
'People(18-44) vaccinated till date:' + dfg['People(18-44) vaccinated till date']


def dashh(val):
    if (val=='% of 18-44 people vaccinated' or val=='Last 7 days avg per 100 people(18-44)' or val=='Doses(18-44) utilization %' ):
        dfg['text']=dfg['text18']
    #if val=='Today Dose wastage %':
        #cs=True
    #else:
        #cs=False
    fig1 = go.Figure(data=go.Choropleth(
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locationmode='geojson-id',
        locations=dfg['state'],
        z=dfg[val].astype(float),

        autocolorscale=False,
        colorscale=[[0, 'RGB(153,0,0)'],[0.2, 'RGB(255,51,51)'],[0.4, 'RGB(255,153,153)'],[0.6, 'RGB(255,204,204)'],[0.8, 'RGB(229,255,204)'],[0.9, 'RGB(0,255,0)'], [1, 'RGB(0,102,0)']],
        #color_continuous_scale=["red", "green"],
        text=dfg[val], 
        hovertext=dfg['text'],
        
        marker_line_color='peachpuff',
        showscale=True,
        #if val=='Today Dose wastage %':
        #reversescale=cs,
        colorbar=dict(
            title={'text': val},

            #thickness=15,
            len=0.35,
            bgcolor='rgba(255,255,255,0.6)',

            tick0=0,
            dtick=max(dfg[val].astype(float))/10,

            xanchor='left',
            x=0.01,
            yanchor='bottom',
            y=0.05
        )
    ))

    fig1.update_geos(
        visible=False,
        projection=dict(
            type='conic conformal',
            parallels=[12.472944444, 35.172805555556],
            rotation={'lat': 24, 'lon': 80}
        ),
        lonaxis={'range': [68, 98]},
        lataxis={'range': [6, 38]}
    )
    #fig1.update_traces( textinfo='value')

    fig1.update_layout(#text=dfg[val], 
        title=dict(
            text=val+" for India on 30 May: "+str(uind[val]),
            xanchor='center',
            x=0.5,
            yref='paper',
            yanchor='bottom',
            y=1,
            pad={'b': 10}
        ),
        margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
        height=750,
        width=750
    )
    return fig1
fig1=dashh('Doses(45+) utilization %')
left_column_2, right_column_2 = st.beta_columns(2)
with left_column_2:
    val = st.selectbox('Select parameter', ['Doses(45+) utilization %','% of 45+ people vaccinated','Last 7 days avg per 100 people(45+)','Doses(18-44) utilization %','% of 18-44 people vaccinated','Last 7 days avg per 100 people(18-44)'])
    fig1=dashh(val)
st.plotly_chart(fig1)
ad=[]
ad.append({'Last 7 days daily avg':'Less than 200',
     'No of Districts':df[df['avgdaily']<200].count()[1]})
ad.append({'Last 7 days daily avg':'Between 200-500',
     'No of Districts':df[df['avgdaily']<500].count()[1]-df[df['avgdaily']<=200].count()[1]})
ad.append({'Last 7 days daily avg':'Between 500-1000',
     'No of Districts':df[df['avgdaily']<1000 ].count()[1]-df[df['avgdaily']<=500].count()[1]})
ad.append({'Last 7 days daily avg':'Between 1000-2000',
     'No of Districts':df[df['avgdaily']<2000 ].count()[1]-df[df['avgdaily']<=1000].count()[1]})
ad.append({'Last 7 days daily avg':'Between 2000-5000',
     'No of Districts':df[df['avgdaily']<5000 ].count()[1]-df[df['avgdaily']<=2000].count()[1]})
ad.append({'Last 7 days daily avg':'More than 5000',
     'No of Districts':df[df['avgdaily']>=5000 ].count()[1]})
ad=pd.DataFrame(ad)
#fig = px.bar(ad, x='Last 7 days daily avg', y='No of Districts')
#fig.update_traces(textposition='outside')

fig = px.pie(ad,values='No of Districts', names='Last 7 days daily avg',title='No of Districts: Last 7 days daily avg vaccinated people(45+ group)',color='Last 7 days daily avg', color_discrete_map={'Less than 200':'RGB(153,0,0)',
                                 'Between 200-500':'RGB(255,51,51)',
                                 'Between 500-1000':'RGB(255,153,153)',
                                 'Between 1000-2000':'RGB(255,204,204)',
                                 'Between 2000-5000':'RGB(229,255,204)',
                                 'More than 5000':'RGB(0,102,0)'})
fig.update_traces(hoverinfo='label+percent', textinfo='value')
fig.add_annotation(text = 'Sachin Pandey @serioussachin, https://covidtika.herokuapp.com & CoWIN,30 May',
                              font_size = 16,
                              showarrow = False,
                              xref = 'paper', x = 0,
                              yref = 'paper', y = -0.3)
st.plotly_chart(fig)
ad18=[]
ad18.append({'Last 7 days daily avg':'Less than 200',
     'No of Districts':df[df['avgdaily 18-44']<200].count()[1]})
ad18.append({'Last 7 days daily avg':'Between 200-500',
     'No of Districts':df[df['avgdaily 18-44']<500].count()[1]-df[df['avgdaily 18-44']<=200].count()[1]})
ad18.append({'Last 7 days daily avg':'Between 500-1000',
     'No of Districts':df[df['avgdaily 18-44']<1000 ].count()[1]-df[df['avgdaily 18-44']<=500].count()[1]})
ad18.append({'Last 7 days daily avg':'Between 1000-2000',
     'No of Districts':df[df['avgdaily 18-44']<2000 ].count()[1]-df[df['avgdaily 18-44']<=1000].count()[1]})
ad18.append({'Last 7 days daily avg':'Between 2000-5000',
     'No of Districts':df[df['avgdaily 18-44']<5000 ].count()[1]-df[df['avgdaily 18-44']<=2000].count()[1]})
ad18.append({'Last 7 days daily avg':'More than 5000',
     'No of Districts':df[df['avgdaily 18-44']>=5000 ].count()[1]})
ad18=pd.DataFrame(ad18)
#fig = px.bar(ad, x='Last 7 days daily avg', y='No of Districts')
#fig.update_traces(textposition='outside')

fig18 = px.pie(ad18,values='No of Districts', names='Last 7 days daily avg',title='No of Districts: Last 7 days daily avg vaccinated people(18-44)',color='Last 7 days daily avg', color_discrete_map={'Less than 200':'RGB(153,0,0)',
                                 'Between 200-500':'RGB(255,51,51)',
                                 'Between 500-1000':'RGB(255,153,153)',
                                 'Between 1000-2000':'RGB(255,204,204)',
                                 'Between 2000-5000':'RGB(229,255,204)',
                                 'More than 5000':'RGB(0,102,0)'})
fig18.update_traces(hoverinfo='label+percent', textinfo='value')
fig18.add_annotation(text = 'Sachin Pandey @serioussachin, https://covidtika.herokuapp.com & CoWIN,30 May',
                              font_size = 16,
                              showarrow = False,
                              xref = 'paper', x = 0,
                              yref = 'paper', y = -0.3)
st.plotly_chart(fig18)
#left_column_3, right_column_3 = st.beta_columns(2)
#with left_column_3:
    #val = st.selectbox('Select parameter', ['% of 18-44 people vaccinated','Last 7 days avg per 100 people(18-44)'])
    #fig2=dashh(val)
#st.plotly_chart(fig2)
valid_states = list(np.unique(mappingdf["state"].values))
# numdays = st.sidebar.slider('Select Date Range', 0, 100, 10)
#unique_districts = list(mappingdf["district"].unique())
#unique_districts.sort()
left_column_1, right_column_1 = st.beta_columns(2)
with left_column_1:
    state_inp = st.selectbox('Select State', [""] + valid_states)
    if state_inp != "":
        df = filter_column(df, "state", state_inp)
        distf=filter_column(mappingdf,"state", state_inp)
        unique_districts = list(np.unique(distf["district"].values))
        with right_column_1:
            dist_inp = st.selectbox('Select District', [""]+unique_districts)
            if dist_inp != "":
                df = filter_column(df, "district", dist_inp)





st.header(str(sum(df['slots']))+' doses(45 group) went unutilized on 30 May. Doses utilization: '+str(round(sum(df['today'])*100.00/ (sum(df['today'])+sum(df['slots'])),2))+'%. ')#Total vaccinated till date:'+str(sum(df['Total doses til date'])))
df.rename(columns=rename_mapping, inplace=True)
table = deepcopy(df[['District','Unutilized Doses(45+)','Doses Administered(45+)','Last 7 days Daily Avg Vaccination(45+)','People(45+) vaccinated till date','Unutilized Doses(18-44)','Doses Administered(18-44)','Last 7 days Daily Avg Vaccination(18-44)','People(18-44) vaccinated till date']])
table.reset_index(inplace=True, drop=True)

#df.to_csv("map.csv",index=False)

#fig.show()
st.table(table)
st.info('Methodology:calculating unutilized doses from available slots in all districts for the same day from appointment api after 5pm or time duration mentioned and vaccinated people on that day in all districts from report api of CoWIN portal. So it is prone to error due to api cache & cowin usability by districts and states!')
    

pageviews=Pageviews()
pageviews.append('dummy')
pg_views = len(pageviews)
footer(pg_views)
