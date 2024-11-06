from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = 'https://ai-calculator-nine.vercel.app/'
PORT = 8000
ENV = 'dev'
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')