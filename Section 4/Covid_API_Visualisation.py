import pandas as pd
import json
import requests
from datetime import datetime
import streamlit as st

# link to pull the data from
link = 'https://api.covid19api.com/live/country/singapore/status/confirmed'

# api call to recieve data
def getData(url):
    payload={}
    headers = {}
    # entering the api to get information in json format
    response = requests.request("GET", url, headers=headers, data=payload)
    
    result = json.loads(response.text)
    # load data into dataframe format
    df = pd.DataFrame(result)
    return df

# to prevent function from wasting resources
@st.cache
def cleanData(df):
    df_clean = df.reindex(columns = ['Date','Confirmed', 'Deaths'])
    # processed date to datetime
    df_clean['Date'] = pd.to_datetime(df_clean['Date']).dt.date
    # get daily cases based on the culmulative differences between Dates
    df_clean['Daily_Confirmed'] = df_clean['Confirmed'].diff().fillna(0).astype(int)
    df_clean['Daily_Deaths'] = df_clean['Deaths'].diff().fillna(0).astype(int)
    return df_clean

# function to get minimum and maximum date
def getMinMaxDate(df):
    minDate = min(df['Date'])
    maxDate = max(df['Date'])
    return minDate, maxDate

# filter function to return a dataframe to display based on selected options
@st.cache
def filterData(df, start_date, end_date, options = 'Cumulative' ,case_type = 'Cases'):
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)].copy()
    if (case_type == 'Cases') & (options == 'Cumulative'):
        df = df.reindex(columns = ['Date', 'Confirmed']).set_index('Date')
        return df
    if (case_type == 'Cases') & (options == 'Daily'):
        df = df.reindex(columns = ['Date', 'Daily_Confirmed']).set_index('Date')
        return df
    if (case_type == 'Death')  & (options == 'Cumulative') :
        df = df.reindex(columns = ['Date', 'Deaths']).set_index('Date')
        return df
    if (case_type == 'Death')  & (options == 'Daily') :
        df = df.reindex(columns = ['Date', 'Daily_Deaths']).set_index('Date')
        return df
    return


@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

def main():
    df = getData(link)
    # cleaning data and getting additional variables
    df_clean = cleanData(df)
    # getting minimum and maximum date range for calendar selection
    minDate, maxDate = getMinMaxDate(df_clean)
    #Streamlit display
    st.title("Covid19 cases in Singapore")
    st.markdown(f"This Graph shows the culmulative and daily cases from Singapore over a time period. All data collected is pulled from the John Hopkins University repo at '{link}'")
    st.markdown("Change the start date and end date to be filtered down to, change the option to select culmulative or daily")
    # formatting of options
    start_date, end_date, options, kind_of_cases = st.columns(4)
    with start_date:
        start_date = st.date_input('Start date', minDate,min_value = minDate, max_value = maxDate)
    with end_date:
        end_date = st.date_input('End date', maxDate,min_value = minDate, max_value = maxDate)
    with options:
        options = st.radio("View in Cumulative or Daily", ("Cumulative","Daily"))
    with kind_of_cases:
        kind_of_cases = st.radio("View Cases or Death", ("Cases","Death"))
    # displaying charts
    st.markdown(f"Now Showing {options} {kind_of_cases}")
    # filtering data to display and show the data
    st.line_chart(filterData(df_clean,start_date,end_date,options,kind_of_cases),height=500,width =500)

    # displaying the data used
    st.write(df_clean)
    # allow for download of data
    st.download_button("download data as csv", convert_df(df_clean), file_name = f"Covid_data_from_{minDate}_to_{maxDate}.csv", mime='text/csv',)

# run codes
if __name__ == "__main__":
    main()