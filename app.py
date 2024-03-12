import streamlit as st
from utils import * 
from collections import Counter
import nltk
from nltk.corpus import stopwords
import pandas as pd
def main():
    # Set the title and introduction
    st.title("Audio Transcriber")
    #st.success("Welcome to our Audio Transcription App! It's more than just transcribing – we summarize, analyze, and convert your conversations to text. Uncover insights effortlessly, turning spoken words into valuable information with ease.")

    # File upload section
    uploaded_files = st.file_uploader("Upload recorded .mp3 files", type=["mp3"], accept_multiple_files=True)
    if uploaded_files:
        st.write("Uploaded Files:")

        # Set button width
        button_width = 200
        st.markdown(f"""
        <style>
        div.stButton > button:first-child {{
            width: {button_width}px;
        }}
        </style>
        """, unsafe_allow_html=True)

        # Iterate through uploaded files
        for idx, uploaded_file in enumerate(uploaded_files):
            file_name = uploaded_file.name

            # Display file information in columns
            col1, col2, col3 = st.columns([0.1, 1, 2])
            with col1:
                st.write("-")
            with col2:
                st.write(file_name)
            with col3:
                # Sidebar section for various actions
                st.sidebar.markdown("Automated audio transcription service.")

                # Transcribe Audio button
                if st.sidebar.button(f"Transcribe Audio {idx}", key=f"transcribe_{idx}"):
                    Only_text = Audio_Transcriber(file_name)
                    st.write(Only_text)
                    st.sidebar.success("Successfully Extract text from audio")

                # Fetch Conversation button
                st.sidebar.markdown("Retrieve chat-style audio transcripts.")
                if st.sidebar.button(f"Fetch Conversation {idx}", key=f"fetch_conversation_{idx}"):
                    Only_text = Audio_Transcriber(file_name)
                    Conversation = Converstaion_Style(Only_text)
                    st.write(Conversation)
                    st.sidebar.success("Successfully Extract Conversation from audio")

                # Summarization button
                st.sidebar.markdown("Summarize Conversation Simply")
                if st.sidebar.button(f"Summarization {idx}", key=f"Summarization{idx}"):
                    Only_text = Audio_Transcriber(file_name)
                    Summary = TextSummarization(Only_text)
                    st.write(Summary)
                    st.sidebar.success("Successfully Extract Summary from audio")

                # Analysis button
                st.sidebar.markdown("Analyze Conversation Simply")
                if st.sidebar.button(f"Analysis {idx}", key=f"Analysis{idx}"):
                    Only_text = Audio_Transcriber(file_name)
                    Conversation = Converstaion_Style(Only_text)

                    # Analyze word frequency and create a horizontal bar chart
                    words = []
                    df = pd.DataFrame(Conversation)
                    for message in df['message']:
                        for word in message.lower().split():
                            if word not in stopwords.words('english'):
                                words.append(word)

                    most_common_df = pd.DataFrame(Counter(words).most_common(20))
                    fig, ax = plt.subplots()
                    newgh = ax.barh(most_common_df[0], most_common_df[1])

                    # Rotate x-axis labels
                    plt.xticks(rotation='vertical')

                    # Add labels and title
                    ax.set_xlabel('Frequency')
                    ax.set_ylabel('Words')
                    ax.set_title('Word Frequency in a Horizontal Bar Chart')

                    # Show the plot
                    st.pyplot(fig)
                    a = plt.show()
                    st.write(most_common_df)

                    # Display unique user names and their count
                    user = df['name'].unique().tolist()
                    st.write("Users Name", user)
                    st.write("Number of the User", len(user))
                    st.sidebar.success("Successfully Completed Analysis")

# Run the Streamlit app
if __name__ == "__main__":
    main()
