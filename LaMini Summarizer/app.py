import streamlit as st
import os

from summarizer.summarizer_utils import llm_pipeline
from summarizer.display_utils import display_pdf

st.set_page_config(page_title="PDF Summarizer", page_icon=":guardsman:", layout="wide")

def main():
    st.title("PDF Summarizer")
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file is not None:
        if st.button("Summarize"):
            col1, col2 = st.columns(2)
            os.makedirs("data", exist_ok=True)
            filepath = os.path.join("data", uploaded_file.name)
            with open(filepath, "wb") as temp_file:
                temp_file.write(uploaded_file.read())
            with col1:
                st.info("Uploaded PDF")
                display_pdf(filepath)
            with col2:
                st.info("Summarized Text")
                summary = llm_pipeline(filepath)
                st.success(summary)

if __name__ == "__main__":
    main()
