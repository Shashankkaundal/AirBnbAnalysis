import pandas as pd
str1="No Data available"
def Cleaning_Fee_Review_Rating_By_Country(val1, val2):
    data = pd.read_csv('/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv')
    if(float(val2)<=6):
        df2 = data.loc[(data['Country'] ==val1) & (data['Review_Rating']<=float(val2) )]
    elif(float(val2)>=7):
        df2 = data.loc[(data['Country'] == val1) & (data['Review_Rating'] >= float(val2))]
    Name_Cord_DF = df2[['Name', 'Country', 'Price', 'Cleaning_Fee','Review_Rating']]
    Name_Cord_DF['Cleaning_Fee'] = Name_Cord_DF['Cleaning_Fee'].astype(int)
    #Name_Cord_DF.sort_values(['Price'], inplace=True, ascending=False)
    Name_Cord_DF.sort_values(['Review_Rating'], inplace=True, ascending=False)
    Name_Cord_DF.sort_values(['Cleaning_Fee'], inplace=True, ascending=False)
    df = Name_Cord_DF.head(10)
    df.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Cleaning_Fee_Plot/Cleaning_Fee_Review_Rating_By_Country_Type.csv",
              index=False)
    data = [str1]
    # Create the pandas DataFrame
    if df.shape[0] < 1:
        df['Name'] = data
        return df
    else:
        return df