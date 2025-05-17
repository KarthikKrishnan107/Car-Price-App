
import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("Model 1.pkl")

st.title("Car Price Prediction App")
st.write("Fill the details below to predict the car price:")

# User inputs
location = st.selectbox("Location", ['Bangalore', 'Chennai', 'Coimbatore', 'Delhi', 'Hyderabad',
                                     'Jaipur', 'Kochi', 'Kolkata', 'Mumbai', 'Pune'])

year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, value=2015)
km_driven = st.number_input("Kilometers Driven")
fuel = st.selectbox("Fuel Type", ['Diesel', 'LPG', 'Petrol'])
transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])
owner_type = st.selectbox("Owner Type", ['First', 'Second', 'Third', 'Fourth & Above'])
mileage = st.number_input("Mileage")
engine = st.number_input("Engine (CC)")
power = st.number_input("Power (bhp)")
seats = st.number_input("Seats", min_value=2, max_value=10, step=1)

# One-hot encoding manually (just like get_dummies)
input_dict = {
    'Year': year,
    'Kilometers_Driven': km_driven,
    'Mileage': mileage,
    'Engine': engine,
    'Power': power,
    'Seats': seats,

    # Location
    'Location_Bangalore': 1 if location == 'Bangalore' else 0,
    'Location_Chennai': 1 if location == 'Chennai' else 0,
    'Location_Coimbatore': 1 if location == 'Coimbatore' else 0,
    'Location_Delhi': 1 if location == 'Delhi' else 0,
    'Location_Hyderabad': 1 if location == 'Hyderabad' else 0,
    'Location_Jaipur': 1 if location == 'Jaipur' else 0,
    'Location_Kochi': 1 if location == 'Kochi' else 0,
    'Location_Kolkata': 1 if location == 'Kolkata' else 0,
    'Location_Mumbai': 1 if location == 'Mumbai' else 0,
    'Location_Pune': 1 if location == 'Pune' else 0,

    # Fuel_Type
    'Fuel_Type_Diesel': 1 if fuel == 'Diesel' else 0,
    'Fuel_Type_LPG': 1 if fuel == 'LPG' else 0,
    'Fuel_Type_Petrol': 1 if fuel == 'Petrol' else 0,

    # Transmission
    'Transmission_Manual': 1 if transmission == 'Manual' else 0,

    # Owner_Type
    'Owner_Type_Fourth & Above': 1 if owner_type == 'Fourth & Above' else 0,
    'Owner_Type_Second': 1 if owner_type == 'Second' else 0,
    'Owner_Type_Third': 1 if owner_type == 'Third' else 0,
}

# Create input array in correct order
input_order = ['Year', 'Kilometers_Driven', 'Mileage', 'Engine', 'Power', 'Seats',
               'Location_Bangalore', 'Location_Chennai', 'Location_Coimbatore', 'Location_Delhi',
               'Location_Hyderabad', 'Location_Jaipur', 'Location_Kochi', 'Location_Kolkata',
               'Location_Mumbai', 'Location_Pune',
               'Fuel_Type_Diesel', 'Fuel_Type_LPG', 'Fuel_Type_Petrol',
               'Transmission_Manual',
               'Owner_Type_Fourth & Above', 'Owner_Type_Second', 'Owner_Type_Third']

final_input = np.array([[input_dict[col] for col in input_order]])

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(final_input)
    st.success(f"Estimated Car Price: ₹ {round(prediction[0], 2)} lakhs")
