from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

azure_key = os.getenv("AZURE_KEY")
azure_endpoint = os.getenv("AZURE_ENDPOINT")
openai_key = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(api_key=openai_key)

