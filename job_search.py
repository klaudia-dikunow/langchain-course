from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


llm = ChatOpenAI(model="gpt-4o-mini")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="Znajdź mi 3 oferty pracy, które wymagają znajomości LangChain w Warszawie aktualnych na 12.11.2026")})
    print(result)

if __name__ == "__main__":
    main()
