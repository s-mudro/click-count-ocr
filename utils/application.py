import streamlit as st
import pandas as pd
import os
import sys
from reader_config import load_config
from functions import plot_rolling_average

# Setup page configuration
st.set_page_config(page_title="Employee Performance Dashboard", layout="wide")
st.title("📊 Employee Performance Dashboard")

# --- 1. DATA LOADING ---
config = load_config()

# Build absolute path to avoid Errno 2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
full_data_path = os.path.join(BASE_DIR, config['data_path'])

try:
    df = pd.read_csv(full_data_path, encoding='utf-16')
    df['date'] = pd.to_datetime(df['date'])
except Exception as e:
    st.error(f"Failed to load data from {config['data_path']}. Error: {e}")
    st.stop()

# --- 2. SIDEBAR & FILTERS ---
st.sidebar.header("Filter Settings")

# Single employee selection for the line chart
all_employees = sorted(df['name'].dropna().unique().tolist())
default_emp = "Roman3" if "Roman3" in all_employees else all_employees[0]
selected_employee = st.sidebar.selectbox("Select Employee:", options=all_employees, index=all_employees.index(default_emp))

# Date range slider
min_date = df['date'].min().to_pydatetime()
max_date = df['date'].max().to_pydatetime()

selected_dates = st.sidebar.slider(
    "Select Date Range:",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="YYYY-MM-DD"
)

start_date, end_date = selected_dates

# --- 3. MAIN DASHBOARD ---
st.subheader("Performance Trend Analysis")

# Generate and display the plot
fig = plot_rolling_average(
    df=df,
    selected_employee=selected_employee,
    start_date=start_date,
    end_date=end_date,
    baseline=config['baseline_clicks']
)

st.pyplot(fig)

st.divider()

# --- 4. EXPORT / SAVE PLOT INTERFACE ---
# Handle local file export to existing 'fig' directory when button is triggered
if st.button("Save Plot"):
    # Format dates into YYYYMMDD string strings
    str_start = start_date.strftime('%Y%m%d')
    str_end = end_date.strftime('%Y%m%d')

    # Construct filename and full export path based on global root directory
    filename = f"{selected_employee}_{str_start}_{str_end}.png"
    fig_dir = os.path.join(BASE_DIR, 'fig')
    full_save_path = os.path.join(fig_dir, filename)

    # Regenerate plot and save it to the specified directory path
    plot_rolling_average(df, selected_employee, start_date, end_date, config['baseline_clicks'],
                         save_path=full_save_path)

    # Display success state indicator in UI
    st.success(f"✓ Plot successfully saved to: `fig/{filename}`")