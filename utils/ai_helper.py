from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"  # fast and free


def get_summary(text):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a study assistant. Summarize study material clearly with key points."
            },
            {
                "role": "user",
                "content": f"Summarize this study material and give key points:\n\n{text}"
            }
        ]
    )
    return response.choices[0].message.content


def get_quiz(text, quiz_type="mcq"):
    prompts = {
        "mcq": f"Generate 5 MCQ questions with 4 options each from this text. Label answers clearly:\n\n{text}",
        "tf": f"Generate 5 true/false questions from this text. Label answers clearly:\n\n{text}",
        "short": f"Generate 5 short answer questions from this text. Include answers:\n\n{text}"
    }
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a study assistant that generates quiz questions."
            },
            {
                "role": "user",
                "content": prompts[quiz_type]
            }
        ]
    )
    return response.choices[0].message.content


def get_chat_response(text, user_message, history):
    messages = [
        {
            "role": "system",
            "content": f"You are StudyZoneCodex AI assistant. Answer questions based on this document only. Be helpful and concise.\n\nDocument:\n{text}"
        }
    ]

    # add previous history
    for h in history:
        messages.append({"role": "user", "content": h["user"]})
        messages.append({"role": "assistant", "content": h["assistant"]})

    # add current message
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    return response.choices[0].message.content