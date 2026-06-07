import streamlit as st
import pandas as pd
from reader_config import load_config
from functions import plot_click_distribution

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Employee Performance Tracker", layout="wide")
st.title("📊 Employee Performance Dashboard")

# --- 2. LOAD CONFIGURATION & DATA ---
try:
    config = load_config('config/config.json')
except Exception as e:
    st.error(f"Configuration error: {e}")
    st.stop()


@st.cache_data
def load_data(file_path):
    """Loads dataset with caching to avoid reloading on every UI interaction."""
    return pd.read_csv(file_path, encoding='utf-8-sig')


try:
    df = load_data(config['data_path'])
except Exception as e:
    st.error(f"Failed to load data from {config['data_path']}. Error: {e}")
    st.stop()

# --- 3. SIDEBAR INTERFACE ---
st.sidebar.header("Filter Settings")

# Get unique employee names from the dataset
all_employees = df['name'].dropna().unique().tolist()

# Multiselect for employees (defaulting to those specified in config)
default_selection = [emp for emp in config['target_employees'] if emp in all_employees]
selected_employees = st.sidebar.multiselect(
    "Select Employees:",
    options=all_employees,
    default=default_selection
)

# --- 4. MAIN DASHBOARD ---
if not selected_employees:
    st.warning("Please select at least one employee from the sidebar.")
else:
    # --- Metrics Section ---
    st.subheader("Quick Insights")
    filtered_df = df[df['name'].isin(selected_employees)]
    avg_clicks = int(filtered_df['clicks'].mean())

    col1, col2, col3 = st.columns(3)
    col1.metric("Selected Employees", len(selected_employees))
    col2.metric("Average Clicks", avg_clicks, delta=avg_clicks - config['baseline_clicks'])
    col3.metric("Total Records", len(filtered_df))

    st.divider()

    # --- Plot Section ---
    st.subheader("Distribution Analysis")

    # Generate the plot using our functions.py
    fig = plot_click_distribution(
        df=df,
        selected_employees=selected_employees,
        baseline_clicks=config['baseline_clicks']
    )

    # Render the plot in Streamlit
    st.pyplot(fig)