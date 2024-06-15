
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
str1="No Data available"
def Security_Deposit_Plot_By_Ctry(val):
    data = pd.read_csv('/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv')
    df2 = data[data["Country"] == val]
    Name_Cord_DF = df2[['Name','Country','Price','Security_Deposit']]
    Name_Cord_DF['Security_Deposit'] = Name_Cord_DF['Security_Deposit'].astype(int)
    Name_Cord_DF.sort_values(['Security_Deposit'], inplace=True, ascending=False)
    #Name_Cord_DF.sort_values(['Price'], inplace=True, ascending=False)
    df = Name_Cord_DF.head(10)
    df.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Security_Deposit_Plot/Sec_Deposit.csv",
              index=False)
    data = [str1]
    # Create the pandas DataFrame
    if df.shape[0] < 1:
        df['Name'] = data
        return df
    else:
        return df
    #return plt.show()
#x=Security_Deposit_Plot_By_Ctry('Bcd')
#print(x)
