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

from folium import plugins

from folium.plugins import TimestampedGeoJson















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



df = pd.read_csv('thijsdf.csv')



tab1, tab2, tab3 = st.tabs(["Kaart", "Dog", "Owl"])

with tab1:
  st.header("Choropleth")  

  st_date = st_folium(mapcp,width=520,height=400)
  
  st.header("Tijdlijn kaart")  
  
  st_data = st_folium(timelapsemap,width=520,height=400)

    
    
    
with tab2:
   st.header("Histogrammen")
    
    
    
    
    
    
    
    
    
    
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
with tab3:
   st.header("A cdasfasdfat")



