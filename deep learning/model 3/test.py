import streamlit as st
import tensorflow
from tensorflow.keras import datasets, layers
from keras.layers import Dense
from tensorflow import keras
from tensorflow.keras.datasets import cifar10
import numpy as np

st.set_page_config(page_icon="fire",page_title="Sada Model",layout="centered")
(x_train,y_train),(x_test,y_test)=cifar10.load_data()
model=keras.models.load_model("Test.h5")
st.title("Cifar-10 Image Classifier")
with st.form("Form"):
    image_number=st.number_input("Enter the Random number between 0-9999",min_value=0,max_value=9999,step=1)
    classes=["plane","automobile",'bird',"cat","deer","dog","frog", "horse","ship","truck"]
    submit=st.form_submit_button("Submitttttt !!!!!!")
    if submit:
        image=x_test[image_number]
        asli_image=st.image(image,width=500)
        image=image.reshape(1,32,32,3)
        prediction=model.predict(image)

        predicted_class=st.write("The predicted Class is :- ",classes[np.argmax(prediction)])
        actual_class=st.write("The actual Class is :- ",classes[y_test[image_number][0]])