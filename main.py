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
total_login = failed + success

threat_score = failed * 20 + denied * 20

if threat_score > 100:
    threat_score = 100

if threat_score >= 80:
    risk = "🔴 HIGH"
elif threat_score >= 50:
    risk = "🟡 MEDIUM"
else:
    risk = "🟢 LOW"

st.subheader("🛡️ AI Threat Analysis")
st.metric("Threat Score", f"{threat_score}/100")
st.error(f"Risk Level: {risk}")
# Suspicious IP Detection

suspicious_ip = "Not Found"

for line in file_content.splitlines():
    if "10.0.0.5" in line:
        suspicious_ip = "10.0.0.5"
        break

st.warning(f"⚠️ Suspicious IP Found: {suspicious_ip}")

# Login Percentage
success_percentage = (success / total_login) * 100
failed_percentage = (failed / total_login) * 100

st.info(f"✅ Login Success: {success_percentage:.1f}%")
st.info(f"❌ Login Failed: {failed_percentage:.1f}%")