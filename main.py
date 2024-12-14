import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next days")
place=st.text_input("Place")
days=st.slider("Forecast Days",min_value=1,max_value=5
               ,help="Select the number of days you want to forecast")
option = st.selectbox("Select data to view",("Temperature","Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

#dates=["2022-09-09","2022-09-10","2022-09-11"]
#temperatures =[9,10,11]

filtered_data = get_data(place,days,option)

if option == "Temperature":
    filtered_data = [x['main']['temp'] for x in filtered_data]
    figure = px.line(x=[i for i in range(days)],y=filtered_data,labels={"x":"Date","y":"Temperature"})
    st.plotly_chart(figure)

if option == "Sky":
    filtered_data = [x['weather'][0]['main'] for x in filtered_data]