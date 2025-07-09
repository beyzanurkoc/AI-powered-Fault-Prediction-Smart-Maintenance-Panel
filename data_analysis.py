import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Analysis Panel")

df = pd.read_csv("sample_data.csv")

st.subheader("All Rows")
st.dataframe(df)

st.write(f"Shape: {df.shape}")

st.subheader("Missing Values")
st.write(df.isnull().sum())

st.subheader("Fault Code Distribution")
st.bar_chart(df["code"].value_counts())
st.dataframe(df["code"].value_counts())

st.subheader("Descriptive Statistics")
st.dataframe(df[["temperature", "pressure", "engine_rpm"]].describe())

tab1, tab2, tab3 = st.tabs(["Temperature", "Pressure", "Engine RPM"])

with tab1:
    fig, ax = plt.subplots()
    df["temperature"].hist(bins=20, ax=ax)
    ax.set_title("Temperature Distribution")
    ax.set_xlabel("Temperature (°C)")
    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots()
    df["pressure"].hist(bins=20, ax=ax)
    ax.set_title("Pressure Distribution")
    ax.set_xlabel("Pressure (bar)")
    st.pyplot(fig)

with tab3:
    fig, ax = plt.subplots()
    df["engine_rpm"].hist(bins=20, ax=ax)
    ax.set_title("Engine RPM Distribution")
    ax.set_xlabel("Engine RPM")
    st.pyplot(fig)

st.subheader("Average Sensor Values per Fault Code")
fig, ax = plt.subplots(figsize=(12,6))
df.groupby("code")[["temperature", "pressure", "engine_rpm"]].mean().plot(kind="bar", ax=ax)
plt.title("Average Sensor Values per Fault Code")
plt.ylabel("Average Value")
plt.xticks(rotation=45)
st.pyplot(fig)
