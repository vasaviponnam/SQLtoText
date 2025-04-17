import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("api"))
genai.configure(api_key=os.getenv("api"))


models = genai.list_models()
for m in models:
    print(m.name, "supports", m.supported_generation_methods)