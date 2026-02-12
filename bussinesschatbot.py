
import os

import streamlit as st
from groq import Groq


#page config
st.set_page_config(
    page_title="AI SME Business Growth Assistant",
    page_icon="🤖",
    layout="centered"
)
# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1E3A8A, #3B82F6);
    }

    .main-card {
        background-color: #FFFFFF;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
    }

    h1 {
        color: #FFFFFF;
        text-align: center;
    }

    .subtext {
        color: #E0E7FF;
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    div.stButton > button {
        background-color: #FFFFFF;
        color: #1E3A8A;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #E0E7FF;
        color: #1E3A8A;
    }
    </style>
""", unsafe_allow_html=True)



# ---------------- HEADER ----------------
st.markdown("<h1>🚀 AI SME Growth Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Generate AI-powered business growth strategies instantly</p>", unsafe_allow_html=True)




# ---------------- CARD START ----------------
st.markdown("<div class='main-card'>", unsafe_allow_html=True)

business_name = st.text_input("🏢 Enter Business Name")
location = st.text_input("📍 Enter Location")
industry = st.text_input("🏷️ Enter Industry")

if st.button("Generate Growth Strategy"):

    if business_name and location and industry:

        client = Groq(api_key=os.environ["GROQ_API_KEY"])

        prompt = f"""
        Suggest detailed growth strategies for a {industry} business 
        named {business_name} located in {location}.
        Focus on customer acquisition, digital marketing, and revenue growth.
        """

        with st.spinner("🤖 Generating strategy..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are an AI business growth expert."},
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content

        st.success("✅ Strategy Generated Successfully!")
        st.balloons()
        st.write(result)

    else:
        st.warning("⚠ Please fill all fields.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; font-size:14px;'>Built by Prabaharan M | AI Programming Trainee</p>",
    unsafe_allow_html=True
)











