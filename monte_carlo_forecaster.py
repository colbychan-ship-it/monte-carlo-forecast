import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Monte Carlo Delivery Time Forecast")

uploaded_file = st.file_uploader("Upload your delivery data CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded data:")
    st.write(df.head())

    # Assume df has a column 'delivery_time' in days
    if "delivery_time" in df.columns:
        delivery_times = df["delivery_time"]

        simulations = st.slider("Number of simulations", 100, 10000, 1000)
        simulated_results = np.random.choice(delivery_times, size=simulations, replace=True)

        st.write("Simulation results summary:")
        st.write(pd.Series(simulated_results).describe())

        fig, ax = plt.subplots()
        ax.hist(simulated_results, bins=30, color="skyblue", edgecolor="black")
        ax.set_title("Monte Carlo Simulation of Delivery Times")
        ax.set_xlabel("Delivery Time (days)")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
    else:
        st.error("CSV must contain a 'delivery_time' column.")
else:
    st.info("Please upload a CSV file to get started.")
