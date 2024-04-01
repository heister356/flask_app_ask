import os
from dotenv import load_dotenv

class DemoConfig(object):
    BASE_KEY = os.environ.get("SECRET_KEY")
    BASE_URL = os.environ.get("DATABASE_URL")