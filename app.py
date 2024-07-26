import pandas as pd
import streamlit as st
import pickle as pk

# Load the model
try:
    with open('model.pkl', 'rb') as file:
        model = pk.load(file)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Failed to load model: {e}")

# App Header
st.markdown(
    """
    <style>
    .main-header {
        font-size:36px;
        color:white;
        font-weight:bold;
        text-align:center;
    }
    .sidebar .sidebar-content {
        background-color: #F0F2F6;
    }
    </style>
    """, 
    unsafe_allow_html=True
)
st.markdown('<div class="main-header">Car Price Prediction 🚗</div>', unsafe_allow_html=True)

# Load data
cars_data = pd.read_csv('Cardetails.csv')

# Function to extract brand name
def get_brand_name(car_name):
    return car_name.split(' ')[0].strip()

cars_data['name'] = cars_data['name'].apply(get_brand_name)

# Sidebar for input
st.sidebar.header('Customize your car details:')
name = st.sidebar.selectbox('Select car brand', cars_data['name'].unique())
year = st.sidebar.slider('Car manufactured year', 1994, 2024)
km_driven = st.sidebar.slider('Car mileage (km)', 11, 200000)
fuel = st.sidebar.selectbox('Fuel type', cars_data['fuel'].unique())
seller_type = st.sidebar.selectbox('Seller type', cars_data['seller_type'].unique())
transmission = st.sidebar.selectbox('Transmission type', cars_data['transmission'].unique())
owner = st.sidebar.selectbox('Number of owners', cars_data['owner'].unique())
mileage = st.sidebar.slider('Fuel consumption (l/km)', 10, 40)
engine = st.sidebar.slider('Engine capacity (cm^3)', 700, 5000)
max_power = st.sidebar.slider('Max Power (hp)', 0, 200)
seats = st.sidebar.slider('Number of seats', 5, 10)

# Predict button
if st.sidebar.button("Predict"):
    # Prepare input data
    input_data_model = pd.DataFrame(
        [[name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
        columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']
    )

    # Encode categorical features
    input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
                                       'Fourth & Above Owner', 'Test Drive Car'], [1, 2, 3, 4, 5], inplace=True)
    input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
    input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
    input_data_model['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
    input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
                                      'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
                                      'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
                                      'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
                                      'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
                                     list(range(1, 32)), inplace=True)

    # Predict price
    car_price = model.predict(input_data_model)

    # Display prediction
    st.markdown(f'<div style="font-size:24px; text-align:center; margin-top:20px;">Estimated Car Price: <span style="color:#E74C3C;">{car_price[0]:,.2f}</span>₽ </div>', unsafe_allow_html=True)
