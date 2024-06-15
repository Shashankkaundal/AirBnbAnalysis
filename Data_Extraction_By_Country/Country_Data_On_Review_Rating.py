import pandas as pd
from Data_Extraction_By_Country.Country_Data_Extraction import Get_Country_Data
def Get_Type_Of_Place_From_Rating(val1, val2):
    data = pd.read_csv('/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv')
    if(float(val2)<=6):
        df2 = data.loc[(data['Country'] ==val1) & (data['Review_Rating']<=float(val2) )]
    elif(float(val2)>=7):
        df2 = data.loc[(data['Country'] == val1) & (data['Review_Rating'] >= float(val2))]
    Name_Cord_DF = df2[['Longitude', 'Latitude', 'Name', 'Country', 'Price', 'Room_Type', 'Review_Rating']]
    Name_Cord_DF.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Data_Extraction_By_Country/Cord_Review_Type.csv",
                        index=False)
    return Name_Cord_DF

