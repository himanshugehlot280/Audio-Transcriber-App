Project Description: 
Audio Transcription and Analysis App


Overview:
This Python project is a Streamlit-based web application designed for transcribing audio files, extracting insights, and performing various analyses on the transcribed text. The application utilizes OpenAI's language model and offers features such as automated audio transcription, chat-style conversation extraction, summarization, and basic analysis of the transcribed content.

Features:
Automated Audio Transcription:

Users can upload recorded .mp3 files.
The app leverages the OpenAI language model to transcribe the audio files into text.
Conversation Extraction:

Users can fetch chat-style conversation transcripts from the transcribed text.
The app utilizes a prompt template to structure the text into a JSON format representing a conversation.
Text Summarization:

Users can obtain a concise summary of the transcribed text using OpenAI's language model.
The summarization is based on a predefined conversation template.
Basic Analysis:

Users can perform a simple analysis of the transcribed content.
The app generates a horizontal bar chart showing word frequency and displays unique user names along with their count.

Project Structure:
app.py:

The main Streamlit application script containing the user interface and interaction logic.
Handles file upload, sidebar actions, and displays transcriptions, conversation, summary, and analysis results.
Utilizes functions from utils.py for audio transcription, conversation extraction, summarization, and analysis.

utils.py:

Contains utility functions for interacting with OpenAI's language model.
Functions include Audio_Transcriber for audio transcription, Converstaion_Style for conversation extraction, and TextSummarization for text summarization.
Dependencies:
streamlit: Web application framework for interactive UI.
whisper: Library for interacting with OpenAI's language model.
nltk: Natural Language Toolkit for text processing.
pandas: Data manipulation library for handling data frames.
matplotlib: Plotting library for generating visualizations.
python-dotenv: Library for managing environment variables.
Getting Started:
Clone the repository.
Install dependencies using pip install -r requirements.txt.
Set up your OpenAI API key in a .env file.
Run the Streamlit app using streamlit run app.py.
Notes:
The application is structured to support future upgrades, including potential integration with Zapier.
Properly documented code and clear comments are provided for better understanding.
Feel free to customize and extend the functionality based on your specific requirements. Happy transcribing and analyzing! 

For Running the application Command is: 
Streamlit run app.py
