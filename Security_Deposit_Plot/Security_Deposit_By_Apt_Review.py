import pandas as pd
from Data_Extraction_By_Country.Country_Data_Extraction import Get_Country_Data
str1="No Data available"
def Security_Deposits_By_Apt_Review_Ratings(val1, val2,val3):
    data = pd.read_csv('/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv')
    if(float(val2)<=6):
        df2 = data.loc[(data['Country'] ==val1) & (data['Review_Rating']<=float(val2) ) & (data['Room_Type']==val3)]
    elif(float(val2)>=7):
        df2 = data.loc[(data['Country'] == val1) & (data['Review_Rating'] >= float(val2)) & (data['Room_Type']==val3)]
    Name_Cord_DF = df2[['Name', 'Country', 'Price', 'Security_Deposit','Room_Type','Review_Rating']]
    Name_Cord_DF['Security_Deposit'] = Name_Cord_DF['Security_Deposit'].astype(int)
    Name_Cord_DF.sort_values(['Review_Rating'], inplace=True, ascending=False)
    Name_Cord_DF.sort_values(['Security_Deposit'], inplace=True, ascending=False)
    df = Name_Cord_DF.head(10)
    df.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Security_Deposit_Plot/Sec_Deposit_Apt_Review_Rating.csv",
              index=False)
    data = [str1]
    # Create the pandas DataFrame
    if df.shape[0] < 1:
        df['Name'] = data
        return df
    else:
        return df
