import streamlit as st

if not st.session_state.get("is_logged_in", False):
    st.error("Please login first.")
    st.stop()

st.title("🔎 Retrieve Data")
st.write("Here is your stored data.")
