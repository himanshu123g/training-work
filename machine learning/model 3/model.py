import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_icon="❤️",page_title="New Model")
import pickle
our_model=pickle.load(open("SadaModel.pkl","rb"))
our_scalar=pickle.load(open("scalar.pkl","rb"))

st.title("This is our Cancer Prediction Model")

with st.form("Form"):
    st.subheader("Enter the values for the diagnosis.")
    radius_mean=st.number_input("Enter the mean radius :- ")
    texture_mean=st.number_input("Enter the texture mean :- ")
    perimeter_mean=st.number_input("Enter the perimeter mean :- ")
    area_mean=st.number_input("Enter the area mean :- ")
    smoothness_mean=st.number_input("Enter the smoothness mean :- ")
    compactness_mean=st.number_input("Enter the compactness mean :- ")
    concavity_mean=st.number_input("Enter the concavity mean :- ")
    concave_points_mean=st.number_input("Enter the concave points mean :- ")                             #concave points_mean
    symmetry_mean=st.number_input("Enter the symmetry mean :- ")
    fractal_dimension_mean=st.number_input("Enter the fractal dimension mean :- ")
    radius_se=st.number_input("Enter the radius se :- ")
    texture_se=st.number_input("Enter the texture_se :- ")
    perimeter_se=st.number_input("Enter the perimeter se :- ")
    area_se=st.number_input("Enter the area se :- ")
    smoothness_se=st.number_input("Enter the smoothness se :- ")
    compactness_se=st.number_input("Enter the compactness se :- ")
    concavity_se=st.number_input("Enter the concavity se :- ")
    concave_points_se=st.number_input("Enter the concave points se :- ")
    symmetry_se=st.number_input("Enter the symmetry se :- ")
    fractal_dimension_se=st.number_input("Enter the fractal dimension se :- ")
    radius_worst=st.number_input("Enter the radius worst :- ")
    texture_worst=st.number_input("Enter the texture worst :- ")
    perimeter_worst=st.number_input("Enter the perimeter worst :- ")
    area_worst=st.number_input("Enter the area worst :- ")
    smoothness_worst=st.number_input("Enter the smoothness worst :- ")
    compactness_worst=st.number_input("Enter the compactness worst :- ")
    concavity_worst=st.number_input("Enter the concavity worst :- ")
    concave_points_worst=st.number_input("Enter the concave points worst :- ")
    symmetry_worst=st.number_input("Enter the symmetry worst :- ")
    fractal_dimension_worst=st.number_input("Enter the fractal dimension worst :- ")

    if st.form_submit_button("submit"):
        newdata=pd.DataFrame([{'radius_mean':radius_mean, 'texture_mean':texture_mean, 'perimeter_mean':perimeter_mean,
        'area_mean':area_mean, 'smoothness_mean':smoothness_mean, 'compactness_mean':compactness_mean, 'concavity_mean':concavity_mean,
        'concave points_mean':concave_points_mean, 'symmetry_mean':symmetry_mean, 'fractal_dimension_mean':fractal_dimension_mean,
        'radius_se':radius_se, 'texture_se':texture_se, 'perimeter_se':perimeter_se, 'area_se':area_se, 'smoothness_se':smoothness_se,
        'compactness_se':compactness_se, 'concavity_se':concavity_se, 'concave points_se':concave_points_se, 'symmetry_se':symmetry_se,
        'fractal_dimension_se':fractal_dimension_se, 'radius_worst':radius_worst, 'texture_worst':texture_worst,
        'perimeter_worst':perimeter_worst, 'area_worst':area_worst, 'smoothness_worst':smoothness_worst,
        'compactness_worst':compactness_worst, 'concavity_worst':concavity_worst, 'concave points_worst':concave_points_worst,
        'symmetry_worst':symmetry_worst, 'fractal_dimension_worst':fractal_dimension_worst}])
        
        newdata=our_scalar.transform(newdata)
        model=our_model.predict(newdata)

        if model[0]==0:
            st.error("⚠ Malignant Tumor Detected")
        else:
            st.success("Benign Tumor.")