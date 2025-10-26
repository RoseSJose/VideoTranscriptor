import streamlit as st
import youtube_transcript_utils as yt

st.title("YouTube Video Transcription and Summary")

video_url = st.text_input("Enter YouTube Video URL")
language = st.text_input("Enter Language Code (e.g., 'en' for English)")
custom_query = st.text_input("Enter Custom Query for Summary", value="Summarize in a clear and understandable way")
translation_option = st.checkbox("Translate to English")
print(language)

if st.button("Transcribe and Summarize"):
    if video_url and language:
        
        video_infos, about, main_topics, response = yt.interpret_video(url=video_url, query= custom_query, language=language, translation="en" if translation_option else None)
        st.subheader("Video Information")
        st.markdown(video_infos)
        st.markdown(about)
        st.markdown(main_topics)
        st.markdown(response)