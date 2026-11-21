import os
from langchain.chat_models import init_chat_model

import os
from dotenv import load_dotenv
load_dotenv()

model = init_chat_model("claude-sonnet-4-6")

response = model.invoke("How Lunar Eclipse occurs ?")

print(response.content)