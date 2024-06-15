from Airbnb_Data.Air_Bnb_Data_Return import Air_Bnb_Data_Return
import pandas as pd

def Data_Extract_In_DF():
    Loc_Data=Air_Bnb_Data_Return()
    All_Data={'Name':[], 'Country':[],'Price':[],'Property_Type':[],'Room_Type':[],'Longitude':[],'Latitude':[],
              'No_Of_Reviews':[],
              'Review_Rating':[],'No_Of_BedRooms':[],'No_Of_BathRooms':[],'No_Of_Beds':[],'Security_Deposit':[],
              'Host_Name':[],'Host_Identity_Verified':[],'Host_Listing_Count':[],'Host_Location':[],'Host_Response_Rate':[],
              'Host_Response_Time':[],'Amenities':[],'Cancellation_Policy':[],'Cleaning_Fee':[],
              'Days_30_Availability':[],'Days_60_Availability':[],'Days_90_Availability':[],'Days_365_Availability':[]
              }
    for z in Loc_Data:
        try:
            Country = z['address']['country']
        except:
            Country = None
        try:
            Longitude = z['address']['location']['coordinates'][0]
        except:
            Longitude = None
        try:
            Latitude = z['address']['location']['coordinates'][1]
        except:
            Latitude = None
        try:
            Name = z['name']
        except:
            Name = None
        try:
            Price = z['price']
        except:
            Price = None
        try:
            Property_Type = z['property_type']
        except:
            Property_Type = None
        try:
            Room_Type = z['room_type']
        except:
            Room_Type = None
        try:
            No_Of_Reviews = z['number_of_reviews']
        except:
            No_Of_Reviews = None
        try:
            Review_Rating = z['review_scores']['review_scores_value']
        except:
            Review_Rating = None
        try:
            No_Of_Beds = z['beds']
        except:
            No_Of_Beds = None
        try:
            No_Of_BathRooms = z['bathrooms']
        except:
            No_Of_BathRooms = None
        try:
            No_Of_BedRooms = z['bedrooms']
        except:
            No_Of_BedRooms = None
        try:
            Security_Deposit = z['security_deposit']
        except:
            Security_Deposit = None
        try:
            Host_Name = z['host']['host_name']
        except:
            Host_Name = None
        try:
            Host_Identity_Verified = z['host']['host_identity_verified']
        except:
            Host_Identity_Verified = None
        try:
            Host_Listing_Count = z['host']['host_total_listings_count']
        except:
            Host_Listing_Count = None
        try:
            Host_Location = z['host']['host_location']
        except:
            Host_Location = None

        try:
            Host_Response_Rate = z['host']['host_response_rate']
        except:
            Host_Response_Rate = None
        try:
            Host_Response_Time = z['host']['host_response_rate']
        except:
            Host_Response_Time = None

        try:
            Amenities = z['amenities']
            Amenities_Final = ','.join(map(str, Amenities))
        except:
            Amenities_Final = None
        try:
            Cancellation_Policy = z["cancellation_policy"]
        except:
            Cancellation_Policy = None
        try:
            Cleaning_Fee = z['cleaning_fee']
        except:
            Cleaning_Fee = None
        try:
            Days_30_Availability = z['availability']['availability_30']
        except:
            Days_30_Availability = None
        try:
            Days_60_Availability = z['availability']['availability_60']
        except:
            Days_60_Availability = None
        try:
            Days_90_Availability = z['availability']['availability_90']
        except:
            Days_90_Availability = None
        try:
            Days_365_Availability = z['availability']['availability_365']
        except:
            Days_365_Availability = None
            ###apedning the data
        All_Data['Longitude'].append(Longitude)
        All_Data['Latitude'].append(Latitude)
        All_Data['Country'].append(Country)
        All_Data['Name'].append(Name)
        All_Data['Price'].append(Price)
        All_Data['Property_Type'].append(Property_Type)
        All_Data['Room_Type'].append(Room_Type)
        All_Data['Review_Rating'].append(Review_Rating)
        All_Data['No_Of_Reviews'].append(No_Of_Reviews)
        All_Data['No_Of_Beds'].append(No_Of_Beds)
        All_Data['No_Of_BathRooms'].append(No_Of_BathRooms)
        All_Data['No_Of_BedRooms'].append(No_Of_BedRooms)
        All_Data['Security_Deposit'].append(Security_Deposit)
        All_Data['Host_Name'].append(Host_Name)
        All_Data['Host_Identity_Verified'].append(Host_Identity_Verified)
        All_Data['Host_Listing_Count'].append(Host_Listing_Count)
        All_Data['Host_Location'].append(Host_Location)
        All_Data['Host_Response_Rate'].append(Host_Response_Rate)
        All_Data['Host_Response_Time'].append(Host_Response_Time)
        All_Data['Amenities'].append(Amenities_Final)
        All_Data['Cancellation_Policy'].append(Cancellation_Policy)
        All_Data['Cleaning_Fee'].append(Cleaning_Fee)
        All_Data['Days_30_Availability'].append(Days_30_Availability)
        All_Data['Days_60_Availability'].append(Days_60_Availability)
        All_Data['Days_90_Availability'].append(Days_90_Availability)
        All_Data['Days_365_Availability'].append(Days_365_Availability)
        Loc_Data_Frame = pd.DataFrame(All_Data)
        ####
    #Loc_Data_Frame.isna().sum()
        ####
    pd.options.mode.chained_assignment = None
    Loc_Data_Frame.No_Of_BedRooms.fillna(Loc_Data_Frame.No_Of_BedRooms.mode()[0], inplace=True)
    Loc_Data_Frame.No_Of_BathRooms.fillna(Loc_Data_Frame.No_Of_BathRooms.mode()[0], inplace=True)
    Loc_Data_Frame.No_Of_Beds.fillna(Loc_Data_Frame.No_Of_Beds.median(), inplace=True)
    Loc_Data_Frame.Security_Deposit.fillna(Loc_Data_Frame.Security_Deposit.median(), inplace=True)
    Loc_Data_Frame.Cleaning_Fee.fillna(Loc_Data_Frame.Cleaning_Fee.median(), inplace=True)
    Loc_Data_Frame.Review_Rating.fillna(Loc_Data_Frame.Review_Rating.median(), inplace=True)
    Loc_Data_Frame.Host_Response_Rate.fillna(Loc_Data_Frame.Host_Response_Rate.median(), inplace=True)
    Loc_Data_Frame.Host_Response_Time.fillna(Loc_Data_Frame.Host_Response_Time.median(), inplace=True)

        ######
    Loc_Data_Frame.Amenities.replace(to_replace='', value='Not Available', inplace=True)


        #####
    #Loc_Data_Frame.isna().sum()

        ######
    #Loc_Data_Frame[Loc_Data_Frame.duplicated()]

        ####
    Loc_Data_Frame.drop(labels=list(Loc_Data_Frame[Loc_Data_Frame.Name.duplicated(keep=False)].index), inplace=True)

        ####

    Loc_Data_Frame.reset_index(drop=True, inplace=True)
    Loc_Data_Frame.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/All_Data_Extraction_DF/All_AirBnbData.csv", index=False)
        #'thumbnails': channel_data['items'][0]['thumbnails']['default']['url']}

    #Loc_Data_Frame.to_csv("/Users/shashankkaundal/Downloads/AirBnbAnalysis/Airbnb_Data/airbnb.csv", index=False)
    #return Location_Data
    return Loc_Data_Frame
#x=Data_Extract_In_DF()
#print(x)

