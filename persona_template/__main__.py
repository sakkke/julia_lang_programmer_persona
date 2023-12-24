import os
from dotenv import load_dotenv
from openai import OpenAI
from persona import Persona

load_dotenv()

client = OpenAI()

prompt = '''Please answer SUCCINCTLY and DIRECTLY. You are an assistant.'''

persona = Persona(client, prompt, model='gpt-4-vision-preview')
persona.run(os.getenv('TOKEN'))
