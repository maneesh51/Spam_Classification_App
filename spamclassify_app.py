# -*- coding: utf-8 -*-
"""
Created on 18.04.2022

@author: Manish Yadav
"""

# -*- coding: utf-8 -*-
"""
Created on 17.04.2022

@author: Manish Yadav https://github.com/maneesh51
"""

import streamlit as st
from annotated_text import annotated_text
import pickle


st.write("""      
# Spam classification App

#### This app will predict if the provided text is a spam or a ham i.e not a spam.
       
 """     )

st.sidebar.header('User Input Features')

### input text
text_input = st.text_area("Type your message below:")


### Reading saved classification model

clf_randomforest = pickle.load(open('spam_clf_randomforest.pkl', 'rb'))
clf_svm = pickle.load(open('spam_clf_svm.pkl', 'rb'))

### using this model to make predications
prediction_rf = clf_randomforest.predict([text_input])
prediction_prob_rf = clf_randomforest.predict_proba([text_input])

prediction_svm = clf_svm.predict([text_input])
prediction_prob_svm = clf_svm.predict_proba([text_input])



###############################################################################
selected_model = st.sidebar.selectbox("Select a pre-trained model", options=["Random forest", "Support Vector Machine (SVM)"])

if selected_model=='Random forest':
    predictions = prediction_rf
    prediction_prob = prediction_prob_rf 

if selected_model=='Support Vector Machine (SVM)':
    predictions = prediction_svm
    prediction_prob = prediction_prob_svm

predict = st.checkbox("Make prediction")

if predict:
    st.markdown("---")
    if (predictions[0]=='spam'):
        predic_pcent = prediction_prob[0][1]*100
        st.write("This message is a spam message. There are {:.2f}% chances that this message is a spam.".format(predic_pcent))
        
        
    if (predictions[0]=='ham'):
        predic_pcent = prediction_prob[0][1]*100
        st.write("This message is not a spam. There are only {:.2f}% chances that this message is a spam.".format(predic_pcent))
        
    st.markdown("---")


    
    
    
    
    
