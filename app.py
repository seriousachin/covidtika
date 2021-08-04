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
td='4 August'
st.set_page_config(layout='wide',
                   #initial_sidebar_state='collapsed',
                   page_icon="https://students.iiserkol.ac.in/~sp13ip016/favicon.ico",
                   page_title="Covid Tika Daily Utilization Tracker Slot Availability")

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def dd():
    df = pd.read_csv("804.csv",index_col = False)
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
    'Total doses til date': 'People (45+) vaccinated till date',
    'center': 'No of not fully utilized centers',
    'state' : 'State',
    'district' : 'District',
    'slots': 'Unutilized doses',
    'today' : 'Doses Administered (45+)',
    'avgdaily': 'Last 7 days Daily Avg Vaccination (45+)',
    'today 18' : 'Doses Administered (18-44)',
    'Total doses til date 18': 'People (18-44) vaccinated till date',
    'avgdaily 18-44': 'Last 7 days Daily Avg Vaccination (18-44)',
    'gratio':'Doses given to Female  per 1000 male',
    'avg people':'Last 7 days Daily Avg Vaccination (18+)',
    'people':'People (18+) vaccinated till date'
    }

st.title('Covid Tika Daily Utilization, Coveragae, Speed Tracker : '+td)
st.write('Tracking daily (non) Utilization, Coverage, Speed, Gender gap, District variations of Covid-19 vaccine doses. Status as on 4 August 2021 , 11:20-11:34PM from CoWIN. ')
st.info('25 June Update: By mistake or knowingly, CoWin Dashboard has stopped giving data on Number of Female/male and Number of 18-44/45+ people being vaccinated, rather they are giving number of doses provided to them. So we are unable to show age, gender specific analysis. We are very sorry for that.')
#dfg = pd.read_csv("map.csv")
#ff=df.sort_values(by='utilization %', ascending=True)
ff=[]
name_stat=np.unique(mappingdf["state"].values)

#141600,80500 ,159433,128953,944709596,357480,289154,,944709596,357480,289154
ppp=[433809,55787608,978264,23055475,72285445,1575709,18908191,646634,15950750,1571030,47072608,20023616,5479377,8731752,26086098,47223245,28740289,220448,60054,55334785,90732824,1969137,2082796,787409,1632268,32024612,1433306,22169872,51330937,463253,55905707,22037645,2759205,150498822,7763594,70953023]
pp=[105669,15897000,372210,8113000,24447000,293781,6955000,222100,5183000,401941,18165000,7177000,2264000,3279000,8395000,18903000,12782000,73245,18467,18965000,35159000,731563,796807,293638,533386,12778000,358310,8924000,17351000,163478,24993000,10372000,987290,47793000,2848000,28410000]
pp1=[181514,23656083,733996,15487657,48850895,503113,12712404,288386,7684565,687704,30700637,13392472,3259129,6122579,16526904,29901024,13879550,125328
,31506,36034217,56232043,1450455,1583181,579270,1054334,18597693,613176,13816067,34233274,323095,32664620,17373309,1949580,99009789,5206552,44278721]
srr=[876,993,938,958,918,818,991,774,868,973,919,879,972,889,948,973,1084,919,946,931,929,985,989,976,931,979,1037,895,928,890,996,985,960,912,963,950]
sr=[868,997,913,953,912,812,995,752,866,973,923,885,983,887,948,971,1099,919,951,933,931,995,989,976,929,985,1047,899,935,883,1000,986,962,910,975,946]
uind={'Todays Doses utilization %':round((sum(df['today'])+sum(df['today 18']))*100.00/ (sum(df['today'])+sum(df['slots'])+sum(df['today 18'])),2),
     '% of 45+ people vaccinated':round(100*sum(df['Total doses til date'])/sum(pp),2),
     'Last 7 days avg per 100 people(45+)':round(100*sum(df['avgdaily'])/sum(pp),2),
      'Days to get 70% coverage(45+) at last 7 days speed':int(max(((0.7*sum(pp))-sum(df['Total doses til date']))/sum(df['avgdaily']),0)),
      
     '% of 18-44 people vaccinated':round(100*sum(df['Total doses til date 18'])/sum(pp1),2),
     'Last 7 days avg per 100 people(18-44)':round(100*sum(df['avgdaily 18-44'])/sum(pp1),2),
     'Today Dose wastage %':round(100*sum(df['wastage'])/(sum(df['today 18'])+sum(df['today'])),2),
     'Female vaccinated per 1000 male':int(round(sum(df['female'])*1000/sum(df['male']),0)),
     'Vaccination Gender Parity Index':round(sum(df['female'])*1000/(sum(df['male'])*944),3),
     'Vaccination District Variation Index':round((min(df['avgdaily 18-44'])+min(df['avgdaily']))/(max(df['avgdaily'])+max(df['avgdaily 18-44'])),4),
     '% of total people(18+) vaccinated':round(100*(sum(df['people']))/(sum(ppp)),2),
     'Last 7 days avg per 100 people(18+)':round(100*(sum(df['avg people']))/(sum(ppp)),2),
     'Days to get 70% coverage(18+) at last 7 days speed':round(max((0.7*(sum(ppp))-sum(df['people']))/(sum(df['avg people'])),0)),
      'Days to get 70% fully vaccinated(18+) at last 7 days speed':round(max((0.7*(sum(ppp))-sum(df['fully']))/(sum(df['avgf'])),0)),
     '% of total people(18+) fully vaccinated':round(100*sum(df['fully'])/(sum(ppp)),2),
     'Todays Priortization Index':round((sum(df['today'])/(sum(pp)-sum(df['Total doses til date'])+sum(df['today'])))/(sum(df['today 18'])/(sum(pp1)-sum(df['Total doses til date 18'])+sum(df['today 18']))),2),
      'Adult population per Active Vaccination Center':int(round((sum(ppp))/sum(df['sites']),0)),
      'Todays avg doses per center':round((sum(df['today 18'])+sum(df['today']))/sum(df['sites']))
     }
