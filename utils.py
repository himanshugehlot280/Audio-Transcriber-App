# Import necessary libraries and modules
import whisper
from langchain.llms import OpenAI
from langchain.agents import initialize_agent 
# Below Two are additional module for future upgradations 
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper
import os 
from langchain import tools 
from langchain.prompts import PromptTemplate 
import json
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
) 
import pandas as pd 
import matplotlib.pyplot as plt
from dotenv import load_dotenv 


# Load environment variables
load_dotenv()
key = os.environ.get("OPENAI_API_KEY")

# Function to transcribe audio using OpenAI language model
def Audio_Transcriber(file):
    """
    Transcribe an audio file using the OpenAI language model.

    Parameters:
    - file (str): Path to the audio file.

    Returns:
    - str: Transcribed text.
    """
    # Initialize OpenAI language model
    # llm = OpenAI(temperature=0.3,key=key)
    model = whisper.load_model("base")

    # Transcribe audio file
    result = model.transcribe(file)
    return result["text"] 

# Function to convert a passage into a conversation in JSON format
def Converstaion_Style(pages_data):
    """
    Convert a passage into a conversation in JSON format using the OpenAI language model.

    Parameters:
    - pages_data (str): Input passage.

    Returns:
    - list: List of dictionaries representing conversation messages.
    """
    template = """Convert the following passage into a conversation in JSON format, where each speaker's lines are represented as a dictionary with "name" and "message" keys:
    : {pages}

    Format the extracted output as JSON with the following keys only: 
    Name 
    """
    prompt_template = PromptTemplate(input_variables=["pages"], template=template)

    # Create an instance of the OpenAI language model
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.3, max_tokens=1000)

    # Generate conversation messages
    full_response = llm(prompt_template.format(pages=pages_data))
    messages = json.loads(full_response)
    return messages

# Function to extract unique names and their count from a passage 
# This work already Included in Analysis part
# def Details(pages_data):
#     """
#     Extract unique names and their count from a passage using the OpenAI language model.

#     Parameters:
#     - pages_data (str): Input passage.

#     Returns:
#     - dict: Dictionary containing unique names and their count.
#     """
#     template = """Extract ONLY the Unique Names and Count of pepoles: 
#     Name: {pages}

#     Format the extracted output as JSON with the following keys only: 
#     Name 
#     """
#     prompt_template = PromptTemplate(input_variables=["pages"], template=template)

#     llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.3)
#     full_response = llm(prompt_template.format(pages=pages_data))
#     data_dict = json.loads(full_response) 
#     return data_dict 

# Function to summarize text using the OpenAI language model
def TextSummarization(speech):  
    """
    Summarize a piece of text using the OpenAI language model.

    Parameters:
    - speech (str): Input text to be summarized.

    Returns:
    - str: Summarized text.
    """
    chat_messages = [
        SystemMessage(content='You are an expert assistant with expertise in summarizing Call Recordings'),
        HumanMessage(content=f'Please provide a short and concise summary of the following Call Recordings:\n TEXT: {speech}')
    ]
    llm = ChatOpenAI(model_name='gpt-3.5-turbo') 
    Summarize_text = llm(chat_messages).content 
    return Summarize_text
