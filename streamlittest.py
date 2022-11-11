# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:41:45 2022

@author: t
"""


import folium
import pandas as pd
import geopandas as gpd
import numpy as np
import streamlit as st
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import statsmodels.api as sm



import plotly.express as px
import plotly.graph_objects as go

from folium import plugins

from folium.plugins import TimestampedGeoJson

################################################################################################################################################

countriesgeometry = gpd.read_file('countriesgeometry.geojson')
landhoeveelheden = pd.read_csv('landhoeveelheden.csv')
countriesgeometry['ADMIN'] = countriesgeometry['ADMIN'].str.lower()

mapcp = folium.Map(zoom_control=False,
               scrollWheelZoom=False,
               dragging=False,
              zoom_start=1,
               location=[20, 10],
               width=620,
               height=500,
               tiles='cartodbpositron')

folium.Choropleth(
    geo_data=countriesgeometry,
    name="choropleth",
    data=landhoeveelheden,
    columns=["Country",'hoeveelheid2'],
    fill_color="YlGn",
    fill_opacity=1,
    line_opacity=.9,
    nan_fill_color="purple",
    key_on ='feature.properties.ADMIN',
    
    legend_name="Haai aanvallen (log schaal)",
).add_to(mapcp)

################################################################################################################################################

sharktotal4 = pd.read_csv('timelapsedataframe.csv')
sharktotal4['Year'] = pd.to_datetime(arg=sharktotal4['Year'])

features = []
for _, row in sharktotal4.iterrows():
    feature = {
        'type': 'Feature',
        'geometry': {
            'type':'Point', 
            'coordinates':[row['LONG'],row['LAT']]
        },
        'properties': {
            'time': row['Year'].date().__str__(),
            'style': {'color' : row['doodkleur']},
            'icon': 'circle',
            'iconstyle':{
                'fillColor': 'black',
                'fillOpacity': 1,
                'stroke': 'true',
                'radius': 1
            }
        }
    }
    features.append(feature)

timelapsemap = folium.Map(zoom_control=False,scrollWheelZoom=False,dragging=False,control_scale=True, zoom_start=1,location=[20, 10],width=520,height=400)

TimestampedGeoJson(
    {'type': 'FeatureCollection',
    'features': features}
    , period='P1Y'
    , add_last_point=True
    , auto_play=False
    , loop=False
    , max_speed=1
    , loop_button=False
    , date_options='YYYY'
    , time_slider_drag_update=True
).add_to(timelapsemap)

################################################################################################################################################

df = pd.read_csv('thijsdf.csv')






################################################################################################################################################

Alle_Landen= df
USA = df[df['Country'] == 'USA']
AUSTRALIA = df[df['Country'] == 'AUSTRALIA']
SOUTH_AFRICA = df[df['Country'] == 'SOUTH AFRICA']
NEW_ZEALAND = df[df['Country'] == 'NEW ZEALAND']
PAPUA_NEW_GUINEA = df[df['Country'] == 'PAPUA NEW GUINEA']
BRAZIL = df[df['Country'] == 'BRAZIL']
BAHAMAS = df[df['Country'] == 'BAHAMAS']

###############

code1 = '''
x = 0
coordsLAT = []
coordsLONG = []
methode = []
for a,b in aanvalplek.iterrows():
    time.sleep(1.01)
    x = x + 1
    print(x)
    try:        
        if not pd.isna(b['Location']):
            geolocator = Nominatim(user_agent="hoenaam@xs4all.nl")
            location = geolocator.geocode(b['Location'])
            coordsLAT.append(location.latitude)
            coordsLONG.append(location.longitude)
            print([location.latitude, location.longitude])
            methode.append('locatie')
        elif not pd.isna(b['Area']):
            geolocator = Nominatim(user_agent="hoenaam@xs4all.nl")
            location = geolocator.geocode(b['Area'])
            coordsLAT.append(location.latitude)
            coordsLONG.append(location.longitude)
            print([location.latitude, location.longitude])
            methode.append('area')
        else:
            if pd.isna(b['Country']):
                coordsLAT.append('geen locatie bekend')
                coordsLONG.append('geen locatie bekend')
                methode.append('error')
            else:
                coordsLAT.append('alleen land bekend')
                coordsLONG.append('alleen land bekend')
                methode.append('error')
    except:
        try:   
            if not (pd.isna(b['Location']) and pd.isna(b['Area'])):
                time.sleep(1.01)
                geolocator = Nominatim(user_agent="hoenaam@xs4all.nl")
                AreaLoc = b['Area'] + ',' + b['Location']
                location = geolocator.geocode(AreaLoc)
                coordsLAT.append(location.latitude)
                coordsLONG.append(location.longitude)
                print([location.latitude, location.longitude])
                methode.append('arealoc')
            else:
                raise ValueError('1 van de 2 is nan')
        except:
            try:
                if not (pd.isna(b['Location']) and pd.isna(b['Country'])):
                    time.sleep(1.01)
                    geolocator = Nominatim(user_agent="hoenaam@xs4all.nl")
                    countryloc = b['Country'] + ',' + b['Location']
                    location = geolocator.geocode(countryloc)
                    coordsLAT.append(location.latitude)
                    coordsLONG.append(location.longitude)
                    print([location.latitude, location.longitude])
                    methode.append('countryloc')
                else:
                    raise ValueError('1 van de 2 is nan')
            except:
                try:
                    if not (pd.isna(b['Country']) and pd.isna(b['Area'])):
                        time.sleep(1.01)
                        geolocator = Nominatim(user_agent="hoenaam@xs4all.nl")
                        countryarea = b['Country'] + ',' + b['Area']
                        location = geolocator.geocode(countryarea)
                        coordsLAT.append(location.latitude)
                        coordsLONG.append(location.longitude)
                        print([location.latitude, location.longitude])
                        methode.append('countryarea')
                    else:
                        raise ValueError('1 van de 2 is nan')
                except:
                    coordsLAT.append('error')
                    coordsLONG.append('error')
                    methode.append('error')'''

code2 = '''
api = KaggleApi()
api.authenticate()

api.dataset_download_file('thedevastator/shark-attacks-the-risks-of-coastal-water-activit',
                          file_name='GSAF5.xls.csv')

import zipfile

with zipfile.ZipFile('GSAF5.xls.csv.zip', 'r') as zipref:
    zipref.extractall('./Datasets')'''

code3 = '''
df['Name']= df['Name'].dropna(how=any)
poging = df.Name.str.split(" ",expand=True,)
df['voornaam'] = poging[0]
df = df.reset_index(drop=True)

d = gender.Detector()
geslacht= []

for i in range(0, len(df)):
    geslacht.append(d.get_gender(df['voornaam'][i]))
    
df['geslacht'] = geslacht

male = pd.Series(np.array(["male","boy","2 males","male,","Mr.","mostly_male"]))
female = pd.Series(np.array(["female","female,","Mrs.","Mrs","Miss","woman","mostly_female"]))


for i in range(0,len(df['geslacht'])):
    if male.str.contains(df['voornaam'][i],regex=False).any():
        df['geslacht'][i] = 'male'
    elif female.str.contains(df['voornaam'][i],regex=False).any():
        df['geslacht'][i] = 'female'
    elif df['geslacht'][i] == 'mostly_male':
        df['geslacht'][i] = 'male'
    elif df['geslacht'][i] == "mostly_female":
        df['geslacht'][i] = 'female'
    elif df['geslacht'][i] == "andy":
        df['geslacht'][i] = 'unknown'
    else:   
        df['geslacht'][i] = df['geslacht'][i]
'''

 


################################################################################################################################################

tab1, tab2, tab3,tab4 = st.tabs(["Kaart", "Activiteit", "Per land",'Code'])
################################################################################################################################################




with tab1:
  st.header("Choropleth")  

  st_date = st_folium(mapcp,width=520,height=400)
  
  st.header("Tijdlijn kaart")  
  
  st_data = st_folium(timelapsemap,width=520,height=400)

################################################################################################################################################
    
    
with tab2:
   st.header("Activiteiten")
    
   newnames = {'Y':'Dodelijk', 'N': 'Niet dodelijk'}
   fig1 = px.histogram(df, x = df['Activity_cat'], color = df['Fatal (Y/N)'],
                     labels={
                       "Activity_cat": "Activiteit"
                  },
                  title='Aantal aanvallen per activiteit').update_xaxes(categoryorder="total descending")
   fig1.update_yaxes(title='Aantal aanvallen')
   fig1.update_layout(legend_title="Uitkomst aanval")
   fig1.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                        legendgroup = newnames[t.name],
                                        hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))
   st.plotly_chart(fig1)
    
################################################################################################################################################
  
  
with tab3:
  st.header("Per land")
  datasetlijst = ["Alle_Landen", "USA", "AUSTRALIA", "SOUTH_AFRICA", "NEW_ZEALAND", "PAPUA_NEW_GUINEA","BRAZIL","BAHAMAS"]
  dataframeselect = st.selectbox('Welke set wil je zien', datasetlijst, key='dataframe select')
  
  if (dataframeselect == datasetlijst[0]) & (dataframeselect != ""):
          display_data = df.copy()
          country = 'All'
  elif (dataframeselect == datasetlijst[1]) & (dataframeselect != ""):
          display_data = USA.copy()
          country = 'USA'
  elif (dataframeselect == datasetlijst[2]) & (dataframeselect != ""):
          display_data = AUSTRALIA.copy()
          country = 'AUSTRALIA'
  elif (dataframeselect == datasetlijst[3]) & (dataframeselect != ""):
          display_data = SOUTH_AFRICA.copy()
          country = 'SOUTH_AFRICA'
  elif (dataframeselect == datasetlijst[4]) & (dataframeselect != ""):
          display_data = NEW_ZEALAND.copy()
          country = 'NEW_ZEALAND'
  elif (dataframeselect == datasetlijst[5]) & (dataframeselect != ""):
          display_data = PAPUA_NEW_GUINEA.copy()
          country = 'PAPUA_NEW_GUINEA'
  elif (dataframeselect == datasetlijst[4]) & (dataframeselect != ""):
          display_data = BRAZIL.copy()
          country = 'BRAZIL'
  elif (dataframeselect == datasetlijst[5]) & (dataframeselect != ""):
          display_data = BAHAMAS.copy()
          country = 'BAHAMAS' 

  display_box0 = display_data[['Year','Attack','Fatal (Y/N)']] 
  display_box = display_box0.groupby(['Year','Fatal (Y/N)'])['Attack'].sum()
  display_box = display_box.to_frame()
  display_box= display_box.reset_index()
  display_box.head()

 
  fig2 = px.box(display_box, color= 'Fatal (Y/N)', y = 'Attack', title="Verhouding dodelijke en niet dodelijke aanvallen")
  fig2.update_layout( yaxis_title="Aantal aanvallen")
  fig2.update_layout(legend_title="Uitkomst aanval")
  fig2.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                        legendgroup = newnames[t.name],
                                        hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))
  
  ###############################################################################################################################################
  
  st.plotly_chart(fig2)
  
  ###############################################################################################################################################
  
  display_line0 = display_data[['Year','Attack']] 
  display_line = display_line0.groupby('Year')['Attack'].sum()
  display_line = display_line.to_frame()
  display_line = display_line.reset_index()
  
  
  
  
  fig3 = px.line(display_line, x="Year", y="Attack", 
                  labels={
                       "Year": "Jaar",
                       "Attack": "Aantal aanvallen"
                  },
                  title='Aantal aanvallen per jaar')
  fig3.update_xaxes(rangeslider_visible=True)
  st.plotly_chart(fig3)
  
  ###############################################################################################################################################

  fig4 = px.scatter(display_box,x= 'Year', y='Attack',symbol="diamond", color='Fatal (Y/N)',trendline='ols',labels={"Year": "Jaar","Attack": "Aantal aanvallen"},title='Aantal aanvallen per jaar')
  fig4.update_layout(legend_title="Uitkomst aanval")
  fig4.for_each_trace(lambda t: t.update(name = newnames[t.name],legendgroup = newnames[t.name],hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))
  fig4.update_xaxes(rangeslider_visible=True)
  st.plotly_chart(fig4)    
  
  
  
 
###############################################################################################################################################
  
with tab4:
  st.header('API')
  
  
  st.code(code2, language="python")
  st.header('Coordinaten vinden')
  st.code(code1, language="python")
  st.header('Gender')
  st.code(code3, language="python")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


