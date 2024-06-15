import pandas as pd
from Data_Extraction_By_Country.Country_Data_Extraction import Get_Country_Data
def Cleaning_Fee_BedRooms_By_Country(val1, val2):
    data = pd.read_csv('/All_Data_Extraction_DF/All_AirBnbData.csv')
    if(float(val2)<=2):
        df2 = data.loc[(data['Country'] ==val1) & (data['No_Of_BedRooms']<=float(val2) )]
    elif(float(val2)>=3):
        df2 = data.loc[(data['Country'] == val1) & (data['No_Of_BedRooms'] >= float(val2))]
    Name_Cord_DF = df2[['Name', 'Country', 'Price', 'Cleaning_Fee','No_Of_BedRooms']]
    Name_Cord_DF['Cleaning_Fee'] = Name_Cord_DF['Cleaning_Fee'].astype(int)
    #Name_Cord_DF.sort_values(['Price'], inplace=True, ascending=False)
    Name_Cord_DF.sort_values(['No_Of_BedRooms'], inplace=True, ascending=False)
    Name_Cord_DF.sort_values(['Cleaning_Fee'], inplace=True, ascending=False)
    df = Name_Cord_DF.head(10)
    df.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Cleaning_Fee_Plot/Cleaning_Fee_BedRoom_By_Country_Type.csv",
              index=False)
    return df
