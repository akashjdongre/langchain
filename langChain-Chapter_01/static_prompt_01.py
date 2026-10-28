import os
from langchain.chat_models import init_chat_model

import os
from dotenv import load_dotenv
load_dotenv()

model = init_chat_model("claude-sonnet-4-6")

prompts = [
    ("system", "You are a helpful assistant."),
    ("user", "Why do parrots talk?"),
]

'''
system => Assign role / behaviour to the model. Helps guide the model's responses.
user => The user input. This is the prompt that the model will respond to.
ai => The model's response. Sends back
'''

response = model.invoke(prompts)

print(response.content)