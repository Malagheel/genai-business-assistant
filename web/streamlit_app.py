import streamlit as st
from app.translator import translate_business_need_to_spec

st.set_page_config(page_title="GenAI Business Assistant", layout="wide")

st.title(" GenAI Business Assistant")
st.markdown("Enter a business challenge and get a structured GenAI-based solution specification.")

# User input
user_input = st.text_area("Business Problem", placeholder="e.g. We want to use AI to reduce customer service wait times.")

if st.button("Generate Specification"):
    if not user_input.strip():
        st.warning("Please enter a business problem first.")
    else:
        with st.spinner("Analyzing with LLM..."):
            output = translate_business_need_to_spec(user_input)
        st.success(" Specification generated!")
        st.markdown("###  Output")
        st.markdown(output)
