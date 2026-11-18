import os
from langchain.chat_models import init_chat_model

import os
from dotenv import load_dotenv
load_dotenv()

model = init_chat_model("claude-sonnet-4-6")
'''
prompts = [
    {"role": "user", "content": "Hello my name is Akash Dongre"},
    {"role": "ai", "content": "Hello Akash Dongre! It's nice to meet you. 😊"},
    {"role": "user", "content": "What is my Name ? "},
]
response = model.invoke(prompts)
print(response.content)
''' 

history = []
while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit", " bye"]:
        break
    history.append({"role": "user", "content": user_input})
    respose = model.invoke(history)
    history.append({"role": "ai", "content": respose})
    print(f"AI: "+ respose.content)