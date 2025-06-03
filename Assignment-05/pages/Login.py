import streamlit as st
from utils.security import encrypt_message, decrypt_message, MAX_ATTEMPTS

# 🔐 Valid credentials
VALID_USERNAME = "zain"
VALID_PASSWORD = "password"

# 🔐 Encrypt the valid username using the password
ENCRYPTED_USERNAME = encrypt_message(VALID_USERNAME, VALID_PASSWORD)

# 🔄 Initialize session state
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'is_logged_in' not in st.session_state:
    st.session_state.is_logged_in = False

# 🧾 UI
st.set_page_config(page_title="Login", page_icon="🔐")
st.title("🔐 Secure Login")

username_input = st.text_input("Username")
password_input = st.text_input("Password", type="password")

# 🔘 Login Button Logic
if st.button("Login"):
    if st.session_state.attempts >= MAX_ATTEMPTS:
        st.error("🚫 Access blocked. Please restart the app.")
    else:
        decrypted = decrypt_message(ENCRYPTED_USERNAME, password_input)
        if decrypted == VALID_USERNAME:
            st.session_state.is_logged_in = True
            st.session_state.attempts = 0
            st.success("✅ Logged in successfully!")
        else:
            st.session_state.attempts += 1
            remaining = MAX_ATTEMPTS - st.session_state.attempts
            st.warning(f"❌ Invalid login. {remaining} attempts left.")
