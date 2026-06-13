import streamlit as st

st.set_page_config(layout="centered",page_title="Meri Class",page_icon="🏛️")
st.title("this is the fastest way")
st.write("Hello World")
st.header("This is header")
st.subheader("This is subheader")
st.text("This is text")
st.code("print('Hello World')")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k = (a(r^{n-1} - 1)) / (r - 1)
''')
st.success("You are enginner!")
st.error("But prompt enginner")
st.warning("But still have chances to get a job!")
st.info("Hey can u tell me what should i do!")
st.page_link("https://www.youtube.com/",label="Click to open youtube.")
st.markdown("This is markdown.")
st.image("image.png")

name=st.text_input("Enter your name")
email=st.text_input("Enter the email",placeholder="ABC@gmail.com")
password=st.text_input("Enter the password",type="password")
age=st.number_input("Enter the age",min_value=10,max_value=100)
dob=st.date_input("Enter your date of birth")
time=st.time_input("Enter the time")
color=st.color_picker("Select your favourite color")
rating=st.slider("Enter the rating",min_value=0,max_value=10)
gender=st.radio("Select your Gender",("Male","Female","Other"))
city=st.selectbox("Enter the City",options=["Jalandhar","Chennai","Delhi"])
lang=st.multiselect("Enter your languages",options=["English","Hindi","Punjabi","Maths","SST"])
image=st.file_uploader("Drop your Image")
about=st.text_area("About Yourself")
btn=st.button("Submit")
if btn:
    if name and email and password and dob and age and time and color and rating and gender and city and lang and image and about:
        st.write("Now we are phishing!",name)
        st.balloons()
        st.snow()
    else:
        st.warning("Kindly fill all the options.")