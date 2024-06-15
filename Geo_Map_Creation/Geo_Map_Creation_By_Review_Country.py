import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
import plotly.express as px
import pandas as pd
from Data_Extraction_By_Country.Country_Data_Extraction import Get_Country_Data
from Data_Extraction_By_Country.Country_Data_On_Review_Rating import Get_Type_Of_Place_From_Rating
str1="No Data available"
def Geo_Map_Creation_Review_Filters(val1,val2):
    x=Get_Type_Of_Place_From_Rating(val1,val2)
    #long =x[['Longitude','Latitude']]
    #name=x['Name']
    df = pd.read_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Data_Extraction_By_Country/Cord_Review_Type.csv")
    if df.shape[0]<1:
        return str1
    else:
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Country"],
                            color_discrete_sequence=["Blue"], zoom=8, height=300)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return fig
#x=Geo_Map_Creation('Turkey')
#print(x)