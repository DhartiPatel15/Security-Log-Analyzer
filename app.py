import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title="Security Log Analyzer", layout="wide")

uploaded_file = st.file_uploader("Upload Log File", type=["txt", "log"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write(uploaded_file.name)
    file_content = uploaded_file.read().decode("utf-8")
    with st.expander("📄 View Uploaded Log File"):
      st.text(file_content)
    failed = file_content.count("LOGIN_FAILED")
    success = file_content.count("LOGIN_SUCCESS")
    denied = file_content.count("ACCESS_DENIED")
    total_login = failed + success

    success_percentage = (success / total_login) * 100
    failed_percentage = (failed / total_login) * 100

    st.write(f"Login Success Percentage: {success_percentage:.1f}%")
    st.write(f"Login Failed Percentage: {failed_percentage:.1f}%")
    if "10.0.0.5" in file_content:
      st.error("⚠️ Suspicious IP Found: 10.0.0.5")
    else:
      st.success("No Suspicious IP Found")
    st.write("Failed Login:", failed)
    st.write("Successful Login:", success)
    st.write("Access Denied:", denied)

st.title("🛡️ Security Log Analyzer Dashboard")
col1, col2, col3 = st.columns(3)

col1.metric("Failed Login", failed)
col2.metric("Successful Login", success)
col3.metric("Access Denied", denied)
col1, col2, col3 = st.columns(3)

col1.metric("Failed Login", failed)
col2.metric("Successful Login", success)
col3.metric("Access Denied", denied)
st.write("Welcome to the Security Log Analyzer Project")

st.header("Security Report")

report = """
Failed Login Attempts : 8
Successful Logins : 4
Access Denied Events : 2
Suspicious IP : 10.0.0.5
"""
report_text = f"""
Security Log Analyzer Report

Failed Login: {failed}
Successful Login: {success}
Access Denied: {denied}

Login Success Percentage: {success_percentage:.1f}%
Login Failed Percentage: {failed_percentage:.1f}%

Suspicious IP: 10.0.0.5
"""

st.download_button(
    label="📥 Download Security Report",
    data=report_text,
    file_name="security_report.txt",
    mime="text/plain"
)

st.text(report)
labels = ["Failed Login", "Successful Login", "Access Denied"]
values = [failed, success, denied]
sizes = [8, 4, 2]

st.subheader("Bar Chart")

fig, ax = plt.subplots()
ax.bar(labels, values, color=["red", "green", "orange"])
ax.set_ylabel("Count")
st.pyplot(fig)
st.subheader("Pie Chart")

fig2, ax2 = plt.subplots()
ax2.pie(sizes, labels=labels, autopct="%1.1f%%")
ax2.axis("equal")
st.pyplot(fig2)
