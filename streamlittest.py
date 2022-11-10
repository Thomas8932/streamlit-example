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
                'fillColor': 'black'],
                'fillOpacity': 1,
                'stroke': 'true',
                'radius': 1
            }
        }
    }
    features.append(feature)

timelapsemap = folium.Map(control_scale=True, zoom_start=1,location=[20, 10],width=520,height=400)

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

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")

with tab2:
   st.header("A dog")

with tab3:
   st_data = st_folium(timelapsemap,width=520,height=400)






