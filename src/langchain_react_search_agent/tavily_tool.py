from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatOpenAI(temperature=0, model="gpt-5")
tools = [TavilySearch()]
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
