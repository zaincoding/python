import streamlit as st

if not st.session_state.get("is_logged_in", False):
    st.error("Please login first.")
    st.stop()

st.title("📝 Insert Data")
st.text_input("Enter some data")
st.button("Save")
