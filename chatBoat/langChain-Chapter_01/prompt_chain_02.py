from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate # 
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

output_parser = StrOutputParser()

llm = init_chat_model("claude-sonnet-4-6")

prompt = ChatPromptTemplate.from_messages([
    {"role": "system", "content": "You are a Language Translator and Convert input Text in {language} Language."},
    {"role": "user", "content": "{query}"}
])

# final_prompt = prompt.format_messages(language="Hinglish", query="This is beautiful house.")
# final_result = llm.invoke(final_prompt)
# print(final_result.content)

# res = llm.invoke(prompt.invoke({"language": "Hinglish", "query": "This is beautiful bungalow."}))
# print(res.content)

def strToUpper(result: str):
    return result.upper()

chains = prompt | llm | output_parser | strToUpper
res = chains.invoke({"language": "Hinglish", "query": "This is beautiful Town."})
# print(res.content)
print(res)


