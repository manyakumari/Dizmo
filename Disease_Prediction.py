import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu('Dizmo!',

                           ['Home','Diabetes',
                            'Heart Disease',
                            'Parkinsons'],
                           menu_icon='hospital-fill',
                           icons=['house','activity', 'heart', 'person'],
                           default_index=0)

    

dlm = pickle.load(open("/Users/manyakumari/Disease Prediction/diabetes_model.sav", 'rb'))
hlm = pickle.load(open("/Users/manyakumari/Disease Prediction/heart_model.sav", 'rb'))
plm = pickle.load(open("/Users/manyakumari/Disease Prediction/parkinsons_model.sav", 'rb'))

if selected == 'Home':
    st.title('Welcome to Dizmo, Doctor!')
    st.write('Please select a calculator from the sidebar')


elif selected == 'Diabetes':
    st.title('Diabetes Prediction Calculator')  
    st.write('Please enter in all data.')
    st.text(" ")
    st.text(" ")
    col1, col2, col3 = st.columns(3)    
    with col1:
         age = st.number_input("Age")
    with col2:
         preg = st.number_input("Number of Pregnancies:")
    with col3:
        bmi = st.number_input("BMI")
    with col1:
        bp = st.number_input("Diastolic Blood Pressure")
    with col2:
        skin = st.number_input("Skin Thickness (mm*100)")
    with col3:
        insulin = st.number_input("Insulin levels")
    with col1:
        gluc = st.number_input("Blood Glucose Level (mg/dL)")
    with col2:
        pedigree = st.number_input("Diabetes Pedigree Score")

    if(st.button('Make Prediction')):
        
        input_data = (preg, gluc, bp, skin, insulin, bmi, pedigree, age)
        input_data_as_np_array = np.array(input_data)
        input_data_reshaped = input_data_as_np_array.reshape(1,-1)
        prediction = dlm.predict(input_data_reshaped)
        if prediction[0] == 1:
            st.error('The patient is likely diabetic.')
        else:
            st.success('The patient is likely not diabetic.')
   

   

elif selected == 'Heart Disease':
    st.title('Heart Disease Prediction Calculator')
    st.write('Please enter in all data.')
    st.text(" ")
    st.text(" ")
    col1, col2, col3 = st.columns(3)    
    with col1:
         age = st.number_input("Age")
    with col2:
         sexcheck = st.radio('Sex',
                  ('female', 'male'))
         if (sexcheck == 'female'):
             sex = 0
         else:       
             sex = 1
    with col3:
        cpcheck = st.radio('Chest Pain Type',
                  ('none/asymptomatic', 'atypical angina', 'non-anginal pain', 'typical angina'))
        if (cpcheck == 'none/asymptomatic'):
             cp = 0
        elif(cpcheck =='atypical angina' ):       
             cp = 1
        elif(cpcheck =='non-anginal pain'):       
             cp = 2
        else:       
             cp = 3
    with col1:
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)")
    with col2:
        chol = st.number_input("Cholestrol (mg/dl)")
    with col3:
         fbscheck = st.radio('Fasting Blood Sugar',
                  ('true', 'false'))
         if (fbscheck == 'true'):
             fbs = 1
         else:       
             fbs = 0
    with col1:
        restecgcheck = st.radio('Resting ECG Results',
                  ('probable/definite left ventricular hypertrophy by Estes criteria', 'normal', 'ST-T wave abnormality'))
        if (restecgcheck == 'probable/definite left ventricular hypertrophy by Estes criteria'):
             restecg = 0
        elif(restecgcheck =='normal' ):       
             restecg = 1
        else:       
             restecg = 2
    with col2:
        thalach = st.number_input("Max Heart Rate")
    with col3:
        exangcheck = st.radio('Exercise Induced Angina',
                  ('true', 'false'))
        if (exangcheck == 'true'):
             exang = 1
        else:       
             exang = 0
    with col1:
        oldpeak = st.number_input("ST Depression Induced By Exercise Relative to Rest")
    with col2:
         slopecheck = st.radio('Slope of Peak Exercise ST Eegment',
                  ('downsloping', 'flat', 'upsloping'))
         if (slopecheck == 'downsloping'):
             slope = 0
         elif(slopecheck =='flat' ):       
             slope = 1
         else:       
             slope = 2
    with col3:
        ca = st.number_input("ST Depression Induced By Exercise Relative to Rest", 0, 3)
    with col1:
        thalcheck = st.radio('Thalassemia',
                  ('fixed defect (no blood flow in some part of the heart)', 'normal blood flow', 'reversible defect (a blood flow is observed but it is not normal)'))
        if (thalcheck == 'fixed defect (no blood flow in some part of the heart)'):
             thal = 1
        elif(thalcheck =='normal blood flow' ):       
             thal = 2
        else:       
             thal = 3
            
    if(st.button('Make Prediction')):
        
        input_data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        input_data_as_np_array = np.array(input_data)
        input_data_reshaped = input_data_as_np_array.reshape(1,-1)
        prediction = hlm.predict(input_data_reshaped)
        print(prediction)
        if prediction[0] == 0:
            st.success('The patient liekly does not have heart disease')
        else:
            st.error('The patient liekly has heart disease')

