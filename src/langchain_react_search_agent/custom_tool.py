from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()


@tool
def search(query: str) -> str:
    """
    Tool that searchs over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Search for {query}")
    return tavily.search(query=query, max_results=3)


llm = ChatOllama(temperature=0, model="gpt-oss:20b", num_ctx=16384)
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main() -> None:
    print("Hello from langchain-react-search-agent!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="search for 3 job postings for an ai engineer using langchain in belo horizonte - minas gerais - brazil, on linkedin, and list their details"
            )
        },
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
