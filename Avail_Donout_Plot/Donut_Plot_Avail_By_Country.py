import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
print([f for f in matplotlib.font_manager.fontManager.ttflist if 'Heiti' in f.name])
def Donut_Plot_Avail_By_Ctry(val):
    data = pd.read_csv('/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv')
    df2 = data[data["Country"] == val]
    Name_Cord_DF = df2[['Name','Country','Price','Days_30_Availability','Days_60_Availability','Days_90_Availability','Days_365_Availability']]
    Name_Cord_DF['Price'] = Name_Cord_DF['Price'].astype(int)
    Name_Cord_DF.sort_values(['Price'], inplace=True,ascending=False)
    df = Name_Cord_DF.head(10)
    df.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Avail_Donout_Plot/Donut_Plot_By_Country1.csv",
              index=False)
    l1=[]
    l1.append( df.loc[:,'Days_30_Availability'].mean())
    l1.append( df.loc[:, 'Days_60_Availability'].mean())
    l1.append(df.loc[:, 'Days_90_Availability'].mean())
    l1.append(df.loc[:, 'Days_365_Availability'].mean())
    print(l1)
    labels = ['30 Days', '60 Days', '90 Days', '365 Days']

    # Pie Chart
    colors = ['#FF0000', '#0000FF', '#FFFF00', '#ADFF2F']

    # explosion
    explode = (0.05, 0.05, 0.05, 0.05)

    # Pie Chart
    plt.pie(l1, colors=colors, labels=labels,
            autopct='%1.1f%%', pctdistance=0.85,
            explode=explode)

    # draw circle
    centre_circle = plt.Circle((0, 0), 0.50, fc='white')
    fig = plt.gcf()
    # Adding Circle in Pie chart
    fig.gca().add_artist(centre_circle)

    # Adding Title of chart
    plt.title('Host Availability over a year')
    return plt
    #return plt.show()
x=Donut_Plot_Avail_By_Ctry('Australia')
print(x)
