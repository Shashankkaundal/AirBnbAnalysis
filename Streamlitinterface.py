import streamlit as st
import altair as alt
import time
from Geo_Map_Creation.Geo_Map_Creation_Final import Geo_Map_Creation
from Geo_Map_Creation.Geo_Map_Creation_2_Filters import Geo_Map_Creation_2_Filters
from Geo_Map_Creation.Geo_Map_Creation_By_Review_Country import Geo_Map_Creation_Review_Filters
from Geo_Map_Creation.Geo_Map_Creation_By_Apt_Review_Country import Geo_Map_Creation_Apt_Review_Filters
from Host_Category_Plot.Top_Host_Category_Plot_By_Ctry import Top_Host_Category_Plot_By_Ctry
from Host_Category_Plot.Top_Host_Category_Plot_By_Room import Top_Host_Category_Plot_By_Room
from Host_Category_Plot.Top_Host_Category_Plot_By_Ratings import Top_Host_Category_Plot_By_Rating
from Host_Category_Plot.Top_Host_Catrgory_Plot_By_Apt_Ratings import Top_Host_Category_Plot_By_Apt_Rating
from Security_Deposit_Plot.Security_Deposit_By_Apt_Review import Security_Deposits_By_Apt_Review_Ratings
from Security_Deposit_Plot.Security_Deposit_Plot import Security_Deposit_Plot_By_Ctry
from Cleaning_Fee_Plot.Cleaning_Fee_Plot_By_Country import Cleaning_Fee_Plot_By_Ctry
from Security_Deposit_Plot.Security_Deposit_By_Room_Type import Security_Deposits_By_Room_Type
from Security_Deposit_Plot.Security_Deposit_By_Review_Rating import Security_Deposits_By_Review_Ratings
from Cleaning_Fee_Plot.Cleaning_Fee_By_Room_Type import Cleaning_Fee_By_Room_Type
from Cleaning_Fee_Plot.Cleaning_Fee_By_Review_Rating_Country import Cleaning_Fee_Review_Rating_By_Country
from Cleaning_Fee_Plot.Cleaning_Fee_3_Parameters.Cleaning_Fee_Review_Rating_By_Room import Cleaning_Fee_Apt_Bedrooms_By_Country

st.set_page_config(
    page_title="Air BNB Analysis Dashboard",
    page_icon="🏨",
    layout="wide",
    #initial_sidebar_state="auto"
    initial_sidebar_state="expanded"
    )

alt.themes.enable("dark")
st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
            text-align: center;
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            text-align: center;
        } 
        div[data-testid="column"]:nth-of-type(3)
        {
            text-align: center;
        } 
    </style>
    """,unsafe_allow_html=True
)

custom_html = """
<div class="banner">
    <img src="https://www.digital.ink/wp-content/uploads/airbnb_logo_detail.jpg" alt="Banner Image" class="center">
</div>
<style>
    .banner {
        width: 100%;
        height: 200px;
        overflow: hidden;
    }
    .banner img {
        width: 40%;
        height: 125px;
        object-fit: cover;
        
    }
    .center{
     display: block;
    margin-left: auto;
    margin-right: auto;
    width: 25%;
    }
