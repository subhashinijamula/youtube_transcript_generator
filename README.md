# youtube_transcript_generator
A Streamlit app that allows users to input YouTube video URLs and obtain transcripts in various languages, including English, Telugu, Tamil, Kannada and Hindi. The app supports standard YouTube videos, shortened URLs, and YouTube Shorts.

## Features

- Extracts transcripts from YouTube videos and Shorts.
- Supports multiple languages including English, Telugu, and Hindi.
- Displays transcripts as a formatted paragraph.

## Requirements

- Python 3.x
- Streamlit
- youtube-transcript-api


4. **Install the required libraries:**

   bash
   pip install streamlit youtube-transcript-api
   

## Usage

1. **Run the Streamlit app:**

   bash
   streamlit run app.py
   

2. **Open your web browser and go to:**

   
   http://localhost:8501
   

3. **Enter the YouTube URL**: You can input URLs for standard YouTube videos, shortened URLs, or YouTube Shorts.

4. **Select the language**: Choose from English, Telugu, Tamil, Kannada or Hindi.

5. **View the transcript**: The app will display the transcript in the selected language.

## Code Overview

- **`app.py`**: Main script for the Streamlit app. Contains functions to extract video IDs, fetch transcripts, and format them into paragraphs. Also includes Streamlit components for user interaction.

