import os
from dotenv import load_dotenv

load_dotenv()

class Data:

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")

    LOGIN2 = os.getenv("LOGIN2")
    PASSWORD2 = os.getenv("PASSWORD2")