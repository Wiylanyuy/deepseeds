import streamlit as st

# Set up the sidebar form
with st.sidebar.form('myform'):
    st.header("Contact Information")
    
    name = st.text_input("Enter your name*")
    email = st.text_input("Enter your email*")
    phone = st.number_input("Enter your phone number*", 
                          min_value=1000000000, 
                          max_value=9999999999,
                          step=1,
                          format="%d")
    description = st.text_area("Tell us more about yourself*")
    
    submitted = st.form_submit_button("Submit")
    
    # Small hint about required fields
    st.caption("* indicates required field")

# Main content area
st.title("Welcome to Our Service")
st.write("Please fill out the form in the sidebar to get started.")

if submitted:
    if not name:
        st.error("Name is required.")
    elif not email:
        st.error("Email is required.")
    elif not phone:
        st.error("Phone number is required.")
    elif not description:
        st.error("Description is required.")
    else:
        # Clear the sidebar inputs on successful submission
        st.sidebar.empty()
        
        # Display results in main area
        st.success("Form submitted successfully!")
        st.balloons()
        
        st.subheader("Submitted Information:")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Name:**", name)
            st.write("**Email:**", email)
        
        with col2:
            st.write("**Phone:**", phone)
        
        st.write("**Description:**")
        st.info(description)
        
        # Optional: Add a button to show the form again
        if st.button("Submit another response"):
            st.rerun()