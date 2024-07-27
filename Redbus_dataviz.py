import streamlit as st 
import pandas as pd 
from streamlit_dynamic_filters import DynamicFilters
import sqlalchemy
import mysql.connector

r=st.sidebar.radio('Main Menu',['Home','Select the Bus'])

client=mysql.connector.connect(host="localhost",user="root",password="Shivani2020",database="redbusdatabase",port=3306)
redbus=client.cursor()
    

if r == 'Home':
    st.title('REDBUS DATA VISUALIZATION')
    st.subheader("Data has been scraped from the Redbus website and presented for your usage")
    st.markdown("*you can browse the Redbus website data here* :sunglasses:")
    st.image("C:/Users/hp/Desktop/Redbuslogo.png")

elif r=='Select the Bus':
    sql_query=pd.read_sql_query("select * from bus_routes",client)
    
    df=pd.DataFrame(sql_query,columns=['id','route_name', 'route_link', 'busname', 'bustype', 'departing_time', 'duration', 'reaching_time', 'star_rating', 'price', 'seats_available'])
    
    # Convert 'Departure Time' to string and extract the time part
    df['departing_time'] = df['departing_time'].astype(str)
    df['departing_time'] = df['departing_time'].apply(lambda timeValue: str(timeValue).split()[-1])
    
    # Convert 'Arrival Time' to string and extract the time part
    df['reaching_time'] = df['reaching_time'].astype(str)
    df['reaching_time'] = df['reaching_time'].apply(lambda timeValue: str(timeValue).split()[-1])
    dynamic_filters = DynamicFilters(df=df, filters=['route_name', 'busname', 'bustype', 'star_rating', 'departing_time', 'price'])
    dynamic_filters.display_filters(location='columns', num_columns=3, gap='large')
    dynamic_filters.display_df()
