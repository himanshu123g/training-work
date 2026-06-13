import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Today's task",page_icon="🚨",layout="centered")
st.title("9 February Task")

c1,c2,c3=st.columns([1,2,1])
with c1:
    st.title("Welcome to AI Learning Hub")
    st.markdown("### What is AI?")
    st.write("Artificial Intelligence (AI) is transforming the way the world works. From smart assistants and recommendation systems to self-driving cars and medical diagnosis, AI is shaping the future of every industry.")
    st.write("At AI Learning Hub, we help students and professionals understand the core concepts of Artificial Intelligence, Machine Learning, Deep Learning, and Generative AI in a simple and practical way.")
    st.markdown("""
                #### Why learn AI !" 
    - High demand career oportunities." 
    - Competetive salaries" 
    - Future ready skills.""")
    st.audio("audio.mp3")
with c2:
    with st.form("REG"):
        st.markdown("**Registration Page**")
        name=st.text_input("Enter your name",placeholder="Alex")
        email=st.text_input("Enter the Email",placeholder="ABC@gmail.com")
        mobile=st.number_input("Enter your 10 digit Mobile Number")
        age=st.number_input("Enter your age",min_value=18,max_value=60)
        qualification=st.selectbox("Enter your highest Qualification",options=["Masters","Becholers","12th","10th"])
        skills=st.multiselect("Select your skills",options=["Listening","Music","Drinking","Eating","Yeah","Screening"])
        rating=st.slider("Please rate us",min_value=0,max_value=10)
        gender=st.radio("Select your gender",("Male","Female","Harshdeep Maan"))
        file=st.file_uploader("Please submit your aadhar card")
        checkbox=st.checkbox("Make sure you should agree to our terms and conditions")
        submit=st.form_submit_button("Submit")
        
    if submit:
        if name and email and mobile:
            st.balloons()
            st.success("We successfully got your data.")
        else:
            st.warning("Please fill atleast name email and mobile.")

with c3:
    st.title("C3 contains video and image")
    st.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")
    st.audio("audio.mp3")