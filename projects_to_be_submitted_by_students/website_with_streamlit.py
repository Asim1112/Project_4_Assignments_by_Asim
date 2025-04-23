import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="📊 Data Dashboard", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .css-1aumxhk {
        padding: 2rem;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>📈 Interactive Data Dashboard</h1>", unsafe_allow_html=True)

# File uploader section
st.markdown("### 📂 Upload Your CSV File Below")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    # Data preview
    st.markdown("### 👀 Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    # Data summary
    st.markdown("### 📊 Data Summary")
    st.dataframe(df.describe(), use_container_width=True)

    # Filter Section
    st.markdown("### 🔎 Filter Your Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.markdown("✅ **Filtered Data:**")
    st.dataframe(filtered_df, use_container_width=True)

    # Plot section
    st.markdown("### 📉 Plot Your Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    if st.button("🚀 Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
        st.success("✅ Plot generated successfully!")

else:
    st.warning("📭 Waiting for file upload...")
