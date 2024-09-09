import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id_from_url(url):
    if 'youtube.com/watch?v=' in url:
        return url.split('v=')[1].split('&')[0]
    elif 'youtu.be/' in url:
        return url.split('youtu.be/')[1].split('?')[0]
    elif 'youtube.com/shorts/' in url:
        return url.split('shorts/')[1].split('?')[0]
    else:
        raise ValueError("URL is not a valid YouTube URL")

def format_transcript_as_paragraph(transcript):
    return ' '.join([segment['text'] for segment in transcript])

def fetch_transcript(url, language_code):
    try:
        video_id = get_video_id_from_url(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
        formatted_transcript = format_transcript_as_paragraph(transcript)
        return formatted_transcript
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An error occurred: {e}"

st.title('YouTube Transcript Converter')

url = st.text_input('Enter YouTube URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID or https://youtu.be/VIDEO_ID):')
language_options = {
    'English': 'en',
    'Telugu': 'te',
    'Hindi':'hi',
    'Tamil':'ta',
    "kannada":'kn',
}
selected_language = st.selectbox('Select Language', list(language_options.keys()))
if url and selected_language:
    language_code = language_options[selected_language]
    transcript = fetch_transcript(url, language_code)
    st.subheader('Transcript:')
    st.write(transcript)