import pandas as pd
from Data_Extraction_By_Country.Country_Data_Extraction import Get_Country_Data
str1="No Data available"
def Cleaning_Fee_By_Room_Type(val1, val2):
    data = pd.read_csv('/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv')
    df2 = data.loc[(data['Country'] ==val1) & (data['Room_Type']==val2 )]
    Name_Cord_DF = df2[['Name', 'Country', 'Price', 'Cleaning_Fee']]
    Name_Cord_DF['Cleaning_Fee'] = Name_Cord_DF['Cleaning_Fee'].astype(int)
    Name_Cord_DF.sort_values(['Cleaning_Fee'], inplace=True, ascending=False)
    #Name_Cord_DF.sort_values(['Price'], inplace=True, ascending=False)
    df = Name_Cord_DF.head(10)
    df.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Cleaning_Fee_Plot/Cleaning_Fee_Room_Type.csv",
              index=False)
    data = [str1]
    # Create the pandas DataFrame
    if df.shape[0] < 1:
        df['Name'] = data
        return df
    else:
        return df
