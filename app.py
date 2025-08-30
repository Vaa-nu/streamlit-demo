import streamlit as st
st.title("Hello Streamlit ")
st.write("This is a simple app deployed on **Streamlit Community cloud.")
name = st.text_input("Enter your name:")
if st.button("Say Hello"):
     st.success(f"Hello {name}, welcome to Streamlit!")
