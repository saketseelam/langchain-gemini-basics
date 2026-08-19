from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

response = model.invoke("Explain the code in main.py")

if isinstance(response.content, list):
    print("".join(part.get("text", "") for part in response.content if isinstance(part, dict)))
else:
    print(response.content)