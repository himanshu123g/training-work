import streamlit as st
#pip install base64
import base64
import requests
# def encode_image_to_base64(file_path):
#     """Reads an image file and encodes it as a Base64 string."""
#     with open(file_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode()
# img=encode_image_to_base64("image.png")


# background_style = f"""
# <style>
# [data-testid="stAppViewContainer"] {{
#     background-image: url("data:image/png;base64,{img}");
#     background-size: cover;
# }}
# </style>
# """
# st.markdown(background_style, unsafe_allow_html=True)

# with st.form("REG"):
#     c1,c2=st.columns(2)#div form in 2 equal parts
#     # c1,c2,c3=st.columns(3) div form in 3 equal parts
#     # c1,c2,c3=st.columns([3:2:4]) div form in 3 parts of ratio 3:2:4
#     with c1:
#         name=st.text_input("Enter your name")
#         email=st.text_input("Enter your email",placeholder="Eg ABC@gmail.com")
#         password=st.text_input("Enter password",type="password")
#         Age=st.number_input("Enter your Age",min_value=18,max_value=100)
#         dob=st.date_input("Enter your date of birth")
#         time=st.time_input("Enter your time")
        
#     with c2:
#         color=st.color_picker("Select your fav colour")
#         rating=st.slider("Enter your rating",min_value=0,max_value=10)
#         gender=st.radio("Select your gender",("Male","Female","Other"))
#         city=st.selectbox("Select your city",options=["Jalandhar","Chennai","Delhi","Mumbai","Kolkata"])
#         lang=st.multiselect("Select your language",options=["Python","Java","C","C++","C#"])
#         image=st.file_uploader("Upload your image")
#     about=st.text_area("About yourself")
#     btn=st.form_submit_button("Submit")





# url = "https://news-api14.p.rapidapi.com/v2/search/publishers"
# topic=st.selectbox("Select your topic",options=["politics","business","entertainment","health","science","sports","technology"])

# querystring = {"query":topic}

# headers = {
# 	"x-rapidapi-key": "51f15210e3msh9fba2736ccb3f5fp17a364jsnc729ab45aca2",
# 	"x-rapidapi-host": "news-api14.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# # print(response.json())
# # st.write(response.json()["data"])

# x=1
# for i in response.json()["data"]:
#     st.write(x,i["title"])
#     x=x+1




a=st.text_input("Enter your prompt")
btn=st.button("Submit")
if btn:
    url = "https://ai-text-to-image-generator-flux-free-api.p.rapidapi.com/aaaaaaaaaaaaaaaaaiimagegenerator/quick.php"

    payload = {
        "prompt": a,
        "style_id": 4,
        "size": "1-1"
    }
    headers = {
        "x-rapidapi-key": "51f15210e3msh9fba2736ccb3f5fp17a364jsnc729ab45aca2",
        "x-rapidapi-host": "ai-text-to-image-generator-flux-free-api.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    # print(response.json())
    st.write(response.json())