
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
str1="No Data available"
def Cleaning_Fee_Plot_By_Ctry(val):
    data = pd.read_csv('/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv')
    df2 = data[data["Country"] == val]
    Name_Cord_DF = df2[['Name','Country','Price','Cleaning_Fee']]
    Name_Cord_DF['Cleaning_Fee'] = Name_Cord_DF['Cleaning_Fee'].astype(int)
    Name_Cord_DF.sort_values(['Cleaning_Fee'], inplace=True, ascending=False)
    #Name_Cord_DF.sort_values(['Price'], inplace=True, ascending=False)
    df = Name_Cord_DF.head(10)
    df.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Cleaning_Fee_Plot/Cleaning_Fee.csv",
              index=False)
    data = [str1]
    # Create the pandas DataFrame
    if df.shape[0] < 1:
        df['Name'] = data
        return df
    else:
        return df

    #return plt.show()
#x=Donut_Plot_Avail_By_Ctry('Australia')
#print(x)
