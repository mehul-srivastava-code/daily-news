from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(
  model="gemini-3.8-flash",
  temperature=0.7
 )
message="genrate random texts"
response=llm.invoke(message)
ans = response.content
if isinstance(ans, list):
        ans = "\n".join(
            block["text"]
            for block in ans
            if isinstance(block, dict) and block.get("type") == "text"
        )
with open("bot_contributer.txt", "w", encoding="utf-8") as file:
    file.write(ans)