for i in range(0,36):
    dfs=df.loc[df['state'] == name_stat[i]]
    if sum(dfs['today'])==0 and sum(dfs['today 18'])==0:
        ff.append({'state':name_stat[i],'Todays Doses utilization %':100,'vaccinated today':sum(dfs['today']),'Last 7 days avg per 100 people(45+)':round(100*sum(dfs['avgdaily'])/pp[i],2),'7 days daily avg':sum(dfs['avgdaily']),'% of 45+ people vaccinated':round(100*sum(dfs['Total doses til date'])/pp[i],2) ,'People vaccinated till date':sum(dfs['Total doses til date']),
 'Days to get 70% coverage(45+) at last 7 days speed':int(max(((0.7*pp[i])-sum(dfs['Total doses til date']))/sum(dfs['avgdaily']),0)), 'vaccinated today 18-44':sum(dfs['today 18']),'Last 7 days avg per 100 people(18-44)':round(100*sum(dfs['avgdaily 18-44'])/pp1[i],2),'7 days daily avg 18-44':sum(dfs['avgdaily 18-44']),'% of 18-44 people vaccinated':round(100*sum(dfs['Total doses til date 18'])/pp1[i],2) ,'People(18-44) vaccinated till date':sum(dfs['Total doses til date 18']),'Female vaccinated per 1000 male':int(round(sum(dfs['female'])*1000/sum(dfs['male']),0)),
                  'Vaccination Gender Parity Index':round(sum(dfs['female'])*1000/(sum(dfs['male'])*sr[i]),3),
     'Vaccination District Variation Index':round((min(dfs['avgdaily 18-44'])+min(dfs['avgdaily']))/(max(dfs['avgdaily'])+max(dfs['avgdaily 18-44'])),4),
                  '% of total people(18+) vaccinated':round(100*(sum(dfs['people']))/(ppp[i]),2),
                  'Last 7 days avg per 100 people(18+)':round(100*(sum(dfs['avg people']))/(ppp[i]),2),
                   'Total People(18+) vaccinated till date':sum(dfs['people']),
                  'Days to get 70% coverage(18+) at last 7 days speed':round(max((0.7*(ppp[i])-sum(dfs['people']))/(sum(dfs['avg people'])),0)),
                   'Days to get 70% fully vaccinated(18+) at last 7 days speed':round(max((0.7*(ppp[i])-sum(dfs['fully']))/(sum(dfs['avgf'])),0)),
     '% of total people(18+) fully vaccinated':round(100*sum(dfs['fully'])/(ppp[i]),2),
     'Todays Priortization Index':0,
                  'Total People vaccinated today':sum(dfs['today'])+sum(dfs['today 18']),
                  'Adult population per Active Vaccination Center':0,
                  'Todays avg doses per center':0})
    elif sum(dfs['slots'])+sum(dfs['today'])==0:
        ff.append({'state':name_stat[i],'Todays Doses utilization %':100,'vaccinated today':sum(dfs['today']),'Last 7 days avg per 100 people(45+)':round(100*sum(dfs['avgdaily'])/pp[i],2),'7 days daily avg':sum(dfs['avgdaily']),'% of 45+ people vaccinated':round(100*sum(dfs['Total doses til date'])/pp[i],2) ,'People vaccinated till date':sum(dfs['Total doses til date']),
 'Days to get 70% coverage(45+) at last 7 days speed':int(max(((0.7*pp[i])-sum(dfs['Total doses til date']))/sum(dfs['avgdaily']),0)), 'vaccinated today 18-44':sum(dfs['today 18']),'Last 7 days avg per 100 people(18-44)':round(100*sum(dfs['avgdaily 18-44'])/pp1[i],2),'7 days daily avg 18-44':sum(dfs['avgdaily 18-44']),'% of 18-44 people vaccinated':round(100*sum(dfs['Total doses til date 18'])/pp1[i],2) ,'People(18-44) vaccinated till date':sum(dfs['Total doses til date 18']),'Female vaccinated per 1000 male':int(round(sum(dfs['female'])*1000/sum(dfs['male']),0)),
                  'Vaccination Gender Parity Index':round(sum(dfs['female'])*1000/(sum(dfs['male'])*sr[i]),3),
     'Vaccination District Variation Index':round((min(dfs['avgdaily 18-44'])+min(dfs['avgdaily']))/(max(dfs['avgdaily'])+max(dfs['avgdaily 18-44'])),4),
                  '% of total people(18+) vaccinated':round(100*(sum(dfs['people']))/(ppp[i]),2),
                 'Last 7 days avg per 100 people(18+)':round(100*(sum(dfs['avg people']))/(ppp[i]),2),
                   'Total People(18+) vaccinated till date':sum(dfs['people']),
                  'Days to get 70% coverage(18+) at last 7 days speed':round(max((0.7*(ppp[i])-sum(dfs['people']))/(sum(dfs['avg people'])),0)),
                   'Days to get 70% fully vaccinated(18+) at last 7 days speed':round(max((0.7*(ppp[i])-sum(dfs['fully']))/(sum(dfs['avgf'])),0)),
     '% of total people(18+) fully vaccinated':round(100*sum(dfs['fully'])/(ppp[i]),2),
     'Todays Priortization Index':max(round((sum(dfs['today'])/(pp[i]-sum(dfs['Total doses til date'])+sum(dfs['today'])))/(sum(dfs['today 18'])/(pp1[i]-sum(dfs['Total doses til date 18'])+sum(dfs['today 18']))),2),0),
                  'Total People vaccinated today':sum(dfs['today'])+sum(dfs['today 18']),
                  'Adult population per Active Vaccination Center':int(round((ppp[i])/sum(dfs['sites']),0)),
                  'Todays avg doses per center':round((sum(dfs['today 18'])+sum(dfs['today']))/sum(dfs['sites']))})
    elif sum(dfs['today 18'])==0:
        ff.append({'state':name_stat[i],'Todays Doses utilization %':round((sum(dfs['today'])+sum(dfs['today 18']))*100.00/ (sum(dfs['today'])+sum(dfs['slots'])+sum(dfs['today 18'])),2),'vaccinated today':sum(dfs['today']),'Last 7 days avg per 100 people(45+)':round(100*sum(dfs['avgdaily'])/pp[i],2),'7 days daily avg':sum(dfs['avgdaily']),'% of 45+ people vaccinated':round(100*sum(dfs['Total doses til date'])/pp[i],2) ,'People vaccinated till date':sum(dfs['Total doses til date']),
 'Days to get 70% coverage(45+) at last 7 days speed':int(max(((0.7*pp[i])-sum(dfs['Total doses til date']))/sum(dfs['avgdaily']),0)), 'Last 7 days avg per 100 people(18-44)':round(100*sum(dfs['avgdaily 18-44'])/pp1[i],2),'7 days daily avg 18-44':sum(dfs['avgdaily 18-44']),'% of 18-44 people vaccinated':round(100*sum(dfs['Total doses til date 18'])/pp1[i],2) ,'People(18-44) vaccinated till date':sum(dfs['Total doses til date 18']),'Female vaccinated per 1000 male':int(round(sum(dfs['female'])*1000/sum(dfs['male']),0)),
                  'Vaccination Gender Parity Index':round(sum(dfs['female'])*1000/(sum(dfs['male'])*sr[i]),3),
     'Vaccination District Variation Index':round((min(dfs['avgdaily 18-44'])+min(dfs['avgdaily']))/(max(dfs['avgdaily'])+max(dfs['avgdaily 18-44'])),4),
                  '% of total people(18+) vaccinated':round(100*(sum(dfs['people']))/(ppp[i]),2),
                  'Last 7 days avg per 100 people(18+)':round(100*(sum(dfs['avg people']))/(ppp[i]),2),
                   'Total People(18+) vaccinated till date':sum(dfs['people']),
                  'Days to get 70% coverage(18+) at last 7 days speed':round(max((0.7*(ppp[i])-sum(dfs['people']))/(sum(dfs['avg people'])),0)),
                   'Days to get 70% fully vaccinated(18+) at last 7 days speed':round(max((0.7*(ppp[i])-sum(dfs['fully']))/(sum(dfs['avgf'])),0)),
     '% of total people(18+) fully vaccinated':round(100*sum(dfs['fully'])/(ppp[i]),2),
   #  'Todays Priortization Index':max(round((sum(dfs['today'])/(pp[i]-sum(dfs['Total doses til date'])+sum(dfs['today'])))/(sum(dfs['today 18'])/(pp1[i]-sum(dfs['Total doses til date 18'])+sum(dfs['today 18']))),2),0),
                  'Total People vaccinated today':sum(dfs['today'])+sum(dfs['today 18']),
                  'Adult population per Active Vaccination Center':int(round((ppp[i])/sum(dfs['sites']),0)),
                  'Todays avg doses per center':round((sum(dfs['today 18'])+sum(dfs['today']))/sum(dfs['sites']))})
    else:
        ff.append({'state':name_stat[i],'Todays Doses utilization %':round((sum(dfs['today'])+sum(dfs['today 18']))*100.00/ (sum(dfs['today'])+sum(dfs['slots'])+sum(dfs['today 18'])),2),'vaccinated today':sum(dfs['today']),'Last 7 days avg per 100 people(45+)':round(100*sum(dfs['avgdaily'])/pp[i],2),'7 days daily avg':sum(dfs['avgdaily']),'% of 45+ people vaccinated':round(100*sum(dfs['Total doses til date'])/pp[i],2) ,'People vaccinated till date':sum(dfs['Total doses til date']),
'Days to get 70% coverage(45+) at last 7 days speed':int(max(((0.7*pp[i])-sum(dfs['Total doses til date']))/sum(dfs['avgdaily']),0)),                   
'vaccinated today 18-44':sum(dfs['today 18']),'Last 7 days avg per 100 people(18-44)':round(100*sum(dfs['avgdaily 18-44'])/pp1[i],2),'7 days daily avg 18-44':sum(dfs['avgdaily 18-44']),'% of 18-44 people vaccinated':round(100*sum(dfs['Total doses til date 18'])/pp1[i],2) ,'People(18-44) vaccinated till date':sum(dfs['Total doses til date 18']),'Female vaccinated per 1000 male':int(round(sum(dfs['female'])*1000/sum(dfs['male']),0)),
                  'Vaccination Gender Parity Index':round(sum(dfs['female'])*1000/(sum(dfs['male'])*sr[i]),3),
     'Vaccination District Variation Index':round((min(dfs['avgdaily 18-44'])+min(dfs['avgdaily']))/(max(dfs['avgdaily'])+max(dfs['avgdaily 18-44'])),4),
                  '% of total people(18+) vaccinated':round(100*(sum(dfs['people']))/(ppp[i]),2),
                  'Last 7 days avg per 100 people(18+)':round(100*(sum(dfs['avg people']))/(ppp[i]),2),
                   'Total People(18+) vaccinated till date':sum(dfs['people']),
                  'Days to get 70% coverage(18+) at last 7 days speed':round(max((0.7*(ppp[i])-sum(dfs['people']))/(sum(dfs['avg people'])),0)),
                   'Days to get 70% fully vaccinated(18+) at last 7 days speed':round(max((0.7*(ppp[i])-sum(dfs['fully']))/(sum(dfs['avgf'])),0)),
     '% of total people(18+) fully vaccinated':round(100*sum(dfs['fully'])/(ppp[i]),2),
     #'Todays Priortization Index':max(round((sum(dfs['today'])/(pp[i]-sum(dfs['Total doses til date'])+sum(dfs['today'])))/(sum(dfs['today 18'])/(pp1[i]-sum(dfs['Total doses til date 18'])+sum(dfs['today 18']))),2),0),
                  'Total People vaccinated today':sum(dfs['today'])+sum(dfs['today 18']),
                  'Adult population per Active Vaccination Center':int(round((ppp[i])/sum(dfs['sites']),0)),
                  'Todays avg doses per center':round((sum(dfs['today 18'])+sum(dfs['today']))/sum(dfs['sites']))})
