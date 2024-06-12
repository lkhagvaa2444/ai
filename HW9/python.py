import os
from groq import Groq

# Set your API key here
API_KEY = "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"

# Set the environment variable
os.environ["GROQ_API_KEY"] = API_KEY

def chat_with_llm(question):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    question = input("Enter your question: ")
    response = chat_with_llm(question)
    print("Response:", response)
