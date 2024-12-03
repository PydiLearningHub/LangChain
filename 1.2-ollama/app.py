import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama  # Note the capital 'O'
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
  [
      ("system", "You are helpful assistance. Please respond to the question asked"),
      ("user", "Question:{question}")
  ]
)

## Streamlit framework
st.title("Langchain Demo with gemma2:2b")
input_text = st.text_input("What question you have in mind.")

## Initialize Ollama model correctly
llm = Ollama(model="gemma2:2b")  # Changed this line
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
  with st.spinner('Generating response...'):
      try:
          response = chain.invoke({"question": input_text})
          st.write(response)
      except Exception as e:
          st.error(f"An error occurred: {str(e)}")