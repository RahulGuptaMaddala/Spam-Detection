# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:29:57 2023

@author: Mounika
"""

import pandas as pd
import numpy as np
import pickle
import streamlit as st


loaded_model=pickle.load(open("trained_model.sav","rb"))

def spam_prediction(input_data):
    input_mail = ["I've been searching for the right words to thank you for this breather. I promise i wont take your help for granted and will fulfil my promise. You have been wonderful and a blessing at all times"]
    input_data_features = feature_extraction.transform(input_mail)
    prediction = model.predict(input_data_features)
    print(prediction)
    if (prediction[0]==1):
        print('Ham mail')
    else:
        print('Spam mail')
        
        
def main():
    st.title('Spam detection')
    Category = st.text_input('Number of Category')
    Message = st.text_input('Name of Message')
    
    diagnosis=""
    
    if st.button("Diabetes Test Result"):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    


if __name__=='__main__':
    main()
