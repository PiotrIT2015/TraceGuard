import streamlit as st
import json
import pandas as pd

st.title("🛡 TraceGuard")

def load_data():
    try:
        with open("data/events.json") as f:
            return json.load(f)
    except:
        return []

data = load_data()

df = pd.DataFrame(data)

st.subheader("📡 Events")

if df.empty:
    st.warning("No events yet (pipeline is safe even if empty)")
    st.stop()

st.dataframe(df)

st.subheader("📊 Top paths")

if "path" in df.columns:
    st.bar_chart(df["path"].value_counts())
else:
    st.info("No path data available")