</style>
"""
st.markdown(custom_html, unsafe_allow_html=True)


#add sidebar
with st.sidebar:
    st.title('🏨 AirBNB Analysis Dashboard')

   # year_list = list(df_reshaped.year.unique())[::-1]

    selected_Country = st.selectbox( label='Choose Country', options=("Australia", "Brazil","Canada",
                                                                      "China","Hong Kong","Portugal","Spain","Turkey","United States"))
    selected_Type_Of_Place = st.selectbox(label='Choose Type of Place', options=("Choose an option", "Entire home/apt", "Private Room",
                                                                                 "Shared Room"))
    #selected_Price_Range = st.selectbox(label='Choose Price Range', options=("Choose an option", "X", "Y"))
    #selected_No_Of_Beds = st.selectbox(label='Choose No Of Beds', options=("Choose an option","<=2",">=3"))
    #selected_No_Of_BedRooms = st.selectbox(label='Choose No Of Bedrooms', options=("Choose an option","<=2",">=3"))
    selected_Review_Ratings=st.selectbox(label='Choose Review Rating', options=("Choose an option", "<=6",">=7"))
col = st.columns((3.0,4.5,3.0), gap='Medium')
with col[1]:
    st.markdown('### Host Locations')
    ###Australia
    if (selected_Country == 'Australia' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Australia'
        val2 = '6'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Australia' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Australia'
        val2 = '7'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Australia' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = '6'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Australia' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = '7'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif(selected_Country == 'Australia' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Australia'
        val2 = '6'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Australia' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Australia'
        val2 = '7'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Australia' and selected_Review_Ratings == '>=7'):
        val1 = 'Australia'
        val2 = '7'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Australia' and selected_Review_Ratings == '<=6'):
        val1 = 'Australia'
        val2 = '6'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Australia'
        val2 = 'Shared room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = 'Private room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Australia'
        val2 = 'Entire home/apt'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
        #z = plot(x)
    elif (selected_Country == 'Australia'):
        val = 'Australia'
        x = Geo_Map_Creation(val)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    ####Turkey
    ###
    if (selected_Country == 'Turkey' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Turkey'
        val2 = '6'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Turkey'
        val2 = '7'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = '6'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = '7'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif(selected_Country == 'Turkey' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Turkey'
        val2 = '6'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    # with plot_spot:
        st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Turkey'
        val2 = '7'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '>=7'):
        val1 = 'Turkey'
        val2 = '7'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '<=6'):
        val1 = 'Turkey'
        val2 = '6'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Turkey'
        val2 = 'Shared room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = 'Private room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Turkey'
        val2 = 'Entire home/apt'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
        #z = plot(x)
    elif (selected_Country == 'Turkey'):
        val = 'Turkey'
        x = Geo_Map_Creation(val)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    ##China
    if (selected_Country == 'China' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'China'
        val2 = '6'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'China' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'China'
        val2 = '7'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'China' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = '6'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    # with plot_spot:
    elif (selected_Country == 'China' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = '7'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif(selected_Country == 'China' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'China'
        val2 = '6'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'China' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'China'
        val2 = '7'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'China' and selected_Review_Ratings == '>=7'):
        val1 = 'China'
        val2 = '7'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'China' and selected_Review_Ratings == '<=6'):
        val1 = 'China'
        val2 = '6'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'China'
        val2 = 'Shared room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = 'Private room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'China'
        val2 = 'Entire home/apt'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
        #z = plot(x)
    elif (selected_Country == 'China'):
        val = 'China'
        x = Geo_Map_Creation(val)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)


    ###Brazil
    if (selected_Country == 'Brazil' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Brazil'
        val2 = '6'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        #st.plotly_chart(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Brazil'
        val2 = '7'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = '6'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = '7'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif(selected_Country == 'Brazil' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Brazil'
        val2 = '6'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Brazil'
        val2 = '7'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '>=7'):
        val1 = 'Brazil'
        val2 = '7'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '<=6'):
        val1 = 'Brazil'
        val2 = '6'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Brazil'
        val2 = 'Shared room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = 'Private room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Brazil'
        val2 = 'Entire home/apt'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
        #z = plot(x)
    elif (selected_Country == 'Brazil'):
        val = 'Brazil'
        x = Geo_Map_Creation(val)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    ###Canada
    if (selected_Country == 'Canada' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Canada'
        val2 = '6'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Canada' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Canada'
        val2 = '7'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Canada' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = '6'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Canada' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = '7'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif(selected_Country == 'Canada' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Canada'
        val2 = '6'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Canada' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Canada'
        val2 = '7'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Canada' and selected_Review_Ratings == '>=7'):
        val1 = 'Canada'
        val2 = '7'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Canada' and selected_Review_Ratings == '<=6'):
        val1 = 'Canada'
        val2 = '6'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Canada'
        val2 = 'Shared room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = 'Private room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Canada'
        val2 = 'Entire home/apt'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
        #z = plot(x)
    elif (selected_Country == 'Canada'):
        val = 'Canada'
        x = Geo_Map_Creation(val)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)


    ##portugal
    if (selected_Country == 'Portugal' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Portugal'
        val2 = '6'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Portugal'
        val2 = '7'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = '6'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = '7'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif(selected_Country == 'Portugal' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Portugal'
        val2 = '6'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Portugal'
        val2 = '7'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '>=7'):
        val1 = 'Portugal'
        val2 = '7'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '<=6'):
        val1 = 'Portugal'
        val2 = '6'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Portugal'
        val2 = 'Shared room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = 'Private room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Portugal'
        val2 = 'Entire home/apt'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
        #z = plot(x)
    elif (selected_Country == 'Portugal'):
        val = 'Portugal'
        x = Geo_Map_Creation(val)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    ##Spain
    if (selected_Country == 'Spain' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Spain'
        val2 = '6'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Spain' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Spain'
        val2 = '7'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Spain' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = '6'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Spain' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = '7'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif(selected_Country == 'Spain' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Spain'
        val2 = '6'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Spain' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Spain'
        val2 = '7'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Spain' and selected_Review_Ratings == '>=7'):
        val1 = 'Spain'
        val2 = '7'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Spain' and selected_Review_Ratings == '<=6'):
        val1 = 'Spain'
        val2 = '6'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Spain'
        val2 = 'Shared room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = 'Private room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Spain'
        val2 = 'Entire home/apt'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
        #z = plot(x)
    elif (selected_Country == 'Spain'):
        val = 'Spain'
        x = Geo_Map_Creation(val)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    ##Honkong
    if (selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif(selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '>=7'):
        val1 = 'Hong Kong'
        val2 = '7'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6'):
        val1 = 'Hong Kong'
        val2 = '6'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Hong Kong'
        val2 = 'Shared room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = 'Private room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Hong Kong'
        val2 = 'Entire home/apt'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
        #z = plot(x)
    elif (selected_Country == 'Hong Kong'):
        val = 'Hong Kong'
        x = Geo_Map_Creation(val)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)


    ##United States
    if (selected_Country == 'United States' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'United States'
        val2 = '6'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'United States' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'United States'
        val2 = '7'
        val3 = 'Shared room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'United States' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = '6'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'United States' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = '7'
        val3 = 'Private room'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2, val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif(selected_Country == 'United States' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'United States'
        val2 = '6'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'United States' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'United States'
        val2 = '7'
        val3='Entire home/apt'
        x = Geo_Map_Creation_Apt_Review_Filters(val1, val2,val3)
    # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)

    elif (selected_Country == 'United States' and selected_Review_Ratings == '>=7'):
        val1 = 'United States'
        val2 = '7'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'United States' and selected_Review_Ratings == '<=6'):
        val1 = 'United States'
        val2 = '6'
        x = Geo_Map_Creation_Review_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'United States'
        val2 = 'Shared room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = 'Private room'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'United States'
        val2 = 'Entire home/apt'
        x = Geo_Map_Creation_2_Filters(val1, val2)
        #with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
        #z = plot(x)
    elif (selected_Country == 'United States'):
        val = 'United States'
        x = Geo_Map_Creation(val)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.plotly_chart(x, use_container_width=True)
with col[1]:
    st.markdown('### Top 10 Hosts Price by selection criteria')
    ###Australia
    if (selected_Country == 'Australia' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Australia'
        val2 = '6'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Australia' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = '7'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif (selected_Country == 'Australia' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = '6'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Australia' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = '7'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif(selected_Country == 'Australia' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Australia'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif(selected_Country == 'Australia' and selected_Review_Ratings =='>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Australia'
        val2 = '7'
        val3='Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2,val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Australia' and selected_Review_Ratings =='>=7'):
        val1 = 'Australia'
        val2 = '7'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Australia' and selected_Review_Ratings =='<=6'):
        val1 = 'Australia'
        val2 = '6'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Australia'
        val2 = 'Shared room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = 'Private room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Australia'
        val2 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
        # z = plot(x)
    elif (selected_Country == 'Australia'):
        val = 'Australia'
        x= Top_Host_Category_Plot_By_Ctry(val)
        # with plot_spot:
        #st.plotly_chart(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
###Brazil
    if (selected_Country == 'Brazil' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Brazil'
        val2 = '6'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        #st.pyplot(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Brazil' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = '7'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = '6'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Brazil' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = '7'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif(selected_Country == 'Brazil' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Brazil'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif(selected_Country == 'Brazil' and selected_Review_Ratings =='>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Brazil'
        val2 = '7'
        val3='Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2,val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Brazil' and selected_Review_Ratings =='>=7'):
        val1 = 'Brazil'
        val2 = '7'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Brazil' and selected_Review_Ratings =='<=6'):
        val1 = 'Brazil'
        val2 = '6'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Brazil'
        val2 = 'Shared room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = 'Private room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Brazil'
        val2 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
        # z = plot(x)
    elif (selected_Country == 'Brazil'):
        val = 'Brazil'
        x = Top_Host_Category_Plot_By_Ctry(val)
        # with plot_spot:
        #st.plotly_chart(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
###Canada
    if (selected_Country == 'Canada' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Canada'
        val2 = '6'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Canada' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = '7'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif (selected_Country == 'Canada' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = '6'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Canada' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = '7'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif(selected_Country == 'Canada' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Canada'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif(selected_Country == 'Canada' and selected_Review_Ratings =='>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Canada'
        val2 = '7'
        val3='Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2,val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Canada' and selected_Review_Ratings =='>=7'):
        val1 = 'Canada'
        val2 = '7'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Canada' and selected_Review_Ratings =='<=6'):
        val1 = 'Canada'
        val2 = '6'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Canada'
        val2 = 'Shared room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = 'Private room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Canada'
        val2 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
        # z = plot(x)
    elif (selected_Country == 'Canada'):
        val = 'Canada'
        x = Top_Host_Category_Plot_By_Ctry(val)
        # with plot_spot:
        #st.plotly_chart(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
###China
    if (selected_Country == 'China' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'China'
        val2 = '6'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'China' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = '7'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif (selected_Country == 'China' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = '6'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'China' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = '7'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif(selected_Country == 'China' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'China'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif(selected_Country == 'China' and selected_Review_Ratings =='>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'China'
        val2 = '7'
        val3='Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2,val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'China' and selected_Review_Ratings =='>=7'):
        val1 = 'China'
        val2 = '7'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'China' and selected_Review_Ratings =='<=6'):
        val1 = 'China'
        val2 = '6'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'China'
        val2 = 'Shared room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = 'Private room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'China'
        val2 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
        # z = plot(x)
    elif (selected_Country == 'China'):
        val = 'China'
        x = Top_Host_Category_Plot_By_Ctry(val)
        # with plot_spot:
        #st.plotly_chart(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
###Hong kong
    if (selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Hong Kong' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Hong Kong' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif(selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif(selected_Country == 'Hong Kong' and selected_Review_Ratings =='>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3='Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2,val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings =='>=7'):
        val1 = 'Hong Kong'
        val2 = '7'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings =='<=6'):
        val1 = 'Hong Kong'
        val2 = '6'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Hong Kong'
        val2 = 'Shared room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = 'Private room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Hong Kong'
        val2 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
        # z = plot(x)
    elif (selected_Country == 'Hong Kong'):
        val = 'Hong Kong'
        x = Top_Host_Category_Plot_By_Ctry(val)
        # with plot_spot:
        #st.plotly_chart(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
###Portugal
    if (selected_Country == 'Portugal' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Portugal'
        val2 = '6'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Portugal' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = '7'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = '6'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Portugal' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = '7'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif(selected_Country == 'Portugal' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Portugal'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif(selected_Country == 'Portugal' and selected_Review_Ratings =='>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Portugal'
        val2 = '7'
        val3='Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2,val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Portugal' and selected_Review_Ratings =='>=7'):
        val1 = 'Portugal'
        val2 = '7'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Portugal' and selected_Review_Ratings =='<=6'):
        val1 = 'Portugal'
        val2 = '6'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Portugal'
        val2 = 'Shared room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = 'Private room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Portugal'
        val2 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
        # z = plot(x)
    elif (selected_Country == 'Portugal'):
        val = 'Portugal'
        x = Top_Host_Category_Plot_By_Ctry(val)
        # with plot_spot:
        #st.plotly_chart(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
###Spain
    if (selected_Country == 'Spain' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Spain'
        val2 = '6'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Spain' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = '7'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif (selected_Country == 'Spain' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = '6'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Spain' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = '7'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif(selected_Country == 'Spain' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Spain'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif(selected_Country == 'Spain' and selected_Review_Ratings =='>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Spain'
        val2 = '7'
        val3='Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2,val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Spain' and selected_Review_Ratings =='>=7'):
        val1 = 'Spain'
        val2 = '7'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Spain' and selected_Review_Ratings =='<=6'):
        val1 = 'Spain'
        val2 = '6'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Spain'
        val2 = 'Shared room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = 'Private room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Spain'
        val2 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
        # z = plot(x)
    elif (selected_Country == 'Spain'):
        val = 'Spain'
        x = Top_Host_Category_Plot_By_Ctry(val)
        # with plot_spot:
        #st.plotly_chart(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
###Turkey
    if (selected_Country == 'Turkey' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Turkey'
        val2 = '6'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Turkey' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = '7'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = '6'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'Turkey' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = '7'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif(selected_Country == 'Turkey' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Turkey'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif(selected_Country == 'Turkey' and selected_Review_Ratings =='>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Turkey'
        val2 = '7'
        val3='Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2,val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Turkey' and selected_Review_Ratings =='>=7'):
        val1 = 'Turkey'
        val2 = '7'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Turkey' and selected_Review_Ratings =='<=6'):
        val1 = 'Turkey'
        val2 = '6'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Turkey'
        val2 = 'Shared room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = 'Private room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Turkey'
        val2 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
        # z = plot(x)
    elif (selected_Country == 'Turkey'):
        val = 'Turkey'
        x = Top_Host_Category_Plot_By_Ctry(val)
        # with plot_spot:
        #st.plotly_chart(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
##United States
    if (selected_Country == 'United States' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'United States'
        val2 = '6'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'United States' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = '7'
        val3 = 'Shared room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif (selected_Country == 'United States' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = '6'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif(selected_Country == 'United States' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = '7'
        val3 = 'Private room'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)


    elif(selected_Country == 'United States' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'United States'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2, val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif(selected_Country == 'United States' and selected_Review_Ratings =='>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'United States'
        val2 = '7'
        val3='Entire home/apt'
        x = Top_Host_Category_Plot_By_Apt_Rating(val1, val2,val3)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'United States' and selected_Review_Ratings =='>=7'):
        val1 = 'United States'
        val2 = '7'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'United States' and selected_Review_Ratings =='<=6'):
        val1 = 'United States'
        val2 = '6'
        x = Top_Host_Category_Plot_By_Rating(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'United States'
        val2 = 'Shared room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = 'Private room'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'United States'
        val2 = 'Entire home/apt'
        x = Top_Host_Category_Plot_By_Room(val1, val2)
        # with plot_spot:
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)
        # z = plot(x)
    elif (selected_Country == 'United States'):
        val = 'United States'
        x = Top_Host_Category_Plot_By_Ctry(val)
        # with plot_spot:
        #st.plotly_chart(x, use_container_width=True)
        if (x == 'No Data available'):
            st.write(x)
        else:
            st.pyplot(x, use_container_width=True)

with col[2]:
    st.markdown('### Top 10 Hosts by Security Deposits')
    ##Australia
    if (selected_Country == 'Australia' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = '6'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Australia' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = '7'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Australia' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Australia'
        val2 = '6'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Australia' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Australia'
        val2 = '7'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )


    elif(selected_Country == 'Australia' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Australia'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )

    elif(selected_Country == 'Australia' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Australia'
        val2 = '7'
        val3='Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Australia' and selected_Review_Ratings=='>=7'):
        val1 = 'Australia'
        val2='7'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Australia' and selected_Review_Ratings=='<=6'):
        val1 = 'Australia'
        val2 ='6'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Australia'
        val2 = 'Shared room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = 'Private room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Australia'
        val2 = 'Entire home/apt'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Australia'):
        val = 'Australia'
        x = Security_Deposit_Plot_By_Ctry(val)
        print(x)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    ##Brazil
    if (selected_Country == 'Brazil' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = '6'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = '7'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Brazil'
        val2 = '6'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                         column_order=("Name", "Security_Deposit"),
                         hide_index=True,
                         width=None,
                         column_config={
                             "Name": st.column_config.TextColumn(
                                 "Name",
                             ),
                             "Security_Deposit": st.column_config.ProgressColumn(
                                 "Security_Deposit",
                                 format="%f",
                                 min_value=0,
                                 max_value=max(x.Security_Deposit),
                             )}
                         )
    elif(selected_Country == 'Brazil' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Brazil'
        val2 = '7'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )


    elif(selected_Country == 'Brazil' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Brazil'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )

    elif(selected_Country == 'Brazil' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Brazil'
        val2 = '7'
        val3='Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Brazil' and selected_Review_Ratings=='>=7'):
        val1 = 'Brazil'
        val2='7'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Brazil' and selected_Review_Ratings=='<=6'):
        val1 = 'Brazil'
        val2 ='6'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Brazil'
        val2 = 'Shared room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = 'Private room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Brazil'
        val2 = 'Entire home/apt'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Brazil'):
        val = 'Brazil'
        x = Security_Deposit_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    #Canada
    if (selected_Country == 'Canada' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = '6'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Canada' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = '7'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Canada' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Canada'
        val2 = '6'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Canada' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Canada'
        val2 = '7'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )


    elif(selected_Country == 'Canada' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Canada'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )

    elif(selected_Country == 'Canada' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Canada'
        val2 = '7'
        val3='Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Canada' and selected_Review_Ratings=='>=7'):
        val1 = 'Canada'
        val2='7'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Canada' and selected_Review_Ratings=='<=6'):
        val1 = 'Canada'
        val2 ='6'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Canada'
        val2 = 'Shared room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = 'Private room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Canada'
        val2 = 'Entire home/apt'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Canada'):
        val = 'Canada'
        x = Security_Deposit_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
#China
    if (selected_Country == 'China' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = '6'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'China' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = '7'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'China' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'China'
        val2 = '6'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'China' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'China'
        val2 = '7'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )


    elif(selected_Country == 'China' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'China'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )

    elif(selected_Country == 'China' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'China'
        val2 = '7'
        val3='Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'China' and selected_Review_Ratings=='>=7'):
        val1 = 'China'
        val2='7'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'China' and selected_Review_Ratings=='<=6'):
        val1 = 'China'
        val2 ='6'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'China'
        val2 = 'Shared room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = 'Private room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'China'
        val2 = 'Entire home/apt'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'China'):
        val = 'China'
        x = Security_Deposit_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

#Hong kong
    if (selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Hong Kong' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )


    elif(selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )

    elif(selected_Country == 'Hong Kong' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3='Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Hong Kong' and selected_Review_Ratings=='>=7'):
        val1 = 'Hong Kong'
        val2='7'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings=='<=6'):
        val1 = 'Hong Kong'
        val2 ='6'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Hong Kong'
        val2 = 'Shared room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = 'Private room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Hong Kong'
        val2 = 'Entire home/apt'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Hong Kong'):
        val = 'Hong Kong'
        x = Security_Deposit_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

#Portugal
    if (selected_Country == 'Portugal' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = '6'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = '7'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Portugal'
        val2 = '6'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Portugal' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Portugal'
        val2 = '7'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )


    elif(selected_Country == 'Portugal' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Portugal'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )

    elif(selected_Country == 'Portugal' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Portugal'
        val2 = '7'
        val3='Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Portugal' and selected_Review_Ratings=='>=7'):
        val1 = 'Portugal'
        val2='7'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Portugal' and selected_Review_Ratings=='<=6'):
        val1 = 'Portugal'
        val2 ='6'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Portugal'
        val2 = 'Shared room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = 'Private room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Portugal'
        val2 = 'Entire home/apt'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Portugal'):
        val = 'Portugal'
        x = Security_Deposit_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
#Spain
    if (selected_Country == 'Spain' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = '6'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Spain' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = '7'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Spain' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Spain'
        val2 = '6'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Spain' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Spain'
        val2 = '7'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )


    elif(selected_Country == 'Spain' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Spain'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )

    elif(selected_Country == 'Spain' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Spain'
        val2 = '7'
        val3='Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Spain' and selected_Review_Ratings=='>=7'):
        val1 = 'Spain'
        val2='7'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Spain' and selected_Review_Ratings=='<=6'):
        val1 = 'Spain'
        val2 ='6'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Spain'
        val2 = 'Shared room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = 'Private room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Spain'
        val2 = 'Entire home/apt'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Spain'):
        val = 'Spain'
        x = Security_Deposit_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

#Turkey
    if (selected_Country == 'Turkey' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = '6'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = '7'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Turkey'
        val2 = '6'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Turkey' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Turkey'
        val2 = '7'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )


    elif(selected_Country == 'Turkey' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Turkey'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )

    elif(selected_Country == 'Turkey' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'Turkey'
        val2 = '7'
        val3='Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'Turkey' and selected_Review_Ratings=='>=7'):
        val1 = 'Turkey'
        val2='7'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Turkey' and selected_Review_Ratings=='<=6'):
        val1 = 'Turkey'
        val2 ='6'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Turkey'
        val2 = 'Shared room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = 'Private room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Turkey'
        val2 = 'Entire home/apt'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'Turkey'):
        val = 'Turkey'
        x = Security_Deposit_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
#United States
    if (selected_Country == 'United States' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = '6'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'United States' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = '7'
        val3 = 'Private room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'United States' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'United States'
        val2 = '6'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'United States' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'United States'
        val2 = '7'
        val3 = 'Shared room'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )


    elif(selected_Country == 'United States' and selected_Review_Ratings == '<=6' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'United States'
        val2 = '6'
        val3 = 'Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )

    elif(selected_Country == 'United States' and selected_Review_Ratings == '>=7' and selected_Type_Of_Place=='Entire home/apt'):
        val1 = 'United States'
        val2 = '7'
        val3='Entire home/apt'
        x = Security_Deposits_By_Apt_Review_Ratings(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Security_Deposit"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Security_Deposit": st.column_config.ProgressColumn(
                         "Security_Deposit",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Security_Deposit),
                     )}
                 )
    elif(selected_Country == 'United States' and selected_Review_Ratings=='>=7'):
        val1 = 'United States'
        val2='7'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'United States' and selected_Review_Ratings=='<=6'):
        val1 = 'United States'
        val2 ='6'
        x = Security_Deposits_By_Review_Ratings(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )

    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'United States'
        val2 = 'Shared room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = 'Private room'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'United States'
        val2 = 'Entire home/apt'
        x = Security_Deposits_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
    elif (selected_Country == 'United States'):
        val = 'United States'
        x = Security_Deposit_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Security_Deposit"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Security_Deposit": st.column_config.ProgressColumn(
                             "Security_Deposit",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Security_Deposit),
                         )}
                     )
with col[0]:
    st.markdown('### Top 10 Hosts by Cleaning Fee')
    #Australia
    if (selected_Country == 'Australia' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Australia'
        val2 = '6'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )


    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Australia'
        val2 = '7'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Private Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Australia'
        val2 = '7'
        val3 = 'Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Australia' and selected_Type_Of_Place=='Private Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Australia'
        val2 = '6'
        val3='Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )



    elif (selected_Country == 'Australia' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '>=7'):
        val1 = 'Australia'
        val2 = '7'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Australia' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '<=6'):
        val1 = 'Australia'
        val2 = '6'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Australia' and selected_Review_Ratings == '>=7'):
        val1 = 'Australia'
        val2 = '7'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Australia' and selected_Review_Ratings == '<=6'):
        val1 = 'Australia'
        val2 = '6'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Australia'
        val2 = 'Shared room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Australia'
        val2 = 'Private room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Australia' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Australia'
        val2 = 'Entire home/apt'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Australia'):
        val = 'Australia'
        x = Cleaning_Fee_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

#Brazil
    if (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Brazil'
        val2 = '6'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                         column_order=("Name", "Cleaning_Fee"),
                         hide_index=True,
                         width=None,
                         column_config={
                             "Name": st.column_config.TextColumn(
                                 "Name",
                             ),
                             "Cleaning_Fee": st.column_config.ProgressColumn(
                                 "Cleaning_Fee",
                                 format="%f",
                                 min_value=0,
                                 max_value=max(x.Cleaning_Fee),
                             )}
                         )


    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Brazil'
        val2 = '7'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Private Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Brazil'
        val2 = '7'
        val3 = 'Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Brazil' and selected_Type_Of_Place=='Private Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Brazil'
        val2 = '6'
        val3='Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )



    elif (selected_Country == 'Brazil' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '>=7'):
        val1 = 'Brazil'
        val2 = '7'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Brazil' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '<=6'):
        val1 = 'Brazil'
        val2 = '6'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '>=7'):
        val1 = 'Brazil'
        val2 = '7'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Brazil' and selected_Review_Ratings == '<=6'):
        val1 = 'Brazil'
        val2 = '6'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Brazil'
        val2 = 'Shared room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Brazil'
        val2 = 'Private room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Brazil' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Brazil'
        val2 = 'Entire home/apt'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Brazil'):
        val = 'Brazil'
        x = Cleaning_Fee_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
#Canada
    if (selected_Country == 'Canada' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Canada'
        val2 = '6'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )


    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Canada'
        val2 = '7'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Private Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Canada'
        val2 = '7'
        val3 = 'Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Canada' and selected_Type_Of_Place=='Private Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Canada'
        val2 = '6'
        val3='Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )



    elif (selected_Country == 'Canada' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '>=7'):
        val1 = 'Canada'
        val2 = '7'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Canada' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '<=6'):
        val1 = 'Canada'
        val2 = '6'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Canada' and selected_Review_Ratings == '>=7'):
        val1 = 'Canada'
        val2 = '7'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Canada' and selected_Review_Ratings == '<=6'):
        val1 = 'Canada'
        val2 = '6'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Canada'
        val2 = 'Shared room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Canada'
        val2 = 'Private room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Canada' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Canada'
        val2 = 'Entire home/apt'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Canada'):
        val = 'Canada'
        x = Cleaning_Fee_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

#China
    if (selected_Country == 'China' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '<=6'):
        val1 = 'China'
        val2 = '6'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )


    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '>=7'):
            val1 = 'China'
            val2 = '7'
            val3 = 'Shared room'
            x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
            if (x['Name'] == 'No Data available').any():
                st.write(x)
            else:
                st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Private Room' and selected_Review_Ratings == '>=7'):
        val1 = 'China'
        val2 = '7'
        val3 = 'Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'China' and selected_Type_Of_Place=='Private Room' and selected_Review_Ratings == '<=6'):
        val1 = 'China'
        val2 = '6'
        val3='Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )



    elif (selected_Country == 'China' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '>=7'):
        val1 = 'China'
        val2 = '7'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'China' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '<=6'):
        val1 = 'China'
        val2 = '6'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'China' and selected_Review_Ratings == '>=7'):
        val1 = 'China'
        val2 = '7'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'China' and selected_Review_Ratings == '<=6'):
        val1 = 'China'
        val2 = '6'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'China'
        val2 = 'Shared room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'China'
        val2 = 'Private room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'China' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'China'
        val2 = 'Entire home/apt'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'China'):
        val = 'China'
        x = Cleaning_Fee_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

#Hongkong
    if (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )


    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Private Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3 = 'Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place=='Private Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3='Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )



    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '>=7'):
        val1 = 'Hong Kong'
        val2 = '7'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '<=6'):
        val1 = 'Hong Kong'
        val2 = '6'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '>=7'):
        val1 = 'Hong Kong'
        val2 = '7'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Hong Kong' and selected_Review_Ratings == '<=6'):
        val1 = 'Hong Kong'
        val2 = '6'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Hong Kong'
        val2 = 'Shared room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Hong Kong'
        val2 = 'Private room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Hong Kong' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Hong Kong'
        val2 = 'Entire home/apt'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Hong Kong'):
        val = 'Hong Kong'
        x = Cleaning_Fee_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

#Portugal
    if (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Portugal'
        val2 = '6'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )


    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Portugal'
        val2 = '7'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Private Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Portugal'
        val2 = '7'
        val3 = 'Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Portugal' and selected_Type_Of_Place=='Private Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Portugal'
        val2 = '6'
        val3='Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )



    elif (selected_Country == 'Portugal' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '>=7'):
        val1 = 'Portugal'
        val2 = '7'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Portugal' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '<=6'):
        val1 = 'Portugal'
        val2 = '6'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '>=7'):
        val1 = 'Portugal'
        val2 = '7'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Portugal' and selected_Review_Ratings == '<=6'):
        val1 = 'Portugal'
        val2 = '6'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Portugal'
        val2 = 'Shared room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Portugal'
        val2 = 'Private room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Portugal' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Portugal'
        val2 = 'Entire home/apt'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Portugal'):
        val = 'Portugal'
        x = Cleaning_Fee_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
#Spain
    if (selected_Country == 'Spain' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Spain'
        val2 = '6'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )


    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Spain'
        val2 = '7'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Private Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Spain'
        val2 = '7'
        val3 = 'Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Spain' and selected_Type_Of_Place=='Private Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Spain'
        val2 = '6'
        val3='Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )



    elif (selected_Country == 'Spain' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '>=7'):
        val1 = 'Spain'
        val2 = '7'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Spain' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '<=6'):
        val1 = 'Spain'
        val2 = '6'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Spain' and selected_Review_Ratings == '>=7'):
        val1 = 'Spain'
        val2 = '7'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Spain' and selected_Review_Ratings == '<=6'):
        val1 = 'Spain'
        val2 = '6'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Spain'
        val2 = 'Shared room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Spain'
        val2 = 'Private room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Spain' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Spain'
        val2 = 'Entire home/apt'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Spain'):
        val = 'Spain'
        x = Cleaning_Fee_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

#Turkey
    if (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Turkey'
        val2 = '6'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )


    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Turkey'
        val2 = '7'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Private Room' and selected_Review_Ratings == '>=7'):
        val1 = 'Turkey'
        val2 = '7'
        val3 = 'Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'Turkey' and selected_Type_Of_Place=='Private Room' and selected_Review_Ratings == '<=6'):
        val1 = 'Turkey'
        val2 = '6'
        val3='Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )



    elif (selected_Country == 'Turkey' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '>=7'):
        val1 = 'Turkey'
        val2 = '7'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Turkey' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '<=6'):
        val1 = 'Turkey'
        val2 = '6'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '>=7'):
        val1 = 'Turkey'
        val2 = '7'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Turkey' and selected_Review_Ratings == '<=6'):
        val1 = 'Turkey'
        val2 = '6'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'Turkey'
        val2 = 'Shared room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'Turkey'
        val2 = 'Private room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Turkey' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'Turkey'
        val2 = 'Entire home/apt'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'Turkey'):
        val = 'Turkey'
        x = Cleaning_Fee_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

#United States
    if (selected_Country == 'United States' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '<=6'):
        val1 = 'United States'
        val2 = '6'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )


    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Shared Room' and selected_Review_Ratings == '>=7'):
        val1 = 'United States'
        val2 = '7'
        val3 = 'Shared room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Private Room' and selected_Review_Ratings == '>=7'):
        val1 = 'United States'
        val2 = '7'
        val3 = 'Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2, val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                 column_order=("Name", "Cleaning_Fee"),
                 hide_index=True,
                 width=None,
                 column_config={
                     "Name": st.column_config.TextColumn(
                         "Name",
                     ),
                     "Cleaning_Fee": st.column_config.ProgressColumn(
                         "Cleaning_Fee",
                         format="%f",
                         min_value=0,
                         max_value=max(x.Cleaning_Fee),
                     )}
                 )

    elif (selected_Country == 'United States' and selected_Type_Of_Place=='Private Room' and selected_Review_Ratings == '<=6'):
        val1 = 'United States'
        val2 = '6'
        val3='Private room'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )



    elif (selected_Country == 'United States' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '>=7'):
        val1 = 'United States'
        val2 = '7'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'United States' and selected_Type_Of_Place=='Entire home/apt' and selected_Review_Ratings == '<=6'):
        val1 = 'United States'
        val2 = '6'
        val3='Entire home/apt'
        x = Cleaning_Fee_Apt_Bedrooms_By_Country(val1, val2,val3)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'United States' and selected_Review_Ratings == '>=7'):
        val1 = 'United States'
        val2 = '7'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'United States' and selected_Review_Ratings == '<=6'):
        val1 = 'United States'
        val2 = '6'
        x = Cleaning_Fee_Review_Rating_By_Country(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )

    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Shared Room'):
        val1 = 'United States'
        val2 = 'Shared room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Private Room'):
        val1 = 'United States'
        val2 = 'Private room'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'United States' and selected_Type_Of_Place == 'Entire home/apt'):
        val1 = 'United States'
        val2 = 'Entire home/apt'
        x = Cleaning_Fee_By_Room_Type(val1, val2)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
    elif (selected_Country == 'United States'):
        val = 'United States'
        x = Cleaning_Fee_Plot_By_Ctry(val)
        if (x['Name'] == 'No Data available').any():
            st.write(x)
        else:
            st.dataframe(x,
                     column_order=("Name", "Cleaning_Fee"),
                     hide_index=True,
                     width=None,
                     column_config={
                         "Name": st.column_config.TextColumn(
                             "Name",
                         ),
                         "Cleaning_Fee": st.column_config.ProgressColumn(
                             "Cleaning_Fee",
                             format="%f",
                             min_value=0,
                             max_value=max(x.Cleaning_Fee),
                         )}
                     )
