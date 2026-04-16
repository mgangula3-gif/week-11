import streamlit as st

st.set_page_config(page_title="Employee Form", layout="centered")

st.title("👨‍💼 Employee Details Form")

# ---------------------------
# Form (like HTML POST form)
# ---------------------------
with st.form("employee_form"):
    name = st.text_input("Employee Name")
    phone = st.text_input("Phone Number")

    submit = st.form_submit_button("Submit")

# ---------------------------
# Display Data (like Servlet)
# ---------------------------
if submit:
    if name and phone:
        st.success("Employee Details Submitted Successfully ✅")

        st.subheader("📋 Employee Information")
        st.write(f"**Name:** {name}")
        st.write(f"**Phone:** {phone}")
    else:
        st.error("Please fill all fields ❌")