dfg = pd.DataFrame(ff)
#tdg = deepcopy(dfg[['state','Vaccination District Variation Index']])
#tdg.reset_index(inplace=True, drop=True)
dfg['Vaccination Index']=round(0.5*dfg['% of 45+ people vaccinated']+0.2*dfg['% of 18-44 people vaccinated']+11*dfg['Last 7 days avg per 100 people(45+)']+4*dfg['Last 7 days avg per 100 people(18-44)']+5*dfg['Vaccination Gender Parity Index']+0.25*dfg['% of total people(18+) fully vaccinated'],2)
uind['Vaccination Index']=round(0.50*uind['% of 45+ people vaccinated']+0.2*uind['% of 18-44 people vaccinated']+11*uind['Last 7 days avg per 100 people(45+)']+4*uind['Last 7 days avg per 100 people(18-44)']+5*uind['Vaccination Gender Parity Index']+0.25*uind['% of total people(18+) fully vaccinated'],2)
#dfg['Vaccine Takers Parity Index(45+ vs 18-44 last 7days)'] = np.where(dfg['Last 7 days avg per 100 people(18-44)'] < 1, dfg['Last 7 days avg per 100 people(18-44)']/dfg['Last 7 days avg per 100 people(18-44)'], dfg['Last 7 days avg per 100 people(18-44)']/dfg['Last 7 days avg per 100 people(18-44)'])
#indd
dfg['Add Doses']=(dfg['People vaccinated till date']*70/dfg['% of 45+ people vaccinated'])-dfg['People vaccinated till date']
ssss=dfg[['state','Add Doses']]




