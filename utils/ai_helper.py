import google.generativeai as genai
import os
from dotenv import load_dotenv

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def get_summary(text):#will generate the summary of the notes
    response = model.generate_content(
        f"Summarise these text. and give key points and imporant key worda from this {text}"
    )
    return response.text
    

def get_quiz(text,quiz_type = "mcq"):#will generate the quiz of the given notes 
    response = model.generate_content(f"generate {quiz_type} from this text :{text}")
    return response.text

def get_chat_response(text,user_message, history):#will response according too the chat and will generate solutions too
    chat = model.start_chat(history=[])

    full_message = f"""You are studyzonecodex.an AI study tool.
    Answer questions based only on this document. Be helpful and concise.
    
    document = {text},
    question = {user_message}"""

    response = chat.send_message(full_message)
    return response.text


