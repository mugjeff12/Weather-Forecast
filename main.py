import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next days")
place=st.text_input("Place")
#place="Dhaka"
days=st.slider("Forecast Days",min_value=1,max_value=5
               ,help="Select the number of days you want to forecast")
option = st.selectbox("Select data to view",("Temperature","Sky"))



try:
    if place:

        filtered_data = get_data(place,days)
        st.subheader(f"{option} for the next {days} days in {place}")
        if option == "Temperature":
            temperatures = [dict['main']['temp'] for dict in filtered_data]
            temperatures = [float(temp)/10 for temp in temperatures]
            dates = [dict['dt_txt'] for dict in filtered_data]
            m,n=len(temperatures),len(dates)
            figure = px.line(x=dates,y=temperatures,labels={"x":"Date","y":"Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [x['weather'][0]['main'] for x in filtered_data]
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png","Rain":"images/rain.png",
                      "Snow":"images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            date_desc = [dict['dt_txt'] for dict in filtered_data]
            for img,date in zip(image_paths,date_desc):
                st.image(img, width=115)
                st.write(date)
except (KeyError):
    st.info("Please enter a valid place.")
