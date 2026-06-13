import streamlit as st
st.set_page_config(page_icon="😮‍💨",page_title="Prediction")

import pickle
import pandas as pd

actual_model=pickle.load(open("knn.pkl","rb"))
actual_scalar=pickle.load(open("scalar.pkl","rb"))

st.title("THIS IS YOUR PREDICTION MODEL")



with st.form("Form"):

    Gender=st.selectbox("Enter the Gender :- ",["Male","Female"])
    Age=st.number_input("Enter your age :- ",min_value=18)
    Salary=st.number_input("Enter the Salary :- ")

    if Gender=="Male":
        Gender=0
    else:
        Gender=1

    if st.form_submit_button("Submit Your Data"):
        new_data=pd.DataFrame([{"Gender":Gender,"Age":Age,"EstimatedSalary":Salary}])
        
        new_data=actual_scalar.transform(new_data)
        result=actual_model.predict(new_data)

        if result[0]==0:
            st.error("User did NOT purchase the product")
            st.snow()
        else:
            st.success("User WILL purchase the product.")
            st.balloons()