import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Security Log Analyzer",
    layout="wide"
)

st.title("🛡️ Security Log Analyzer Dashboard")

uploaded_file = st.file_uploader(
    "Upload Log File",
    type=["txt", "log"]
)

if uploaded_file is not None:

    st.success("File uploaded successfully!")

    file_content = uploaded_file.read().decode("utf-8")

    with st.expander("📄 View Uploaded Log File"):
        st.text(file_content)

    failed = file_content.count("LOGIN_FAILED")
    success = file_content.count("LOGIN_SUCCESS")
    denied = file_content.count("ACCESS_DENIED")

    col1, col2, col3 = st.columns(3)

    col1.metric("❌ Failed Login", failed)
    col2.metric("✅ Successful Login", success)
    col3.metric("🚫 Access Denied", denied)