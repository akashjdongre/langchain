from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool

@tool
def add_numbers(a:int, b:int):
    """
    Addition of two numbers a and b
    """
    result = a + b
    return result

@tool
def multiplication(a:int, b:int):
    """
    Multiplication of two numbers a and b
    """
    result = a * b
    return result

# res = multiplication.invoke({"a": 15, "b": 3})
# print(res)

llm_agent = create_agent(
    model="claude-sonnet-4-6",
    tools=[add_numbers, multiplication],
    system_prompt="You are Calculater Agent, you can perform all calculation of two numbers."
)

result = llm_agent.invoke({"messages": [{"role": "user", "content": "Whats is the result of (15 + 3) * 4?"}]})
print(result["messages"][-1].content)