for col in dfg.columns:
    dfg[col] = dfg[col].astype(str)

dfg['text'] = dfg['state'] + '<br>' +\
'Today Doses Utilization % : ' + dfg['Todays Doses utilization %'] +  '<br>' +\
'Vaccinated today:' + dfg['vaccinated today'] +  '<br>' +\
'Last 7 days avg per 100 people(45+):' + dfg['Last 7 days avg per 100 people(45+)'] + '<br>' +\
'Last 7 days Daily Avg Vaccination:' + dfg['7 days daily avg'] + '<br>' +\
'% of 45+ people vaccinated:' + dfg['% of 45+ people vaccinated'] + '<br>' +\
'People vaccinated till date:' + dfg['People vaccinated till date']
dfg['text18'] = dfg['state'] + '<br>' +\
'Vaccinated today 18-44:' + dfg['vaccinated today 18-44'] +  '<br>' +\
'Last 7 days avg per 100 people(18-44):' + dfg['Last 7 days avg per 100 people(18-44)'] + '<br>' +\
'Last 7 days Daily Avg Vaccination 18-44:' + dfg['7 days daily avg 18-44'] + '<br>' +\
'% of 18-44 people vaccinated:' + dfg['% of 18-44 people vaccinated'] + '<br>' +\
'People(18-44) vaccinated till date:' + dfg['People(18-44) vaccinated till date']
dfg['gen'] = dfg['state'] + '<br>' +\
'% of total people(18+) vaccinated :'+dfg['% of total people(18+) vaccinated']+ '<br>' +\
'Total People vaccinated today:'+dfg['Total People vaccinated today']+ '<br>' +\
'Last 7 days avg per 100 people(18+) :'+dfg['Last 7 days avg per 100 people(18+)']+ '<br>' +\
'Total People(18+) vaccinated till date :'+dfg['Total People(18+) vaccinated till date']+ '<br>' +\
'% of total people(18+) fully vaccinated: '+dfg['% of total people(18+) fully vaccinated']+ '<br>' +\
'Doses given to Female  per 1000 male : ' + dfg['Female vaccinated per 1000 male']+ '<br>' +\
'Vaccination Gender Parity Index: '+dfg['Vaccination Gender Parity Index']+ '<br>' +\
'Adult population per Active Vaccination Center:'+dfg['Adult population per Active Vaccination Center']+ '<br>' +\
'Todays avg doses per center: '+dfg['Todays avg doses per center']
#'Doses given to Female  per 1000 male : ' + dfg['Female vaccinated per 1000 male']+ '<br>' +\

