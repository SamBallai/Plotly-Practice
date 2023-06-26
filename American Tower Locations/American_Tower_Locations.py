import pandas as pd
import geopandas as gpd
import plotly.express as px
import openpyxl

file = pd.read_excel('americantower_backup-power_site-list.xls')

#Creates a scatterplot of American Tower locations
def show_locations_on_map(df):
    
    #Create the scatterplot
    fig = px.scatter_geo(
        df, 
        lat = 'Latitude', 
        lon = 'Longitude', 
        hover_data = df.columns.tolist()
        )
    #Zoom in on America
    fig.update_geos(fitbounds="locations")
    #Adjusting title and offsets
    fig.update_layout(height = 500, margin = {"r":0,"t":50,"l":0,"b":0})
    fig.update_layout(title = 'American Tower - Tower Locations', title_x = 0.5)
    fig.show()

#Creates a histogram of Ground Elevetions 
def create_histogram(df):
    fig = px.histogram(df, x="Ground Elevation", nbins=10)
    fig.show()

show_locations_on_map(file)
create_histogram(file)