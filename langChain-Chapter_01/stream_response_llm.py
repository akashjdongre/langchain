from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model("claude-sonnet-4-6",stream=True)

question = "Write essay on India ?"
res = model.stream(question)

for chunk in res:
    print(chunk.content,end="",flush=True)