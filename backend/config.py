import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    HF_API_KEY = os.getenv("HF_API_KEY")