#name_stat


def dashh(val):
    if (val=='% of 18-44 people vaccinated' or val=='Last 7 days avg per 100 people(18-44)' or val=='Todays Doses(18-44) utilization %' ):
        dfg['text']=dfg['text18']
    if (val=='Female vaccinated per 1000 male' or val=='Vaccination Gender Parity Index' or val=='% of total people(18+) vaccinated' or val=='Last 7 days avg per 100 people(18+)' or val=='Days to get 70% coverage(18+) at last 7 days speed' or val=='% of total people(18+) fully vaccinated' or val=='Vaccination Index' or val=='Todays Priortization Index' or val=='Adult population per Active Vaccination Center' or val=='Todays avg doses per center' or val=='Todays Doses utilization %'):
        dfg['text']=dfg['gen']
    if val=='Days to get 70% coverage(45+) at last 7 days speed' or val=='Days to get 70% coverage(18+) at last 7 days speed' or val=='Adult population per Active Vaccination Center' or val=='Days to get 70% fully vaccinated(18+) at last 7 days speed':
        cs=True
    else:
        cs=False
    if val=='Vaccination Index':
        vi='Vaccination Index is calculated'+  '<br>' +\
        'on coverage & speed  in'+  '<br>' +\
        '45+(50%) & 18-44(20%) group, '+  '<br>' +\
        'Gender Parity(5%) & Fully Vaccinated(25%) '
    elif val=='Todays Priortization Index':
        vi='Todays Priortization Index is calculated'+  '<br>' +\
        'as % of 45+ unvaccinated population '+  '<br>' +\
        'vaccinated today to % of 18-44 '+  '<br>' +\
        'unvaccinated population vaccinated today'
    else:
        vi=''
    if val=='Vaccination Gender Parity Index':
        claim='Based on doses given to Female per 1000'+  '<br>' +\
        'doses to Male normalized to sex ratio among 18+'
    elif val=='% of total people(18+) fully vaccinated' or val=='Todays avg doses per center' or val=='Days to get 70% fully vaccinated(18+) at last 7 days speed':
        claim=''
    else:
        claim='*Data based on atleast single dose vaccinated people.'
    
        
    zz=dfg[val]    
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
        #below=True,
        #if val=='Today Dose wastage %':
        reversescale=cs,
        colorbar=dict(
            title={'text': val},

            #thickness=15,
            len=0.35,
            bgcolor='rgba(255,255,255,0.6)',

            tick0=0,
            dtick=max(dfg[val].astype(float))/10.0,
            

            xanchor='left',
            x=0.01,
            yanchor='bottom',
            y=0.05
        )
    ))
    #fig1.update_traces(name=dfg[val], selector=dict(type='choropleth'))

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
            text=val+" (All India): "+str(uind[val]),
            xanchor='center',
            x=0.5,
            yref='paper',
            yanchor='bottom',
            y=0.93,
            pad={'b': 10}
        ),
         annotations = [dict(
        x=0.85,
        y=0.15,
        xref='paper',
        yref='paper',
        text='Sachin Pandey @serioussachin,'+ '<br>' +\
             'https://covidtika.herokuapp.com '+ '<br>' +\
             'CoWIN, '+td+'. 18+ population data'+ '<br>' +\
             ' from GoI Affidavit in Supreme Court'+ '<br>' +\
             ''+ '<br>' +\
             ''+vi,
        showarrow = False
    ), dict(
        x=0.2,
        y=0.06,
        xref='paper',
        yref='paper',
        text='Lakshadweep: '+zz[18],
        showarrow = False
    )
        , dict(
        x=0.85,
        y=0.93,
        xref='paper',
        yref='paper',
        text=claim,
        showarrow = False
    )], 
        margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
        height=750,
        width=750,
        dragmode=False 
    )
    return fig1