elif selected == 'Parkinsons':
    st.title('Parkinsons Prediction Calculator')
    st.write('Please enter in all data.')
    st.text(" ")
    st.text(" ")
    col1, col2, col3 = st.columns(3)    
    with col1:
         MDVPFoHz = st.number_input("Average Vocal Fund Freq")
    with col2:
         MDVPFhiHz = st.number_input("Maximum Vocal Fund Freq")
    with col3:
         MDVPFloHz = st.number_input("Minimum Vocal Fund Freq")
    with col1:
         MDVPJitterperc = st.number_input("Measure of Variation in Fund Freq 1")
    with col2:
         MDVPJitterAbs = st.number_input("Measure of Variation in Fund Freq 2")
    with col3:
         MDVPrap = st.number_input("Measure of Variation in Fund Freq 3")
    with col1:
         MDVPppq = st.number_input("Measure of Variation in Fund Freq 4")
    with col2:
         JitterDDP = st.number_input("Measure of Variation in Fund Freq 5")
         
    with col3:
         MDVPShimmer = st.number_input("Measure of Variation in Amp 1")
    with col1:
         MDVPShimmerdB = st.number_input("Measure of Variation in Amp 2")
    with col2:
         MShimmerAPQ3 = st.number_input("Measure of Variation in Amp 3")
    with col3:
         ShimmerAPQ5 = st.number_input("Measure of Variation in Amp 4")
    with col1:
         MDVPapq = st.number_input("Measure of Variation in Amp 5")
    with col2:
         ShimmerDDA = st.number_input("Measure of Variation in Amp 6")

    with col3:
         nhr = st.number_input("Measure of Ratio of Noise to Tonal Compo in Voice 1 (nhr)")
    with col1:
         hnr = st.number_input("Measure of Ratio of Noise to Tonal Compo in Voice 2 (hnr)")
    with col2:
         rpde = st.number_input("Nonlinear Dynamical Complexity Measure 1 (RPDE)")
    with col3:
         d2 = st.number_input("Nonlinear Dynamical Complexity Measure 1 (D2)")
    with col1:
         dfa = st.number_input("Signal fractal scaling exponent")
    with col2:
         spread1 = st.number_input("Nonlinear Measure of Fund Freq Variation 1")
    with col3:
         spread2 = st.number_input("Nonlinear Measure of Fund Freq Variation 2")
    with col1:
         ppe = st.number_input("Nonlinear Measure of Fund Freq Variation 3 (PPE)")

    if(st.button('Make Prediction')):
        
        input_data = (MDVPFoHz, MDVPFhiHz, MDVPFloHz, MDVPJitterperc, MDVPJitterAbs, MDVPrap, MDVPppq, JitterDDP, MDVPShimmer,MDVPShimmerdB, MShimmerAPQ3, ShimmerAPQ5, MDVPapq, ShimmerDDA, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe )
        input_data_as_np_array = np.array(input_data)
        input_data_reshaped = input_data_as_np_array.reshape(1,-1)
        prediction = plm.predict(input_data_reshaped)
        if (prediction[0] == 0):
             st.success("The patient likely does not have Parkinsons")
        else:
            st.error("The patient likely has Parkinsons.")

