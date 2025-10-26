# VideoTranscription

A Streamlit web app to transcribe, summarize, and analyze YouTube videos using LLMs (Meta Llama via Groq API). Enter a YouTube URL to get the transcript, a summary, main topics, and custom query responses.

## Features

- Extracts and displays YouTube video title and transcript.
- Summarizes the video in one sentence.
- Lists main topics covered in the video.
- Answers custom queries about the video content.
- Optionally translates transcripts to English.
- Simple web interface using Streamlit.

## Requirements

- Python 3.8+
- API key for Groq (see `.env` setup)
- The following Python packages:
  - streamlit
  - langchain
   - langchain_community
   - langchain_core
   - langchain_groq
  - python-dotenv
  - requests
  - beautifulsoup4

## Setup

1. **Clone the repository** and navigate to the `VideoTranscription` directory.

2. **Install dependencies**:
   ```powershell
   pip install streamlit langchain langchain_community langchain_core langchain_groq python-dotenv requests beautifulsoup4
   ```

3. **Set up API keys**:
   - Create a `.env` file in the `VideoTranscription` directory.
    - Add your Groq API key:
       ```
       GROQ_API_KEY=your_groq_api_key
       ```

4. **File structure**:
   ```
    VideoTranscription/
       ├── video_transcription_app.py
       ├── youtube_transcript_utils.py
       ├── .env
   ```

## Usage

1. **Start the Streamlit app**:
   ```powershell
   streamlit run video_transcription_app.py
   ```

2. **In the web UI**:
   - Enter a YouTube video URL.
   - Enter the language code (e.g., `en` for English).
   - Enter a custom query for the summary (optional, defaults to "Summarize in a clear and understandable way").
   - Optionally, check "Translate to English".
   - Click "Transcribe and Summarize".

3. **Outputs**:
   - Video information (title, URL)
   - One-sentence summary
   - Main topics
   - Detailed response to your custom query

## How it works

- The app uses `youtube_transcript_utils.py` to:
   - Fetch the video transcript and title.
   - Use a large language model (Meta Llama via Groq API) to summarize and analyze the transcript, including custom queries.
- The Streamlit UI in `video_transcription_app.py` provides a simple interface for user input and displays results.

## Notes

- Ensure your API keys are valid and have sufficient quota.
- The app is designed for educational and research purposes.
