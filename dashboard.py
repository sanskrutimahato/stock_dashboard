import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("clean_stock_data.csv")
    df["Date_"] = pd.to_datetime(df["Date_"])
    return df

df = load_data()

# Page title
st.set_page_config(page_title="Stock Dashboard", page_icon="📊", layout="wide")
st.title("📊 Stock Market Dashboard")
st.markdown("### A clean & interactive dashboard to analyze stock trends")

# Company selection
companies = ["INFY.NS", "TCS.NS"]
selected_company = st.selectbox("Choose a company:", companies)

# Map company to column names
col_map = {
    "INFY.NS": {
        "Close": "Close_INFY.NS",
        "Open": "Open_INFY.NS",
        "High": "High_INFY.NS",
        "Low": "Low_INFY.NS",
        "Volume": "Volume_INFY.NS",
    },
    "TCS.NS": {
        "Close": "Close_TCS.NS",
        "Open": "Open_TCS.NS",
        "High": "High_TCS.NS",
        "Low": "Low_TCS.NS",
        "Volume": "Volume_TCS.NS",
    }
}

# Latest values
latest_row = df.iloc[-1]
col1, col2, col3 = st.columns(3)
col1.metric("📈 Closing Price", f"{latest_row[col_map[selected_company]['Close']]:,.2f}")
col2.metric("📊 Opening Price", f"{latest_row[col_map[selected_company]['Open']]:,.2f}")
col3.metric("📦 Volume", f"{latest_row[col_map[selected_company]['Volume']]:,}")

# Tabs for visualization
tab1, tab2 = st.tabs(["📉 Price Trend", "📊 Volume Trend"])

with tab1:
    st.subheader(f"Closing Price of {selected_company}")
    fig_price = px.line(
        df, 
        x="Date_", 
        y=col_map[selected_company]["Close"], 
        title=f"{selected_company} Closing Price Over Time",
        labels={"Date_": "Date", col_map[selected_company]["Close"]: "Price"},
        template="plotly_white"
    )
    st.plotly_chart(fig_price, use_container_width=True)

with tab2:
    st.subheader(f"Trading Volume of {selected_company}")
    fig_volume = px.bar(
        df,
        x="Date_",
        y=col_map[selected_company]["Volume"],
        title=f"{selected_company} Trading Volume Over Time",
        labels={"Date_": "Date", col_map[selected_company]["Volume"]: "Volume"},
        template="plotly_white"
    )
    st.plotly_chart(fig_volume, use_container_width=True)

# Show raw data option
with st.expander("📂 Show Raw Data"):
    st.dataframe(df[["Date_"] + list(col_map[selected_company].values())], use_container_width=True)
