## For run code
## python -m streamlit run apps.py

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load('flight_price_model.pkl')

# Define categorical options (must match training data)
airlines = ['IndiGo', 'Air India', 'Vistara', 'SpiceJet']
sources = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai']
destinations = ['Cochin', 'Hyderabad', 'Kolkata', 'New Delhi']
total_stops_options = ['0 stops', '1 stop', '2 stops', '3 stops', '4 stops']

# Load feature names from a saved CSV or manually define them
feature_columns = [
    'Airline_IndiGo', 'Airline_Air India', 'Airline_Vistara', 'Airline_SpiceJet',
    'Source_Delhi', 'Source_Mumbai', 'Source_Kolkata', 'Source_Chennai',
    'Destination_Cochin', 'Destination_Hyderabad', 'Destination_Kolkata', 'Destination_New Delhi',
    'Total_Stops_0 stops', 'Total_Stops_1 stop', 'Total_Stops_2 stops', 'Total_Stops_3 stops', 'Total_Stops_4 stops'
]

# Streamlit UI
st.title("Flight Price Prediction")

# User Inputs
selected_airline = st.selectbox("Select Airline", airlines)
selected_source = st.selectbox("Select Source", sources)
selected_destination = st.selectbox("Select Destination", destinations)
selected_total_stops = st.selectbox("Total Stops", total_stops_options)

if st.button("Predict Price"):
    # Create an empty feature vector
    input_data = pd.DataFrame(np.zeros((1, len(feature_columns))), columns=feature_columns)

    # Set categorical features to 1
    if f'Airline_{selected_airline}' in input_data.columns:
        input_data[f'Airline_{selected_airline}'] = 1
    if f'Source_{selected_source}' in input_data.columns:
        input_data[f'Source_{selected_source}'] = 1
    if f'Destination_{selected_destination}' in input_data.columns:
        input_data[f'Destination_{selected_destination}'] = 1
    if f'Total_Stops_{selected_total_stops}' in input_data.columns:
        input_data[f'Total_Stops_{selected_total_stops}'] = 1

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display the predicted price
    st.write(f"**Predicted Flight Price: ₹{prediction:,.2f}**")
