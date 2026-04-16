import streamlit as st
import sqlite3

# ---------------------------
# Database Setup
# ---------------------------
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")
conn.commit()


# ---------------------------
# Functions
# ---------------------------
def register_user(username, password):
    cursor.execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, password))
    conn.commit()


def login_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cursor.fetchone()


def change_password(username, old_pass, new_pass):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, old_pass))
    if cursor.fetchone():
        cursor.execute("UPDATE users SET password=? WHERE username=?", (new_pass, username))
        conn.commit()
        return True
    return False


# ---------------------------
# UI
# ---------------------------
st.set_page_config(page_title="User System", layout="centered")

st.title("👨‍💻 Streamlit User System (Servlet Replacement)")

menu = ["Hello World", "Register", "Login", "Change Password"]
choice = st.sidebar.selectbox("Menu", menu)


# ---------------------------
# 1. Hello World
# ---------------------------
if choice == "Hello World":
    st.header("Hello World")
    st.success("Hello World from Streamlit! 🎉")


# ---------------------------
# 2. Registration
# ---------------------------
elif choice == "Register":
    st.header("User Registration")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if username and password:
            register_user(username, password)
            st.success("Registration Successful!")
        else:
            st.error("Please fill all fields")


# ---------------------------
# 3. Login
# ---------------------------
elif choice == "Login":
    st.header("User Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.success(f"Welcome {username} ✅")
        else:
            st.error("Invalid Credentials ❌")


# ---------------------------
# 4. Change Password
# ---------------------------
elif choice == "Change Password":
    st.header("Change Password")

    username = st.text_input("Username")
    old_pass = st.text_input("Old Password", type="password")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Change Password"):
        if change_password(username, old_pass, new_pass):
            st.success("Password Changed Successfully!")
        else:
            st.error("Invalid Username or Old Password")
