import os
import streamlit as st
from dotenv import load_dotenv
from litellm import completion

# Load environment variables
load_dotenv()

# Set Streamlit page title
st.set_page_config(page_title="Gemini Chat - LiteLLM", page_icon="🤖")
st.title("Chat with Gemini")
st.write("Type your message below and get a response from Gemini LLM.")

# Get API Key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ GEMINI_API_KEY not found in environment variables.")
    st.stop()

# Input from user
user_input = st.text_area("Enter your message:", value="How to make a chocolate cake?", height=100)

# Submit button
if st.button("Ask Gemini"):
    try:
        response = completion(
            model="gemini/gemini-2.0-flash",
            messages=[{"role": "user", "content": user_input}],
            api_key=api_key
        )
        reply = response['choices'][0]['message']['content']
        st.success("✅ Gemini says:")
        st.markdown(f"**{reply}**")

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Waniza Khan")