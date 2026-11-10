import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello from langchain-course!")

    prompt = "Tell me a joke about a dog."
    messages = [("human", prompt)]
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=1)

    response = llm.invoke(messages)

    print(response.content)

if __name__ == "__main__":
    main()
