import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
    PLAID_SECRET = os.getenv("PLAID_SECRET")
