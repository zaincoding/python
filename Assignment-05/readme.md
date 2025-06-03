# 🔐 Streamlit Secure Login App

This is a secure login-based Streamlit application that uses **Fernet encryption** to validate user credentials and restrict access to private pages.

### 🔗 Live App  
Access here: [Login Page](https://assignment7-qbwbqdvfhihucnmgrgyxpc.streamlit.app/Login)

---

## 🧠 How It Works

- **Encrypted Login:** The valid username is encrypted using a password. Login works only if the password correctly decrypts the username.
- **Access Control:** Users get 3 attempts to log in. After that, access is blocked.
- **Session Handling:** `session_state` manages login status and attempts.
- **Protected Pages:** `Insert_Data.py` and `Retrieve_Data.py` are only accessible after login.

---

## 📄 Pages

- `/Login`: Login form with encryption logic.
- `/Insert_Data`: Input form (protected).
- `/Retrieve_Data`: Displays stored data (protected).

---

## 🧪 Default Credentials

- **Username:** `zain`
- **Password:** `password`

