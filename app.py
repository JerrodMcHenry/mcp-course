import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello in one short sentence."
)

print(response.text)

chat = client.chats.create(model="gemini-2.5-flash")

response = chat.send_message("What is the current price of Bitcoin?")
print(response.text)

print(response)

url = f"https://www.binance.com/en/price/bitcoin"
response = requests.get(url)
data = response.json()
print(data)