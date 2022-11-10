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



sharktotal1 = pd.read_csv('sharktotal1.csv')

sharktotal1 = sharktotal1[sharktotal1['Year'] > 1969]
sharktotal1['Year'] = sharktotal1['Year'].replace(3019.0,2019.0)
sharktotal1['Year'] = pd.to_datetime(arg=sharktotal1['Year'],format="%Y")

sharktotal1 = sharktotal1[sharktotal1['LAT'] != 'geen locatie bekend']
sharktotal1 = sharktotal1[sharktotal1['LAT'] != 'error']
sharktotal1 = sharktotal1[sharktotal1['LAT'] != 'alleen land bekend']
sharktotal1 = sharktotal1[sharktotal1['LAT'] != '1 van de 2 is nan']
sharktotal1 = sharktotal1[sharktotal1['LAT'] != 'geen locatie bekend']
sharktotal1 = sharktotal1[sharktotal1['LAT'] != 'error']

sharktotal1[['LAT','LONG']] = sharktotal1[['LAT','LONG']].astype(float)





features = []
for _, row in sharktotal1.iterrows():
    feature = {
        'type': 'Feature',
        'geometry': {
            'type':'Point', 
            'coordinates':[row['LONG'],row['LAT']]
        },
        'properties': {
            'time': row['Year'].date().__str__(),
            'style': {'color' : 'red'},
            'icon': 'circle',
            'iconstyle':{
                'fillColor': 'red',
                'fillOpacity': 1,
                'stroke': 'true',
                'radius': 1
            }
        }
    }
    features.append(feature)



coords_belgium=[30, 10]
timelapsemap = folium.Map(location=coords_belgium, control_scale=True, zoom_start=1.5)


TimestampedGeoJson(
    {'type': 'FeatureCollection',
    'features': features}
    , period='P1Y'
    , add_last_point=True
    , auto_play=False
    , loop=False
    , max_speed=1
    , loop_button=True
    , date_options='YYYY'
    , time_slider_drag_update=True
).add_to(timelapsemap)


#timelapsemap

# sharkjason = create_geojson_features(sharktotal1)
# make_map(sharkjason)


st_data = st_folium(timelapsemap,width=2000)