fig1=dashh('Todays Doses utilization %')
left_column_2, right_column_2 = st.beta_columns(2)
with left_column_2:
    val = st.selectbox('Select parameter', ['% of total people(18+) vaccinated','Last 7 days avg per 100 people(18+)','Days to get 70% coverage(18+) at last 7 days speed','% of total people(18+) fully vaccinated','Days to get 70% fully vaccinated(18+) at last 7 days speed','Adult population per Active Vaccination Center','Vaccination Gender Parity Index','Todays avg doses per center','Todays Doses utilization %'])
#% of 45+ people vaccinated','Last 7 days avg per 100 people(45+)','Days to get 70% coverage(45+) at last 7 days speed','Todays Doses(45+) utilization %','% of 18-44 people vaccinated','Last 7 days avg per 100 people(18-44)','Todays Doses(18-44) utilization %','Todays Priortization Index','Vaccination Gender Parity Index','Female vaccinated per 1000 male', ,'Vaccination Index' 'Todays Doses utilization %'  
    fig1=dashh(val)
st.plotly_chart(fig1)
ad=[]
ad.append({'Last 7 days daily avg':'Less than 500',
     'No of Districts':df[df['avg people']<500].count()[1]})
ad.append({'Last 7 days daily avg':'Between 500-1000',
     'No of Districts':df[df['avg people']<1000 ].count()[1]-df[df['avg people']<=500].count()[1]})
