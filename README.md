## Loan Qualifier

This project uses Docker to run

## How to Start

1. Make sure Docker is installed and the daemon is running
2. Put in API keys in the .env there is a .env.example
3. Make sure to make private.key and certificate.crt for https
4. Run these Commands

  - docker compose build
  - docker compose run

---

## Overview

The **Bank Statement Analyzer** is a web application that allows users to upload **PDF** files of their bank statements. The application then processes the PDF, extracts relevant data, and generates a **rating** of how "good" or "bad" the bank statement is, based on predefined criteria. The overall rating is presented as a score out of **100**, and a summary of the bank statement is provided to give insights into the user's financial activity.

This project features an interactive **dashboard** that visually displays the rating and summary, allowing users to easily understand the quality of their financial activity over the given period.

## Features

- **PDF Upload**: Upload bank statement PDFs through the user interface.
- **Automated Analysis**: The application extracts data from the PDF (such as transactions, balances, etc.) and evaluates it based on preset criteria.
- **Rating System**: The bank statement is rated on a scale from **0 to 100**, with factors such as:
  - Spending habits
  - Savings and income trends
  - Frequency of large transactions
- **Dashboard**: A dynamic dashboard that displays:
  - **Overall score** of the bank statement
  - **Summary of the bank statement**, highlighting key insights like total income, total expenses, and notable transactions
  - **Visuals**: Charts and graphs to make it easier to digest the analysis.

## Technologies Used

- **Frontend**:
  - HTML, CSS, JavaScript, React
  - Chart.js for data visualization
- **Backend**:
  - Python (Flask/Django) or Node.js for handling backend logic
  - **PDF Parsing**: Libraries `pdfplumber` to extract text and data from PDF files
  - **Data Analysis**: Python's **Pandas** and **NumPy** for analyzing the extracted data and calculating the score
  - **Machine Learning**: A simple model could be used to rate the statement based on user-defined patterns (such as regular income deposits or spending spikes).
