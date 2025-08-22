from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
result = model.invoke("Who is known as the god of cricket in 5 lines")
print(result.content)