ad.append({'Last 7 days daily avg':'Between 1000-2000',
     'No of Districts':df[df['avg people']<2000].count()[1]-df[df['avg people']<=1000].count()[1]})
ad.append({'Last 7 days daily avg':'Between 2000-5000',
     'No of Districts':df[df['avg people']<5000 ].count()[1]-df[df['avg people']<=2000].count()[1]})
ad.append({'Last 7 days daily avg':'Between 5000-10000',
     'No of Districts':df[df['avg people']<10000 ].count()[1]-df[df['avg people']<=5000].count()[1]})
ad.append({'Last 7 days daily avg':'Between 10000-20000',
     'No of Districts':df[df['avgdaily']<20000 ].count()[1]-df[df['avg people']<=10000].count()[1]})
ad.append({'Last 7 days daily avg':'More than 20000',
     'No of Districts':df[df['avg people']>=20000 ].count()[1]})
ad=pd.DataFrame(ad)
xxx=df[df['Total doses til date 18']>df['Total doses til date']].count()[1]
#xxx
fig = px.pie(ad,values='No of Districts', names='Last 7 days daily avg',title='No of Districts: Last 7 days daily avg vaccinated people(18+)',color='Last 7 days daily avg', color_discrete_map={'Less than 500':'RGB(153,0,0)',
                                 'Between 500-1000':'RGB(255,51,51)',
                                 'Between 1000-2000':'RGB(255,153,153)',
                                 'Between 2000-5000':'RGB(255,204,204)',
                                 'Between 5000-10000':'RGB(229,255,204)',
                                 'Between 10000-20000':'RGB(0,255,0)',
                                 'More than 20000':'RGB(0,102,0)'})
fig.update_traces(hoverinfo='label+percent', textinfo='value')
fig.add_annotation(text = 'Sachin Pandey @serioussachin, https://covidtika.herokuapp.com & CoWIN, '+td,
                              font_size = 10,
                              showarrow = False,
                              xref = 'paper', x = 0.5,
                              yref = 'paper', y = -0.05)
fig.update_layout(title_x=0.5)
#col1,col2 = st.beta_columns(2)
#with col1:
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
ad18.append({'Last 7 days daily avg':'Between 5000-10000',
     'No of Districts':df[df['avgdaily 18-44']<10000 ].count()[1]-df[df['avgdaily 18-44']<=5000].count()[1]})
ad18.append({'Last 7 days daily avg':'More than 10000',
     'No of Districts':df[df['avgdaily 18-44']>=10000 ].count()[1]})
ad18=pd.DataFrame(ad18)
adg=[]
adg.append({'Female vaccinated per 1000 male':'Less than 600',
     'No of Districts':df[df['gratio']<600].count()[1]})
adg.append({'Female vaccinated per 1000 male':'Between 600-700',
     'No of Districts':df[df['gratio']<700].count()[1]-df[df['gratio']<=600].count()[1]})
adg.append({'Female vaccinated per 1000 male':'Between 700-800',
     'No of Districts':df[df['gratio']<800 ].count()[1]-df[df['gratio']<=700].count()[1]})
adg.append({'Female vaccinated per 1000 male':'Between 800-900',
     'No of Districts':df[df['gratio']<900 ].count()[1]-df[df['gratio']<=800].count()[1]})
adg.append({'Female vaccinated per 1000 male':'Between 900-950',
     'No of Districts':df[df['gratio']<950 ].count()[1]-df[df['gratio']<=900].count()[1]})
adg.append({'Female vaccinated per 1000 male':'Between 950-1000',
     'No of Districts':df[df['gratio']<1000 ].count()[1]-df[df['gratio']<=950].count()[1]})
adg.append({'Female vaccinated per 1000 male':'More than 1000',
     'No of Districts':df[df['gratio']>=1000 ].count()[1]})
adg=pd.DataFrame(adg)

#fig = px.bar(ad, x='Last 7 days daily avg', y='No of Districts')
#fig.update_traces(textposition='outside')

