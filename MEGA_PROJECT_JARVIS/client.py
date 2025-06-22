from openai import OpenAI

client = OpenAI(api_key = "{apikey}")


completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google"
        }
        {
            "role": "user",
            "content": "What is coding."
        }
    ]
)

print(completion.choices[0].message.content)