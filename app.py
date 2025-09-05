import streamlit as st
import pickle
import numpy as np

# Load model
with open('pumpkin_seeds.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🎃 Pumpkin Seed Classifier By Maruti")

st.write("Enter the following features to predict the seed type:")

# Define all the features used in training
features = ['Area', 'Perimeter', 'Major_Axis_Length', 'Minor_Axis_Length',
            'Convex_Area', 'Equiv_Diameter', 'Eccentricity', 'Solidity',
            'Extent', 'Roundness', 'Aspect_Ration', 'Compactness']

# Collect user input for each feature
user_input = []
for feature in features:
    value = st.number_input(f"{feature}", step=0.01, format="%.4f")
    user_input.append(value)

# Predict on button click
if st.button("Predict"):
    try:
        input_array = np.array([user_input])
        prediction = model.predict(input_array)[0]
        label = 'Ürgüp Sivrisi' if prediction == 1 else 'Çerçevelik'
        st.success(f"🌱 Predicted Seed Class: **{label}**")
    except Exception as e:
        st.error(f"❌ Error in prediction: {e}")
