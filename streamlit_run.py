import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="US Airbnb Dashboard",
    layout="wide"
)

# -----------------------
# Header image
# -----------------------
st.image("airbnb.png", width=150)
st.title("U.S. Airbnb Analysis Dashboard (2020 vs 2023)")
st.caption("Exploratory analysis of Airbnb listings across U.S. cities")

# -----------------------
# Load data
# -----------------------
@st.cache_data
def load_data():
    air2020 = pd.read_csv("AB_US_2020.csv")
    air2023 = pd.read_csv("AB_US_2023.csv")
    air2020["year"] = "2020"
    air2023["year"] = "2023"
    return air2020, air2023

air2020, air2023 = load_data()
data = pd.concat([air2020, air2023], ignore_index=True)

# -----------------------
# Sidebar filters
# -----------------------
st.sidebar.header("Filters")

year = st.sidebar.selectbox("Select Year", ["2020", "2023"])

city_options = sorted(data["city"].dropna().unique())
city = st.sidebar.selectbox("Select City", ["All"] + city_options)

room_type_options = sorted(data["room_type"].dropna().unique())
room_type = st.sidebar.multiselect(
    "Room Type",
    room_type_options,
    default=room_type_options
)

price_range = st.sidebar.slider(
    "Price Range",
    int(data["price"].min()),
    int(data["price"].quantile(0.95)),
    (
        int(data["price"].min()),
        int(data["price"].quantile(0.95))
    )
)

# -----------------------
# Apply filters
# -----------------------
filtered = data[data["year"] == year]
filtered = filtered[filtered["room_type"].isin(room_type)]
filtered = filtered[
    (filtered["price"] >= price_range[0]) &
    (filtered["price"] <= price_range[1])
]

if city != "All":
    filtered = filtered[filtered["city"] == city]

# -----------------------
# KPI metrics
# -----------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Listings", len(filtered))
col2.metric("Average Price ($)", round(filtered["price"].mean(), 2))
col3.metric("Median Price ($)", round(filtered["price"].median(), 2))
col4.metric("Avg Reviews / Month", round(filtered["reviews_per_month"].mean(), 2))

# -----------------------
# Price distribution
# -----------------------
st.subheader("Price Distribution")

fig_price = px.histogram(
    filtered,
    x="price",
    nbins=50,
    color="room_type",
    labels={"price": "Price ($)"}
)

st.plotly_chart(fig_price, use_container_width=True)

# -----------------------
# Room type breakdown
# -----------------------
st.subheader("Room Type Breakdown")

room_counts = filtered["room_type"].value_counts().reset_index()
room_counts.columns = ["room_type", "count"]

fig_room = px.bar(
    room_counts,
    x="room_type",
    y="count",
    labels={"count": "Number of Listings"}
)

st.plotly_chart(fig_room, use_container_width=True)

# -----------------------
# City price comparison
# -----------------------
st.subheader("Average Price by City")

city_prices = (
    filtered.groupby("city")["price"]
    .mean()
    .sort_values(ascending=False)
    .head(15)
    .reset_index()
)

fig_city = px.bar(
    city_prices,
    x="city",
    y="price",
    labels={"price": "Average Price ($)"}
)

st.plotly_chart(fig_city, use_container_width=True)

# -----------------------
# Map visualization
# -----------------------
st.subheader("Geographic Distribution")

fig_map = px.scatter_mapbox(
    filtered,
    lat="latitude",
    lon="longitude",
    color="room_type",
    size="price",
    hover_name="name",
    hover_data=["city", "price", "room_type"],
    zoom=3,
    height=600
)

fig_map.update_layout(
    mapbox_style="carto-positron",
    margin={"r": 0, "t": 0, "l": 0, "b": 0}
)

st.plotly_chart(fig_map, use_container_width=True)

# -----------------------
# Raw data
# -----------------------
with st.expander("View Raw Data"):
    st.dataframe(filtered)