fig18 = px.pie(ad18,values='No of Districts', names='Last 7 days daily avg',title='No of Districts: Last 7 days daily avg vaccinated people(18-44)',color='Last 7 days daily avg', color_discrete_map={'Less than 200':'RGB(153,0,0)',
                                 'Between 200-500':'RGB(255,51,51)',
                                 'Between 500-1000':'RGB(255,153,153)',
                                 'Between 1000-2000':'RGB(255,204,204)',
                                 'Between 2000-5000':'RGB(229,255,204)',
                                 'Between 5000-10000':'RGB(0,255,0)',
                                 'More than 10000':'RGB(0,102,0)'})
fig18.update_traces(hoverinfo='label+percent', textinfo='value')
fig18.add_annotation(text = 'Sachin Pandey @serioussachin, https://covidtika.herokuapp.com & CoWIN, '+td,
                              font_size = 10,
                              showarrow = False,
                              xref = 'paper', x = 0.5,
                              yref = 'paper', y = -0.05)
fig18.update_layout(title_x=0.5)
#with col2:
#st.plotly_chart(fig18)
figg = px.pie(adg,values='No of Districts', names='Female vaccinated per 1000 male',title='No of Districts: Female vaccinated per 1000 male',color='Female vaccinated per 1000 male', color_discrete_map={'Less than 600':'RGB(153,0,0)',
                                 'Between 600-700':'RGB(255,51,51)',
                                 'Between 700-800':'RGB(255,153,153)',
                                 'Between 800-900':'RGB(255,204,204)',
                                 'Between 900-950':'RGB(229,255,204)',
                                 'Between 9500-1000':'RGB(0,255,0)',
                                 'More than 1000':'RGB(0,102,0)'})
figg.update_traces(hoverinfo='label+percent', textinfo='value')
figg.add_annotation(text = 'Sachin Pandey @serioussachin, https://covidtika.herokuapp.com & CoWIN, '+td,
                              font_size = 10,
                              showarrow = False,
                              xref = 'paper', x = 0.5,
                              yref = 'paper', y = -0.05)
figg.update_layout(title_x=0.5)
#st.plotly_chart(figg)
#left_column_3, right_column_3 = st.beta_columns(2)
#with left_column_3:
    #val = st.selectbox('Select parameter', ['% of 18-44 people vaccinated','Last 7 days avg per 100 people(18-44)'])
    #fig2=dashh(val)
#st.plotly_chart(fig2)
st.header('State and District wise Data')
valid_states = list(np.unique(mappingdf["state"].values))
# numdays = st.sidebar.slider('Select Date Range', 0, 100, 10)
#unique_districts = list(mappingdf["district"].unique())
#unique_districts.sort()
left_column_1, center_column_1,right_column_1 = st.beta_columns(3)
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





st.write(str(sum(df['slots']))+'('+str(sum(df['paid slot']))+' paid slots) doses went unutilized on '+td)#Total vaccinated till date:'+str(sum(df['Total doses til date'])))
df.rename(columns=rename_mapping, inplace=True)
with center_column_1:
    sort_inp = st.selectbox('Sort by', ['Unutilized doses','Doses Administered (45+)','Doses Administered (18-44)','Last 7 days Daily Avg Vaccination (18+)','People (18+) vaccinated till date','Doses given to Female  per 1000 male'] )
    if sort_inp != "":
        df= df.sort_values(by=sort_inp, ascending=False)
#'Last 7 days Daily Avg Vaccination (45+)','People (45+) vaccinated till date','Last 7 days Daily Avg Vaccination (18-44)','People (18-44) vaccinated till date','Female vaccinated per 1000 male'    
table = deepcopy(df[['District','Unutilized doses','Doses Administered (45+)','Doses Administered (18-44)','Last 7 days Daily Avg Vaccination (18+)','People (18+) vaccinated till date','Doses given to Female  per 1000 male']])
#,'Unutilized doses''District','Unutilized Doses (45+)','Doses Administered (45+)','Last 7 days Daily Avg Vaccination (45+)','People (45+) vaccinated till date','Unutilized Doses (18-44)','Doses Administered (18-44)','Last 7 days Daily Avg Vaccination (18-44)','People (18-44) vaccinated till date','Female vaccinated per 1000 male'

table.reset_index(inplace=True, drop=True)
xxx=df.describe()
#xxx
st.table(table)
st.info('Methodology:calculating unutilized doses from available slots in all districts for the same day from appointment api after 10pm or time duration mentioned and vaccinated people on that day in all districts from report api of CoWIN portal. So it is prone to error due to api cache & cowin usability by districts and states! Vaccination Gender parity Index= (Doses given to female per 1000 Male)/(Female population per 1000 male among 18+ as on 2021 projected from census 2011)')
    

pageviews=Pageviews()
pageviews.append('dummy')
pg_views = len(pageviews)
footer(pg_views)
