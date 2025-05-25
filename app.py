import streamlit as st
from model_loader import load_model, generate_response

st.set_page_config(page_title="Phi2-GPTQ Chatbot", layout="centered")
st.title("🧠 Phi2-GPTQ Chatbot (Streamlit Cloud)")

prompt = st.text_area("Enter a prompt:", value="What is Artificial Intelligence?", height=150)

if 'model' not in st.session_state:
    with st.spinner("Loading Phi2-GPTQ model from Hugging Face..."):
        tokenizer, model = load_model()
        st.session_state.tokenizer = tokenizer
        st.session_state.model = model
        st.success("Model loaded successfully!")

if st.button("Generate"):
    if prompt.strip():
        with st.spinner("Generating response..."):
            response = generate_response(prompt, st.session_state.tokenizer, st.session_state.model)
            st.write("### Output")
            st.success(response)
    else:
        st.warning("Please enter a prompt.")
