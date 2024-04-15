import streamlit as st
import langchain_helper as lch
import textwrap
from dotenv import load_dotenv
import os
import random

huggingface_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
load_dotenv()

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="What is the YouTube video URL?",
            max_chars=50
            )
        
        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
            )
        if not huggingface_api_key:

            huggingface_api_key =  st.sidebar.text_input(
                label="huggingface API Key",
                key="langchain_search_api_key_huggingface",
                max_chars=50,
                type="password"
                )

        submit_button = st.form_submit_button(label='Submit')

if query and youtube_url:
    if not huggingface_api_key:
        st.info("Please add your Huggingface API key to continue.")
        st.stop()
    else:
        db = lch.create_db_from_youtube_video_url(youtube_url)
        response, docs = lch.get_response_from_query(db, query)
        st.subheader("Answer:")
        st.text(textwrap.fill(response, width=85))