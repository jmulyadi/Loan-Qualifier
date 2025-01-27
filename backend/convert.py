import os

import convertapi
from dotenv import load_dotenv

load_dotenv()
convertapi.api_credentials = os.getenv("CONVERT_KEY")


def pdf_to_csv(filename):
    # output_dir = f"app/csv/{filename[:-4]}"
    # Construct the directory path inside the container
    output_dir = os.path.join("csv", filename[:-4])
    # output_dir = os.path.join("csv", filename[:-4])
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    # with open(f"{output_dir}/hi.pdf", "w") as f:
    #     f.write("Hello, this is an example file!")
    source = f"uploads/{filename}"
    convertapi.convert(
        "csv", {"File": source, "Delimiter": ","}, from_format="pdf"
    ).save_files(output_dir)
