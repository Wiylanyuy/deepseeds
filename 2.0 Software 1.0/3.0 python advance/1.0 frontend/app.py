import streamlit as st
# st.title("WElcom to GenAI Frontend")
# st.write('hell, world')
# st.header("Welcome Back")
# print("run")
# pressed=st.button("Click Me")
# print(pressed)

# pressed2=st.button("Click Me 2")
# print(pressed2)

# st.title("My GenAi journey")
# st.header("I specialized pre training")

# from profile import markdown_code
# st.markdown(markdown_code)


# st.image("tremimg.jpg", caption="Aspiring Ai Engineer", use_column_width=True)

# upload image and display image 
# uploaded_image = st.file_uploader("Upload your profile picture Here", type=["jpg", "jpeg", "png"])
# if uploaded_image:
#     st.image(uploaded_image, caption="Profile Picture", use_column_width=True)

# with st.form('myform'):
#    name=  st.text_input("Enter your name")
#    email= st.text_input("Enter your email")
#    phone=st.number_input("Enter your phone number")
#    description=st.text_area("Tell us more about yourself")
#    submitted = st.form_submit_button("Submit")
#    if submitted:
#        if not name:
#            st.error("Name is required.")
#        elif not email:
#            st.error("Email is required.")
#        elif not phone:
#            st.error("Phone number is required.")
#        elif not description:
#            st.error("Description is required.")
#        else:
#            st.write(f"Name: {name}")
#            st.write(f"Email: {email}")
#            st.write(f"Phone: {phone}")
#            st.write(f"Description: {description}")
#            st.success("Form submitted successfully!")
#            st.balloons()

# creating sidebar
with st.form('myform'):
   st.header("Personal Information")
   name=  st.text_input("Enter your name")
   email= st.text_input("Enter your email")
   phone=st.number_input("Enter your phone number")
   description=st.text_area("Tell us more about yourself")
   submitted = st.form_submit_button("Submit")
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
           st.write(f"Name: {name}")
           st.write(f"Email: {email}")
           st.write(f"Phone: {phone}")
           st.write(f"Description: {description}")
           st.success("Form submitted successfully!")
           st.balloons()
st.sidebar.title("* Welcome to our service, please fill out the form  to get started.")
temperature = st.sidebar.slider("Select temperature", 0.0, 1.0, 0.5)
model_choice = st.sidebar.selectbox("Choose a model", ["Gemini", "gpt-4", "claude", "llama-3", "mistral"])   
# import time
# progtress = st.progress(0)
# for percent in range(100):
#     time.sleep(0.02)  # Simulatecomputation
# #     progtress.progress(percent + 1)
# #     st.success("✅Generation completed!")

# #2 tabs(st.tabs)
# # separate sections for different content
# tab1, tab2 = st.tabs(["✍Prompt", "📋 output"])
# with tab1:
#     st.header("Prompt")
#     prompt = st.text_area("Enter your prompt here")
      
# with tab2:
#     st.header("Output")
#     st.write("Generated output  results will appear here.")
# #3 Columns(st.columns)
# # Places elements side by side (e.g input on left output on right)
# col1, col2=st.columns(2)
# with col1:
#     st.text_input("Enter Prompt")
# with col2:
#     st.write("Ai result goes here")
    
# #4 containers(st.container)
# # group relted elements and allow for dynamic update inside the group
# container=st.container() 
# container.write("Generate text area")
# btn=container.button("Generate text area")
# # --------------------------------------------------------

# #5 Expander(st.expander)
# #Hide/show details on demnd -useful for advance setting or explanation
# with st.expander("Advance options"):
#     st.slider("max Token", 100, 1000)
#     st.checkbox("stream output")


# #6 Empty(st.empty)
# #reserve a space for contain that updates later(eg. dynamic results areas)
# placeholder=st.empty
# if st.button("Generate"):
#     placeholder.write("Generating...")
#     # simulate geration
#     placeholder.write("✅done here is the results")

#---------------------------------------------------------
# combined Layout for GenAi app

st.title("GenAi Prompt Generator")
# sidbebar setting
st.sidebar.title("Setting")
temp=st.sidebar.slider("Creativity(temperature)", 0.0, 1.0, 0.7)
# tabs 
tab1, tab2=st.tabs(["Prompt", "Output"])
with tab1:
    prompt=st.text_area("Enter your prompt")

with tab2:
    st.write("**AI OUTPUT**")
    if st.button("Generate"):
        st.success(f"Response from model(temp={temp}) for: {prompt}")