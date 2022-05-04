import pickle
import streamlit as st
 
@st.cache()
def prediction(seq_len, mole_w, gravy, instab, aromat):
    # loading the trained model
    with open("data,model/prot_classifier.pkl", 'wb') as input_file: 
    # pickle_in = open('data,model/prot_classifier.pkl', 'rb') 
        classifier = pickle.load(input_file)
    
        # Making predictions 
        prediction = classifier.predict( 
            [[seq_len, mole_w, gravy, instab, aromat]])

     
    if prediction == 1:
        pred = 'Disordered'
    else:
        pred = 'Normal'
    return pred