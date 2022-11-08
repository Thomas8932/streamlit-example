# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:02:46 2022

@author: lpnnr
"""

import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import geopandas as gpd
import numpy as np




coordinaten = pd.read_csv('plekcoords.csv',index_col=0)
#coordinaten = coordinaten.loc[1:2000]










# from branca.element import Template, MacroElement

# template = """
# {% macro html(this, kwargs) %}

# <!doctype html>
# <html lang="en">
# <head>
#   <meta charset="utf-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1">
#   <title>jQuery UI Draggable - Default functionality</title>
#   <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

#   <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
#   <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
#   <script>
#   $( function() {
#     $( "#maplegend" ).draggable({
#                     start: function (event, ui) {
#                         $(this).css({
#                             right: "auto",
#                             top: "auto",
#                             bottom: "auto"
#                         });
#                     }
#                 });
# });

#   </script>
# </head>
# <body>

 
# <div id='maplegend' class='maplegend' 
#     style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
#      border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
     
# <div class='legend-title'>Aantal laadpalen per cluster</div>
# <div class='legend-scale'>
#   <ul class='legend-labels'>
#     <li><span style='background:orange;opacity:0.7;'></span>100+</li>
#     <li><span style='background:yellow;opacity:0.7;'></span>10-99</li>
#     <li><span style='background:green;opacity:0.7;'></span>0-9</li>

#   </ul>
# </div>
# </div>
 
# </body>
# </html>

# <style type='text/css'>
#   .maplegend .legend-title {
#     text-align: left;
#     margin-bottom: 5px;
#     font-weight: bold;
#     font-size: 90%;
#     }
#   .maplegend .legend-scale ul {
#     margin: 0;
#     margin-bottom: 5px;
#     padding: 0;
#     float: left;
#     list-style: none;
#     }
#   .maplegend .legend-scale ul li {
#     font-size: 80%;
#     list-style: none;
#     margin-left: 0;
#     line-height: 18px;
#     margin-bottom: 2px;
#     }
#   .maplegend ul.legend-labels li span {
#     display: block;
#     float: left;
#     height: 16px;
#     width: 30px;
#     margin-right: 5px;
#     margin-left: 0;
#     border: 1px solid #999;
#     }
#   .maplegend .legend-source {
#     font-size: 80%;
#     color: #777;
#     clear: both;
#     }
#   .maplegend a {
#     color: #777;
#     }
# </style>
# {% endmacro %}"""



st.header("test 2")


# m = folium.Map(location=[52,5])



# for a,b in coordinaten.iterrows():
#     try:
            
#         folium.Marker(location=[b['LAT'], b['LONG']]).add_to(m)
#     except:
#         asdf = []



# macro = MacroElement() 
# macro._template = Template(template)
# m.get_root().add_child(macro)



# st_data = st_folium(m,width=725)






countriesgeometry = gpd.read_file('countriesgeometry.geojson')
sharktotal1 = pd.read_csv('sharktotal1.csv')



landhoeveelheden = sharktotal1.groupby('Country')[['Country']].count()

landhoeveelheden.rename(columns = {'Country':'hoeveelheid'}, inplace = True)

landhoeveelheden = landhoeveelheden.sort_values(by='hoeveelheid',ascending=False)

landhoeveelheden.reset_index(inplace=True)
landhoeveelheden['Country'] = landhoeveelheden['Country'].str.lower()
countriesgeometry['ADMIN'] = countriesgeometry['ADMIN'].str.lower()


landhoeveelheden['hoeveelheid2'] = np.log10(landhoeveelheden['hoeveelheid'])




mapc = folium.Map(zoom_control=False,
               scrollWheelZoom=False,
               dragging=False,
              zoom_start=1,
               location=[20, 10],
               width=520,
               height=400,
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
).add_to(mapc)

mapc



st_data = st_folium(mapc,width=725)













