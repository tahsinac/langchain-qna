import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os


## Streamlit UI
st.set_page_config(page_title="ELI11 Q&A Chatbot")
st.header("Hey, Let's Chat!")


chat=ChatOpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"),temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="You are an AI assitant that gives explanations in such a way that eleven year olds can understand them.")
    ]


def get_chatmodel_response(question):
    """
    Get a chat model response based on the user's question.

    Parameters:
    question (str): The user's question.

    Returns:
    str: The content of the chat model's response.
    """
    # Append the user's question to the 'flowmessages' list in the session state
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    
    # Get a response from the chat model based on the current 'flowmessages'
    answer = chat(st.session_state['flowmessages'])
    
    # Append the chat model's response to the 'flowmessages' list in the session state
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    
    # Return the content of the chat model's response
    return answer.content

input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("Send")

if submit:
    st.subheader("Reply:")
    st.write(response)













