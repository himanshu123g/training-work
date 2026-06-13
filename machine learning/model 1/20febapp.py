import pickle
import streamlit as st
import pandas as pd

our_scalar=pickle.load(open("scalar.pkl","rb"))
our_encoder=pickle.load(open("encoder.pkl","rb"))
our_model=pickle.load(open("model.pkl","rb"))

st.title("THIS IS THE PROPER HOUSE PRICE PREDICTION")
st.write("Please Enter all the required details below *")

area=st.number_input("Enter the area :- ",min_value=0)
bedrooms=st.number_input("Enter the bedrooms :- ",min_value=0)
bathrooms=st.number_input("Enter the bathrooms :- ",min_value=0)
stories=st.number_input("Enter the stories :- ",min_value=0)
mainroad=st.selectbox("Enter the mainroad yes(1) or no(0):- ",[0,1])
guestroom=st.selectbox("Enter the guestroom yes(1) or no(0):- ",[0,1])
basement=st.selectbox("Enter the basement yes(1) or no(0):- ",[0,1])
hotwaterheating=st.selectbox("Enter the water heater yes(1) or no(0):- ",[0,1])
airconditioning=st.selectbox("Enter the water air conditioner yes(1) or no(0):- ",[0,1])
parking=st.number_input("Enter the parking ",min_value=0)
prefarea=st.selectbox("Enter the prefarea :- ",[0,1])
furnishingstatus=st.selectbox("Enter the furnishingstatus(furnished/semi-furnished/unfurnished) :- ",["furnished","semi-furnished","unfurnished"])

if st.button("Submit"):
    new_pred=pd.DataFrame([{"area":area
                    ,"bedrooms":bedrooms,
                    "bathrooms":bathrooms,
                    "stories":stories,
                    'mainroad':mainroad,
       'guestroom':guestroom, 'basement':basement, 'hotwaterheating':hotwaterheating, 'airconditioning':airconditioning,
       'parking':parking, 'prefarea':prefarea, 'furnishingstatus':furnishingstatus}])
    
    ohe=our_encoder.transform(new_pred[["furnishingstatus"]])
    new_pred=new_pred.drop(columns="furnishingstatus")
    new_pred[our_encoder.get_feature_names_out()]=ohe

    new_pred=our_scalar.transform(new_pred)

    prediction=our_model.predict(new_pred)

    
    st.success(f"Your price is :- ₹ {int(prediction[0])}")
    st.balloons()
    st.snow()