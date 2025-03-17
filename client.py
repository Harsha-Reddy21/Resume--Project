import os 
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
groq_apikey=os.getenv('GROQ_APIKEY')


client=Groq(api_key=groq_apikey)