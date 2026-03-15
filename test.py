from google import genai

client = genai.Client(api_key="AIzaSyA49g7Aw9D--kks7GUNUaBI7I8-6nwncqo")

resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello"
)

print(resp.text)