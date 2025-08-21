from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

result = model.invoke("Write a 5 line poem on Cricket")
print(result.content)