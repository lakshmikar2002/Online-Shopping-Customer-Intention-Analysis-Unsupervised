import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("best_model.pkl")

st.title("Customer Segmentation App")

# 🔹 Input fields (keep minimum required)
Administrative_Duration = st.number_input("Administrative Duration", min_value=0.0)
Informational_Duration = st.number_input("Informational Duration", min_value=0.0)
ProductRelated = st.number_input("Product Related", min_value=0, value=30)
ProductRelated_Duration = st.number_input("Product Related Duration", min_value=0.0)
BounceRates = st.slider("Bounce Rates", 0.0, 1.0, 0.02)
ExitRates = st.slider("Exit Rates", 0.0, 1.0, 0.04)
PageValues = st.number_input("Page Values", min_value=0.0)
SpecialDay = st.slider("Special Day", 0.0, 1.0, 0.0)

Month = st.selectbox("Month", 
    ['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sep','Oct','Nov','Dec'])

OperatingSystems = st.selectbox("Operating System", [1,2,3,4,5,6,7,8])
Browser = st.selectbox("Browser", [1,2,3,4,5,6,7,8,9,10])
Region = st.selectbox("Region", [1,2,3,4,5,6,7,8,9])
TrafficType = st.selectbox("Traffic Type", list(range(1,21)))

VisitorType = st.selectbox("Visitor Type", 
    ['Returning_Visitor','New_Visitor','Other'])

Weekend = st.selectbox("Weekend", [0,1])

# 🔮 Prediction
if st.button("Predict Cluster"):

    data = pd.DataFrame([{
        'Administrative_Duration': Administrative_Duration,
        'Informational_Duration': Informational_Duration,
        'ProductRelated': ProductRelated,
        'ProductRelated_Duration': ProductRelated_Duration,
        'BounceRates': BounceRates,
        'ExitRates': ExitRates,
        'PageValues': PageValues,
        'SpecialDay': SpecialDay,
        'Month': Month,
        'OperatingSystems': OperatingSystems,
        'Browser': Browser,
        'Region': Region,
        'TrafficType': TrafficType,
        'VisitorType': VisitorType,
        'Weekend': Weekend
    }])

    cluster = model.predict(data)[0]

    # Optional meaning
    cluster_map = {
        0: "Browsers (Low Engagement)",
        1: "High Value Customers 💰",
        2: "Potential Buyers"
    }

    st.success(f"Cluster: {cluster}")
    st.info(cluster_map.get(cluster, "Unknown"))