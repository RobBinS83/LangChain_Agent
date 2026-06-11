from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(x: float) -> float:
    """
    Returns the triple of a number.

    param x: The number to be tripled.
    return: The triple of the input number.
    """
    return 3.0 * float(x)

tools = [TavilySearch(max_results=1), triple]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0).bind_tools(tools)

