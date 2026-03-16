import streamlit as st
from google import genai
from google.genai import types

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("👨‍💻 Afshan's Tech Journey")
st.write("Welcome to my first step into the tech industry!")

st.header("About Me")
st.write("""
I am a B.Tech engineering student exploring the world of technology.
Currently learning programming and building small AI projects using Python and Streamlit.
""")

question = st.text_input("Ask something about my tech journey")

if st.button("Ask"):
    if question:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction="""
You are an AI assistant representing Afshan, a beginner engineering student starting a journey in the tech industry.
Keep answers simple and professional.
"""
            )
        )

        st.subheader("AI Response")
        st.write(response.text)