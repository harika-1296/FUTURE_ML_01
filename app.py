import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Sales Forecast Dashboard")

# Load data
df = pd.read_csv("superstore.csv", encoding='latin1')

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Monthly sales
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

monthly_sales['Date'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(DAY=1))

# Plot
fig, ax = plt.subplots()
ax.plot(monthly_sales['Date'], monthly_sales['Sales'])
ax.set_title("Monthly Sales Trend")

st.pyplot(fig)

st.write("### 📌 Data Preview")
st.dataframe(monthly_sales)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Sales Forecast Dashboard")

# Description
st.write("This dashboard shows historical sales trends and helps in forecasting future demand for better business decisions.")

# Load data
df = pd.read_csv("superstore.csv", encoding='latin1')

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create features
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

monthly_sales['Date'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(DAY=1))

# 🔥 KPI SECTION
total_sales = monthly_sales['Sales'].sum()
avg_sales = monthly_sales['Sales'].mean()
max_sales = monthly_sales['Sales'].max()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"{total_sales:,.0f}")
col2.metric("📊 Avg Sales", f"{avg_sales:,.0f}")
col3.metric("🚀 Max Sales", f"{max_sales:,.0f}")

# 🔥 DATE FILTER
start_date = st.date_input("Start Date", monthly_sales['Date'].min())
end_date = st.date_input("End Date", monthly_sales['Date'].max())

filtered_data = monthly_sales[
    (monthly_sales['Date'] >= pd.to_datetime(start_date)) &
    (monthly_sales['Date'] <= pd.to_datetime(end_date))
]

# 📈 Plot
fig, ax = plt.subplots()
ax.plot(filtered_data['Date'], filtered_data['Sales'])
ax.set_title("📈 Monthly Sales Trend Analysis")

st.pyplot(fig)

# 📊 Data preview
st.write("### 📌 Data Preview")
st.dataframe(filtered_data)
