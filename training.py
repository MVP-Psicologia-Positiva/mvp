import streamlit as st
from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI"]["api_key"])

client.fine_tuning.jobs.create(
  training_file="training_files/mvpTraining.docx", 
  model="gpt-4o-mini-2024-07-18"
)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "what is your name?"},
  ]
)

message = response.choices[0].message.content
