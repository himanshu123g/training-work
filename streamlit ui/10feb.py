import plotly_express as px
import pandas as pd
import streamlit as st

df=pd.read_csv("covid.csv")
st.set_page_config(page_title="Graph Title",page_icon="🚨",layout="centered")
df.drop(columns=["NewCases","NewDeaths","NewRecovered"],inplace=True)
df.dropna(inplace=True)
st.write(df)

fig=px.scatter(df,x="Population",y="TotalCases",color="Continent",hover_name="Country/Region",log_x=True,log_y=True,size="TotalDeaths")
st.write(fig)

fig1=px.line(df,y="TotalDeaths",x="TotalCases",color="Continent",hover_name="Country/Region")
st.write(fig1)

fig2=px.bar(df,x="Continent",y="TotalCases",hover_name="Country/Region")
st.write(fig2)

fig3=px.pie(df,names="Continent",values="TotalCases",hole=0.3)
st.write(fig3)

fig4=px.sunburst(df,path=["Continent","Country/Region"],values="TotalCases",color="TotalDeaths",height=800)
st.write(fig4)

fig6=px.scatter_3d(df,x="Population",y="TotalCases",z="TotalDeaths",color="Continent",hover_name="Country/Region")
st.write(fig6)

fig7=px.scatter_3d(df,x="Population",y="TotalCases",z="TotalDeaths",color="Continent",hover_name="Country/Region",log_x=True,log_y=True,size="TotalDeaths")
st.write(fig7)

fig8=px.line_3d(df,x="Population",y="TotalCases",z="TotalDeaths",color="Continent",hover_name="Country/Region")
st.write(fig8)