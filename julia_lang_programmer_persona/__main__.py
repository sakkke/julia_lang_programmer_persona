import os
from dotenv import load_dotenv
from openai import OpenAI
from persona import Persona

load_dotenv()

client = OpenAI()

prompt = '''Please answer SUCCINCTLY and DIRECTLY.
You are a Julia programming language professional, CASUAL, FUN, EASY TO TALK TO, and PRECISE.
Your goal is to help users with Julia programming skills.'''

persona = Persona(client, prompt, model='gpt-4-vision-preview')
persona.run(os.getenv('TOKEN'))
