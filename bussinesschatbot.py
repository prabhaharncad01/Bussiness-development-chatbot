
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

/* Background */
.stApp {
    background:#F5F7FA;
}

/* Title */
.main-title {
    text-align: center;
    color: #3431E0;
    font-size: 42px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #27277D;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Banner Image */
.banner-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 15px;
    margin-bottom: 30px;
}

/* Form Card */
.form-card {
    background-color: white;
    padding: 40px;
    border-radius: 20px;
    width: 50%;
    margin: auto;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
}

/* Button */
div.stButton > button {
    background-color: #1E3A8A;
    color: white;
    font-size: 16px;
    padding: 10px 20px;
    border-radius: 10px;
    border: none;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #2563EB;
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)




# ---------------- TITLE ----------------
st.markdown("<div class='main-title'>🤖 AI SME Growth Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Generate AI-powered business growth strategies instantly</div>", unsafe_allow_html=True)

# ---------------- BANNER ----------------
st.markdown("""
<img src="https://images.pexels.com/photos/7947753/pexels-photo-7947753.jpeg"
class="banner-img">
""", unsafe_allow_html=True)

# ---------------- FORM CARD ----------------


st.markdown("### Enter Business Details")

business_name = st.text_input("Business Name")
location = st.text_input("Location")
industry = st.text_input("Industry")

generate = st.button("Generate Growth Strategy")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- AI LOGIC ----------------
if generate:

    if business_name and location and industry:

        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

        prompt = f"""
        Suggest detailed growth strategies for a {industry} business 
        named {business_name} located in {location}.
        Focus on:
        - Customer acquisition
        - Digital marketing
        - Revenue growth
        - Competitive positioning
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
        st.markdown("## 📊 Growth Strategy")
        st.write(result)

    else:
        st.warning("Please fill all fields.")
st.markdown(
    "<p style='text-align:center; font-size:14px; margin-top:200px;'>Built by Prabaharan M | AI Programming Trainee</p>",
    unsafe_allow_html=True
)




























