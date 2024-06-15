import pandas as pd

from All_Data_Extraction_DF.Data_Extract_In_DF import Data_Extract_In_DF
def Get_Country_Data(val):
    data=pd.read_csv('/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv')
    df2=data[data["Country"] == val]
    Name_Cord_DF=df2[['Longitude','Latitude','Name','Country','Price','Room_Type','Review_Rating','Host_Name','No_Of_BedRooms','No_Of_BathRooms','No_Of_Beds']]
    Name_Cord_DF.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Data_Extraction_By_Country/Cord.csv",index=False)
    return Name_Cord_DF
#x=Get_Country_Data('Australia')
#print(x)



