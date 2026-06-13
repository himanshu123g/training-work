import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_icon="🚨",page_title="My Registration Page",layout="centered")
st.title("Registration Page")


# with st.form("REG"):
#     name=st.text_input("Enter your name")
#     email=st.text_input("Enter your email",placeholder="ABC@gmail.com")
#     password=st.text_input("Enter the password",type="password")
#     age=st.number_input("Enter the age",min_value=18,max_value=60)
#     dob=st.date_input("Enter the date of birth")
#     time=st.time_input("Enter the time")
#     color=st.color_picker("Enter the color")
#     rating=st.slider("Select the rating",min_value=0,max_value=10)
#     gender=st.radio("Enter the gender",("Male","Female","Harshdeep"))
#     city=st.selectbox("Enter the city",options=["jalandhar","Delhi","Chennai"])
#     lang=st.multiselect("Enter your languages",options=["English","Hindi","Punjabi"])
#     image=st.file_uploader("Upload your image")
#     about=st.text_area("About Yourself")
#     btn=st.form_submit_button("Submit")
#     if btn:
#         if name and email:
#             st.write("Now we are phishing!",name)
#             st.balloons()
#             st.snow()
#         else:
#             st.warning("Kindly fill all the options.")


# with st.form("REG"):
#     c1,c2=st.columns(2)
#     with c1:
#         name=st.text_input("Enter your name")
#         email=st.text_input("Enter your email",placeholder="ABC@gmail.com")
#         password=st.text_input("Enter the password",type="password")
#         age=st.number_input("Enter the age",min_value=18,max_value=60)
#         dob=st.date_input("Enter the date of birth")
#         time=st.time_input("Enter the time")
#     with c2:
#         color=st.color_picker("Enter the color")
#         rating=st.slider("Select the rating",min_value=0,max_value=10)
#         gender=st.radio("Enter the gender",("Male","Female","Harshdeep"))
#         city=st.selectbox("Enter the city",options=["jalandhar","Delhi","Chennai"])
#         lang=st.multiselect("Enter your languages",options=["English","Hindi","Punjabi"])
#         image=st.file_uploader("Upload your image")
#         about=st.text_area("About Yourself")
#         btn=st.form_submit_button("Submit")
# if btn:
#     if name and email:
#         st.write("Now we are phishing!",name)
#         st.balloons()
#         st.snow()
#     else:
#         st.warning("Kindly fill all the options.")




# t1,t2,t3=st.tabs(["Register","Login","Home"])
# with t1:
#     st.title("REGISTRATION PAGE IN TAB 1")
#     with st.form("REG"):
#         c1,c2=st.columns(2)
#         with c1:
#             name=st.text_input("Enter your name")
#             email=st.text_input("Enter your email",placeholder="ABC@gmail.com")
#             password=st.text_input("Enter the password",type="password")
#             age=st.number_input("Enter the age",min_value=18,max_value=60)
#             dob=st.date_input("Enter the date of birth")
#             time=st.time_input("Enter the time")
#         with c2:
#             color=st.color_picker("Enter the color")
#             rating=st.slider("Select the rating",min_value=0,max_value=10)
#             gender=st.radio("Enter the gender",("Male","Female","Harshdeep"))
#             city=st.selectbox("Enter the city",options=["jalandhar","Delhi","Chennai"])
#             lang=st.multiselect("Enter your languages",options=["English","Hindi","Punjabi"])
#             image=st.file_uploader("Upload your image")
#             about=st.text_area("About Yourself")
#             btn=st.form_submit_button("Submit")
#     if btn:
#         if name and email:
#             st.write("Now we are phishing!",name)
#             st.balloons()
#             st.snow()
#         else:
#             st.warning("Kindly fill all the options.")
# with t2:
#     with st.form("Login"):
#         st.title("LOGIN ON TAB 2")
#         email=st.text_input("Enter your email",placeholder="ABC@gmail.com")
#         password=st.text_input("Enter the password",type="password")
#         btn=st.form_submit_button("Submit")
#         if btn:
#             if email and password:
#                 st.success("Success Man!")
#             else:
#                 st.warning("kindly fill all.")
# with t3:
#     st.title("IMAGE ON TAB 3")
#     st.header("This is the image given below")
#     st.image("image.png")



# with st.sidebar:
#     st.write("This is sidebar")
#     bt1=st.button("Register")
#     bt2=st.button("Login")
#     bt3=st.button("Home")

# if bt1:
#     st.title("Register")
    
#     with st.form("REG"):
#         c1,c2=st.columns(2)
#         with c1:
#             name=st.text_input("Enter your name")
#             email=st.text_input("Enter your email",placeholder="Eg ABC@gmail.com")
#             password=st.text_input("Enter password",type="password") 
#         with c2:
#             color=st.color_picker("Select your fav colour")
#             rating=st.slider("Enter your rating",min_value=0,max_value=10)
#             gender=st.radio("Select your gender",("Male","Female","Other"))
#         about=st.text_area("About yourself")
#         btn=st.form_submit_button("Submit")
#     if btn:
#         if name and email and password:
#             st.success("Registration successful")
#             st.write(name)
#             st.balloons()
#         else:
#             st.error("Please fill the required values")
# elif bt2:
#     st.title("Login page")
#     with st.form("login"):
#         email=st.text_input("Enter Email")
#         password=st.text_input("Enter password",type="password")
#         btn=st.form_submit_button("submit")
#     if btn:
#         st.write("DONE")
# elif bt3:
#     st.title("Home")
#     st.image("image.png")



opt=option_menu("Menu",options=["Register","Login","Home"],icons=["person",'person','house'],orientation="horizontal")
if opt=="Register":
    st.title("Register")
    
    with st.form("REG"):
        c1,c2=st.columns(2)
        with c1:
            name=st.text_input("Enter your name")
            email=st.text_input("Enter your email",placeholder="Eg ABC@gmail.com")
            password=st.text_input("Enter password",type="password")
            
        with c2:
            color=st.color_picker("Select your fav colour")
            rating=st.slider("Enter your rating",min_value=0,max_value=10)
            gender=st.radio("Select your gender",("Male","Female","Other"))
        about=st.text_area("About yourself")
        btn=st.form_submit_button("Submit")

    if btn:
        if name and email and password:
            st.success("Registration successful")
            st.write(name)
            st.balloons()
        else:
            st.error("Please fill the required values")

elif opt=="Login":
    st.title("Login page")
    with st.form("login"):
        email=st.text_input("Enter Email")
        password=st.text_input("Enter password",type="password")
        btn=st.form_submit_button("submit")
    if btn:
        st.write("DONE")

elif opt=="Home":
    st.title("Home")
    st.image("image.png")