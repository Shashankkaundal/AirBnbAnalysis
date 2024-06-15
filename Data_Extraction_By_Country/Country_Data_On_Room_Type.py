import pandas as pd
from Data_Extraction_By_Country.Country_Data_Extraction import Get_Country_Data
def Get_Type_Of_Place(val1, val2):
    data = pd.read_csv('/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv')
    df2 = data.loc[(data['Country'] ==val1) & (data['Room_Type']==val2 )]
    Name_Cord_DF = df2[['Longitude', 'Latitude', 'Name', 'Country', 'Price', 'Room_Type', 'Review_Rating', 'Host_Name',
                        'No_Of_BedRooms', 'No_Of_BathRooms', 'No_Of_Beds']]
    Name_Cord_DF.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Data_Extraction_By_Country/Cord2.csv",
                        index=False)
    return Name_Cord_DF

