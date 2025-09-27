import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(

  page_title="My streamlit App",
  page_icon="🌻",
  layout="wide",
)
#st.image("image.jpeg", use_container_width=True)
st.title("My Dashboard")
st.write("Hello! This is my first streamlit app.")



Car_Data = pd.read_csv("Car Sales.xlsx - car_data.csv")


#side bar   
st.sidebar.image("CarPic.jpg")
st.sidebar.title("Car Sales Data Analysis")
st.sidebar.header("Filter Here:")

Gender = st.sidebar.multiselect(
   "Select Gender:",
   options= Car_Data["Gender"].unique(),
   default= Car_Data["Gender"].unique()

)

Company = st.sidebar.multiselect(
   "Select Company:",
   options= Car_Data["Company"].unique(),
   default= Car_Data["Company"].unique()

)

Engine = st.sidebar.multiselect(
   "Select Engine Type:",
   options= Car_Data["Engine"].unique(),
   default= Car_Data["Engine"].unique()

)

Color = st.sidebar.multiselect(
   "Select Color:",
   options= Car_Data["Color"].unique(),
   default= Car_Data["Color"].unique()

)

Car_Data_selection = Car_Data.query(
    "Gender == @Gender & Company == @Company & Engine == @Engine & Color ==  @Color"

)



Gender_div = Car_Data_selection.groupby(['Gender']).size().reset_index(name='count')
fig_Gender = px.bar(Gender_div, 
             x='Gender', 
             y='count', 
             color='Gender', 
             hover_data=['count', 'Gender'], 
             title='Customer Count by Gender')
st.plotly_chart(fig_Gender)


Color_div = Car_Data_selection.groupby(['Gender', 'Color']).size().reset_index(name='count')
Color_div['Gender_Color'] = Color_div['Gender'] + " | " + Color_div['Color']
fig_Color = px.bar(Color_div, 
                   x='Color', 
                   y='count', 
                   color='Gender_Color', 
                   hover_data=['count', 'Gender'], 
                   title='Customer Count by Gender')

st.plotly_chart(fig_Color, key="color_chart")








Company_div = Car_Data_selection.groupby(['Gender', 'Company']).size().reset_index(name='count')
Company_div['Gender_Company'] = Company_div['Gender'] + " | " + Company_div['Company']
fig_Company = px.bar(Company_div, 
                   x='Company', 
                   y='count', 
                   color='Gender', 
                   hover_data=['count', 'Gender'], 
                   title='Customer Count by company')
fig_Company.update_layout(barmode='group')

st.plotly_chart(fig_Company , key="company_chart")



