import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Smart Traffic Optimization", layout="wide")

st.title("🚦 AI Powered Smart Traffic Optimization System")

model = joblib.load("traffic_model.pkl")

st.sidebar.header("Traffic Input")

vehicles = st.sidebar.slider("Vehicle Count",0,100,35)
junction = st.sidebar.selectbox("Junction",[1,2,3,4])
year = st.sidebar.number_input("Year",2015,2030,2017)
month = st.sidebar.slider("Month",1,12,8)
day = st.sidebar.slider("Day",1,31,15)
hour = st.sidebar.slider("Hour",0,23,18)
dow = st.sidebar.slider("Day Of Week",0,6,2)

sample = pd.DataFrame({
    "Vehicles":[vehicles],
    "Junction":[junction],
    "Year":[year],
    "Month":[month],
    "Day":[day],
    "Hour":[hour],
    "DayOfWeek":[dow]
})

prediction = model.predict(sample)

levels = {
    0:"Free Flow",
    1:"Moderate",
    2:"Heavy",
    3:"Severe"
}

st.subheader("Predicted Traffic")

st.success(levels[int(prediction[0])])
