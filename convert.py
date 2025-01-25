import os

import convertapi
from dotenv import load_dotenv

load_dotenv()
convertapi.api_credentials = os.getenv("CONVERT_KEY")


def pdf_to_csv():
    pdf_name = "1"
    convertapi.convert(
        "csv", {"File": "./1.pdf", "Delimiter": ","}, from_format="pdf"
    ).save_files("./csv/1/")
