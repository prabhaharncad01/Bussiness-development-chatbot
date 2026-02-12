
import os

import streamlit as st
from groq import Groq


#page config
st.set_page_config(
    page_title="AI SME Growth Assistant",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
    <h1 style='text-align: center; color: #274DF5;'>
        🤖 AI SME Growth Assistant
    </h1>
    <p style='text-align: center; font-size:18px; color: #79E031'>
        Generate AI-powered business growth strategies in seconds
     
    </p>
    <p style='text-align: center; font-size:18px;color: #79E031'>
        This App is developed by M.prabhaharn😎

    </p>
    
""", unsafe_allow_html=True)

st.divider()


# User input
business_name = st.text_input("Enter Business Name")
location = st.text_input("Enter Location")
industry = st.text_input("Enter Industry")

if st.button("Generate Growth Strategy"):

    if business_name and location and industry:

        client = Groq(api_key=os.environ["GROQ_API_KEY"])

        prompt = f"""
        Suggest detailed growth strategies for a {industry} business 
        named {business_name} located in {location}.
        Focus on customer acquisition, digital marketing, and revenue growth.
        """

        with st.spinner("Generating strategy..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are an AI business growth expert."},
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content

        st.success("Strategy Generated Successfully!")
        st.balloons()
        st.write(result)

    else:
        st.warning("Please fill all fields.")



st.markdown("""
    <style>
    .stApp {
        background-color: #f5f7fa;
    }
    </style>
""", unsafe_allow_html=True)



st.divider()
st.markdown(
    "<p style='text-align:center; font-size:14px;'>Built by Prabaharan M | AI Programming Trainee</p>",
    unsafe_allow_html=True
)






