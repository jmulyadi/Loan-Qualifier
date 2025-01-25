import os

import pandas as pd
from openai import OpenAI


def main():
    filename = "combined_output.csv"
    try:
        data = pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    csv_content = data.to_string(index=False)
    API(csv_content)


def API(input):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are an advanced AI assistant specializing in analyzing bank statements and extracting key financial features to assist in determining loan eligibility. Your task is to process a PDF of a bank statement and extract specific, relevant features to evaluate whether the individual or business qualifies for a loan.

Focus on the following features:

1. **Account Balance**
    
    - Average monthly balance over the past 3-6 months.
    - End-of-month balances for the last 3-6 months.
2. **Income**
    
    - Total credited amounts for each month.
    - Consistency and sources of income (e.g., salary, business revenue, dividends).
3. **Expenses**
    
    - Total debited amounts for each month.
    - Major recurring expenses (e.g., rent, loan repayments, utilities).
    - Unusual or large one-time expenses.
4. **Savings and Investment Behavior**
    
    - Presence of transfers to savings accounts or investments.
    - Evidence of wealth-building behavior.
5. **Loan Repayment History**
    
    - Any existing loan or credit card payments.
    - Timeliness and regularity of these payments.
6. **Overdrafts and Negative Balances**
    
    - Frequency of overdraft usage.
    - Duration of negative balances, if any.
7. **Transaction Patterns**
    
    - Cash deposits and withdrawals.
    - Frequency and amounts of high-value transactions.
8. **Red Flags**
    
    - Declined transactions or insufficient funds notices.
    - High-risk spending behavior (e.g., gambling, irregular patterns).

Your output should be structured as a clear and concise summary of these features, along with any observations about financial health that might affect the loan decision. Avoid making the loan decision yourself; instead, focus on providing all relevant information to enable an informed decision.""",
            },
            {
                "role": "user",
                "content": input,
            },
        ],
    )
    output = completion.choices[0].message.content
    with open("output.md", "w") as file:
        file.write(output)
    print(output)


if __name__ == "__main__":
    main()
