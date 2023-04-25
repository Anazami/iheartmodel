#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:30:47 2023

@author: zoe
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('iheart_model.sav', 'rb'))

def iheart_prediction (data):
    
    #input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

    # change the data to an array
    data_array=np.asarray(data)

    data_arrays = data_array.reshape(1,-1)


    prediction = loaded_model.predict(data_arrays)
    print(prediction)

    if (prediction[0]== 0):
      return'The Person does not have a Heart Disease'
    else:
      return'The Person may have a Heart Disease, The person is advised to visit the doctor'
      
def main():
    st.title('iHeart Web App')
    age = st.number_input('Age of the patient in years: ', step=1, min_value=0)
    sex = st.number_input('Male/Female: ', min_value=0, max_value=1, help ='Male = 0 & Female = 1', step=1)
    cp = st.number_input('chest pain type ([typical angina, atypical angina, non-anginal, asymptomatic]): ', step=1, min_value=0, max_value=3, help ='typical angina = 0, atypical angina = 1, non-anginal = 2, asymptomatic = 3')
    trestbps = st.number_input('resting blood pressure (resting blood pressure (in mm Hg on admission to the hospital)): ', step=1)
    chol = st.number_input('serum cholesterol in mg/dl: ', step=1, min_value=0)
    fbs = st.number_input('if fasting blood sugar > 120 mg/dl: ', step=1, min_value=0, max_value=1, help ='True = 0 & False = 1')
    restecg =st.number_input('resting electrocardiographic results ([normal, stt abnormality, lv hypertrophy]): ', step=1,  min_value=0, max_value=2, help ='normal = 0, stt abnormality = 1, lv hypertrophy = 2')
    thalach = st.number_input('maximum heart rate achieved: ', step=1, min_value=0)
    exang = st.number_input('exercise-induced angina (True/ False): ', step=1, min_value=0, max_value=1, help ='True = 0 & False = 1')
    oldpeak = st.number_input('ST depression induced by exercise relative to rest: ', min_value=0.00)
    slope = st.number_input('the slope of the peak exercise ST segment: ', step=1, min_value=0)
    ca = st.number_input('number of major vessels (0-3) colored by fluoroscopy: ', step=1, min_value=0, max_value=3, help ='0 to 3')
    thal = st.number_input('Thalassemia [normal; fixed defect; reversible defect]: ', step=1, min_value=0, max_value=2,help ='normal = 0, fixed defect = 1, reversible defect = 2')

    predict = ''
    
    if st.button ('Check Heart Condition'):
        predict = iheart_prediction([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
    st.success(predict)
    
    
if __name__ == '__main__':
    main()

