
import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq



# Page config
st.set_page_config(page_title="AI SME Growth Assistant", page_icon="🚀")

st.title("🚀 AI SME Growth Assistant")
st.write("Get AI-powered business growth strategies instantly.")

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
        st.write(result)

    else:
        st.warning("Please fill all fields.")

