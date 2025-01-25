import convertapi

convertapi.api_credentials = "secret_Q1wYRYUtqMICFfoE"
pdf_name = "1"
convertapi.convert(
    "csv", {"File": "./1.pdf", "Delimiter": ","}, from_format="pdf"
).save_files("./csv/1/")
