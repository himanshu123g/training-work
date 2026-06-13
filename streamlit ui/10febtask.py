import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly_express as px

st.set_page_config(page_title=("Final Page"),page_icon="🧹",layout="centered")
# opt=option_menu("Menu",options=["Home","Cleaned Data","Graphs","Insights"],icons=["house", "table", "bar-chart", "lightbulb"])
with st.sidebar:
    opt=option_menu("Menu",options=["Home","Cleaned Data","Graphs","Insights"],icons=["house", "table", "bar-chart", "lightbulb"])

if opt=="Home":
    st.header("Welcome to the Home Tab.")
    st.markdown("### This is about the Project Overview.")
    st.write("This project presents an interactive data analysis dashboard built using the Wine Quality dataset. The purpose of this project is to explore, clean, analyze, and visualize wine quality data in order to understand the factors that influence wine ratings. The dataset contains various physicochemical properties of wine such as acidity, pH level, alcohol content, sulphates, density, and other chemical attributes. Each wine sample is assigned a quality score based on sensory evaluation.")
    st.success("We are able to achieve that project.")
    st.error("there were so many obstructions though")
    with st.form("REG"):
        name=st.text_input("Please Enter your name")
        email=st.text_input("Please enter your email :-")
        check=st.checkbox("Please agree to our terms and conditions.")
        submit=st.form_submit_button("Submit")
        if submit:
            if name and email and check:
                st.markdown("### Your data is safe! please dont worry.")
                st.balloons()
            else:
                st.write("please fill all the columns first.")


elif opt=="Cleaned Data":
    st.title("This is whole dataset of WINEQT")
    df=pd.read_csv("WineQT.csv")
    st.write(df)
    st.markdown("### The first five rows of the dataset are given below:- ")
    st.write(df.head(5))
    st.write("### The null values in the dataset are :-",df.isna().sum())
    df_new=df.dropna()
    st.write("#### The duplicate values here are :- ",df.duplicated().sum())
    st.write("#### The cleaned dataset preview is given below :-",df)
    st.write("#### The raw dataset having rows and columns respectively :- ",df.shape)
    st.write("#### The cleaned dataset having rows and columns respectively :- ",df_new.shape)
    st.write("#### The values of Mean, Standard Deviation, Minimum and Maximum Value are :- ",df_new.describe().loc[["mean","std","min","max"]])

elif opt=="Graphs":

    df=pd.read_csv("WineQT.csv")
    fig=px.histogram(df,x="quality",title="Wine Quality Count",color="quality")
    

    fig1=px.histogram(df,x="alcohol",nbins=30,title="Alcohol Content Distribution",color="quality")

    fig3=px.imshow(df.corr(),aspect="auto",title="Correlation between each values",text_auto=True)

    fig5=px.box(df,x="quality",y="alcohol",)

    st.header("This tab is for Representing Graphs.")
    selector=st.selectbox("Click to open the graph :",options=["Diagram 1","Diagram 2","Diagram 3","Diagram 4"])
    if selector =="Diagram 1":
        diagram_fig1=st.plotly_chart(fig)
    
    elif selector=="Diagram 2":
        diagram_fig2=st.plotly_chart(fig1)
    
    elif selector=="Diagram 3":
        diagram_fig3=st.plotly_chart(fig3)
    
    elif selector=="Diagram 4":
        diagram_fig4=st.plotly_chart(fig5)

if opt=="Insights":
    st.header("Insights from Wine Quality Analysis")
    st.markdown("### 1. Quality Score Distribution")
    st.write("The analysis of wine quality distribution reveals that the majority of wines fall within the mid-range quality scores, particularly between 5 and 6. Very few wines have extremely low or extremely high quality ratings. This indicates that the dataset is slightly concentrated around average-quality wines, suggesting a moderate overall wine standard.")
    st.markdown("### 2. Relationship Between Alcohol and Quality")
    st.write("From the histogram and boxplot analysis, a positive relationship is observed between alcohol content and wine quality. Wines with higher alcohol percentages tend to receive better quality ratings. The median alcohol level for higher-rated wines is generally greater compared to lower-rated wines.")
    st.markdown("#### This suggests that alcohol content plays a significant role in determining wine quality.")
    st.markdown("### 3. Correlation Analysis")
    st.write("The correlation heatmap indicates that alcohol shows a moderate positive correlation with quality, making it one of the more influential features in the dataset.")
    st.markdown("#### Some chemical properties exhibit weak correlations with quality, suggesting they may have limited direct impact on wine ratings. Additionally, certain features show strong correlation among themselves, which may indicate interdependency between chemical characteristics.")
    st.markdown("### 4. Feature Behavior Observations")
    st.write("Most chemical properties are distributed within a reasonable range without extreme outliers. The dataset appears well-balanced and suitable for further predictive modeling.")
    st.subheader("The variation in chemical composition contributes collectively to the final quality score rather than relying on a single dominant factor.")
    st.markdown("### 5. Final Conclusion")
    st.markdown("""
    ### Based on the exploratory data analysis:
    - Alcohol content is one of the most influential factors affecting wine quality.
    - Wine quality is moderately distributed across mid-range scores.
    - Multiple chemical attributes together influence the final rating.
    - Data visualization significantly enhances understanding of relationships between variables.""")
    st.markdown("#### This analysis provides a strong foundation for building predictive models to estimate wine quality using machine learning techniques in future work.")
