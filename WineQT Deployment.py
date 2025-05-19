#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
import pandas as pd
import joblib

model = joblib.load('wine_quality_model.pkl')


# In[13]:


import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('wine_quality_model.pkl')

st.title("🍷 Wine Quality Prediction App")
st.write("Enter the wine features below:")

fixed_acidity = st.number_input('Fixed Acidity', 0.0, 20.0, step=0.1)
volatile_acidity = st.number_input('Volatile Acidity', 0.0, 2.0, step=0.01)
citric_acid = st.number_input('Citric Acid', 0.0, 1.0, step=0.01)
residual_sugar = st.number_input('Residual Sugar', 0.0, 15.0, step=0.1)
chlorides = st.number_input('Chlorides', 0.0, 1.0, step=0.01)
free_sulfur = st.number_input('Free Sulfur Dioxide', 0.0, 100.0, step=1.0)
total_sulfur = st.number_input('Total Sulfur Dioxide', 0.0, 300.0, step=1.0)
density = st.number_input('Density', 0.9900, 1.0050, step=0.0001, format="%.4f")
pH = st.number_input('pH', 2.0, 4.5, step=0.01)
sulphates = st.number_input('Sulphates', 0.0, 2.0, step=0.01)
alcohol = st.number_input('Alcohol', 5.0, 15.0, step=0.1)

if st.button('Predict Quality'):
    input_data = pd.DataFrame({
        'fixed acidity': [fixed_acidity],
        'volatile acidity': [volatile_acidity],
        'citric acid': [citric_acid],
        'residual sugar': [residual_sugar],
        'chlorides': [chlorides],
        'free sulfur dioxide': [free_sulfur],
        'total sulfur dioxide': [total_sulfur],
        'density': [density],
        'pH': [pH],
        'sulphates': [sulphates],
        'alcohol': [alcohol]
    })

    prediction = model.predict(input_data)
    st.success(f'Predicted Wine Quality: {round(prediction[0], 2)}')


# In[ ]:




