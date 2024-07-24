!pip install scikit-learn
import streamlit as st
import pickle
import pandas as pd
import numpy as np


with open('truck_classification_rfc.pkl','rb') as file:
    model = pickle.load(file)

with open('encoder.pkl','rb') as file:
    encoder = pickle.load(file)

with open('scalar.pkl','rb') as file:
    scalar = pickle.load(file)

def prediction(numcols,catcols):

    cat_encoded = encoder.transform([catcols])
    num_scaled = scalar.transform([numcols])

    all_cols = np.concatenate((num_scaled,cat_encoded),axis=1)

    prob = model.predict_proba(all_cols)

    return prob[:,1][0]
def main():
    st.image('transport-logistics-products.jpg',use_column_width=True)
    st.title('TRUCK DELAY PREDICTION')

    route_avg_temp =  st.text_input('Enter Avg Temp of Route in Deg F')
    route_avg_wind = st.text_input('Enter Avg Wind speed of Route in MPH')
    route_avg_precip = st.text_input('Enter Avg Precipitation of Route in inches')
    route_avg_humidity = st.text_input('Enter Avg Humidity of Route')
    route_avg_visibility = st.text_input('Enter Avg Visibility of Route in Miles')
    route_avg_pressure = st.text_input('Enter Avg pressure of Route in mBar')
    origin_avg_temp =  st.text_input('Enter Avg Temp of Origin Deg F')
    origin_avg_wind = st.text_input('Enter Avg Wind speed of Origin in MPH')
    origin_avg_precip = st.text_input('Enter Avg Precipitation of Origin in inches')
    origin_avg_humidity = st.text_input('Enter Avg Humidity of Origin')
    origin_avg_visibility = st.text_input('Enter Avg Visibility of Origin in Miles')
    origin_avg_pressure = st.text_input('Enter Avg pressure of Origin mBar')
    dest_avg_temp =  st.text_input('Enter Avg Temp of Destination Deg F')
    dest_avg_wind = st.text_input('Enter Avg Wind speed of Destination MPH')
    dest_avg_precip = st.text_input('Enter Avg Precipitation of Destination in inches')
    dest_avg_humidity = st.text_input('Enter Avg Humidity of Destination')
    dest_avg_visibility = st.text_input('Enter Avg Visibility of Destination in Miles')
    dest_avg_pressure = st.text_input('Enter Avg pressure of Destination in mBar')
    avg_nov = st.text_input('Enter Avg No. Of Vehicles on Route')
    accident = (lambda x:1 if x=='Yes' else 0)(st.selectbox('Are there any Accidents on routes?',['Yes','No']))
    truck_age = st.text_input('Enter the age of truck in Years')
    capacity = st.text_input('Enter the load capacity of truck in Pounds')
    milage = st.text_input('Enter the milage of the truck in MPG')
    age = st.text_input('Enter the age of driver')
    exp = st.text_input('Enter the experience of driver')
    ratings = st.slider('Select the driver rating',min_value=0,max_value=10,step=1)
    speed = st.text_input('Select the avg speed of driver MPH')

    num_inputs = [route_avg_temp,route_avg_wind,route_avg_precip,route_avg_humidity,route_avg_visibility,route_avg_pressure,
                 origin_avg_temp,origin_avg_wind,origin_avg_precip,origin_avg_humidity,origin_avg_visibility,origin_avg_pressure,
                 dest_avg_temp,dest_avg_wind,dest_avg_precip,dest_avg_humidity,dest_avg_visibility,dest_avg_pressure,
                 avg_nov,accident,truck_age,capacity,milage,age,exp,ratings,speed]
    route_desc = st.selectbox('Select the description of route wether',['Clear','Moderate rain' ,'Sunny' ,'Light rain',
    'Patchy light rain with thunder', 'Overcast','Moderate or heavy rain with thunder', 'Partly cloudy',
    'Patchy rain possible' ,'Cloudy', 'Moderate or heavy rain shower','Light rain shower', 'Mist' ,'Moderate or heavy snow showers' ,
    'Light snow','Blowing snow','Light drizzle','Heavy snow','Patchy light rain','Blizzard','Heavy rain','Fog','Patchy light drizzle',
    'Freezing fog','Moderate snow','Torrential rain shower','Thundery outbreaks possible','Patchy light snow','Patchy moderate snow',
    'Light sleet','Moderate rain at times','Light sleet showers','Patchy snow possible','Patchy heavy snow','Moderate or heavy sleet showers',
    'Patchy sleet possible','Moderate or heavy sleet','Moderate or heavy snow with thunder','Moderate or heavy freezing rain',
    'Light freezing rain','Patchy light snow with thunder','Freezing drizzle','Heavy rain at times'])
    
    origin_desc = st.selectbox('Select the description of origin city wether',['Sunny','Partly cloudy','Overcast','Clear','Light snow','Cloudy',
    'Heavy snow','Blizzard','Light drizzle','Light rain shower','Moderate snow','Mist','Moderate rain','Patchy heavy snow'])

    dest_desc = st.selectbox('Select the description of destination city wether',['Sunny','Partly cloudy','Overcast','Clear','Light snow','Cloudy',
    'Heavy snow','Blizzard','Light drizzle','Light rain shower','Moderate snow','Mist','Moderate rain','Patchy heavy snow'])

    fuel_type = st.selectbox('Select the fuel type',['diesel','gas'])
    gender = st.selectbox('Select the gender',['male','unknown','female'])
    driving_style = st.selectbox('Select the driving style of driver',['proactive','conservative','unknown'])

    cat_inputs = [route_desc,origin_desc,dest_desc,fuel_type,gender,driving_style]
    predic = 0
    if st.button('Predict'):
        predic = prediction(num_inputs,cat_inputs)
        st.success(f'The chances of getting delayed is {round(predic,4)*100}%')

if __name__=='__main__': 
    main()
