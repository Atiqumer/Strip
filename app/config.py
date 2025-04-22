import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRETE_KEY = os.getenv('SECRETE KEY','Your secrete key')
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRETE_KEY')

    SESSION_TYPE = 'filesystem'