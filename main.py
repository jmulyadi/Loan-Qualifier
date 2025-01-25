import os

import convertapi
from dotenv import load_dotenv

load_dotenv()
convertapi.api_credentials = os.getenv("CONVERT_KEY")

# goal before lunch have a frontend that accepts a file
