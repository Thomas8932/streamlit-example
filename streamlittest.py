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




timelapsemap = folium.Map(location=coords_belgium, control_scale=True, zoom_start=1.5)

st_data = st_folium(timelapsemap,width=725)











