import os

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def LLM():

    filename = "combined_output.csv"
    try:
        data = pd.read_csv(filename)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    csv_content = data.to_string(index=False)
    return API(csv_content)


def API(input):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
Most Important! make sure Output is valid JSON
You are an advanced AI assistant specializing in analyzing bank statements and extracting key financial features to assist in determining loan eligibility. Your task is to process a PDF of a bank statement and extract specific, relevant features to evaluate whether the individual or business qualifies for a loan.

Your output must strictly adhere to valid JSON format, organized into the following categories: Balance, Income, Expenses, Savings, Repayments, Overdrafts, Patterns, and Red_Flags. Ensure that all numeric values are provided as numbers (not strings). Use null for missing data, and provide detailed breakdowns where applicable.

### Categories and Expected Fields:
1. **Balance**:
    - "average_monthly_balance": Average monthly balance over the past 12 months.
    - "end_of_month_balances": { "YYYY-MM": Balance for each of the past 12 months }.

2. **Income**:
    - "total_credited_amounts": { "YYYY-MM": Total credited amounts for each of the past 12 months }.
    - "sources_of_income": A brief description of income consistency and sources.

3. **Expenses**:
    - "total_debited_amounts": { "YYYY-MM": Total debited amounts for each of the past 12 months }.
    - "recurring_expenses": A list of major recurring expenses with approximate amounts and descriptions.
    - "large_one_time_expenses": A list of any unusual large one-time expenses.

4. **Savings**:
    - "savings_transfers": Total transfers to savings accounts or investments over the past 12 months.
    - "wealth_building_behavior": A brief description of wealth-building behavior, if any.

5. **Repayments**:
    - "existing_loans": A list of existing loans or credit card payments being serviced.
    - "repayment_timeliness": A brief description of timeliness and regularity of payments.

6. **Overdrafts**:
    - "overdraft_usage": Frequency of overdraft usage over the past 3-6 months.
    - "negative_balances": Duration of any negative balances, if applicable.

7. **Patterns**:
    - "cash_transactions": { "deposits": Total cash deposits, "withdrawals": Total cash withdrawals over the past 3-6 months }.
    - "high_value_transactions": A list of high-value transactions with dates and amounts.

8. **Red_Flags**:
    - "declined_transactions": Count of declined transactions over the past 3-6 months.
    - "high_risk_behavior": A brief description of high-risk spending behavior, if any.
### Example output
{
  "Balance": {
    "average_monthly_balance": 55000.50,
    "end_of_month_balances": {
      "Jan": 56000.75,
      "Feb": 53000.25,
      "Mar": 54000.50,
      "Apr": 55000.00,
      "May": 57000.25,
      "Jun": 58000.75,
      "Jul": 59000.50,
      "Aug": 60000.00,
      "Sep": 61000.25,
      "Oct": 62000.75,
      "Nov": 63000.50,
      "Dec": 64000.00
    }
  },
  "Income": {
    "total_credited_amounts": {
      "Jan": 30000,
      "Feb": 32000,
      "Mar": 31000,
      "Apr": 33000,
      "May": 34000,
      "Jun": 35000,
      "Jul": 36000,
      "Aug": 37000,
      "Sep": 38000,
      "Oct": 39000,
      "Nov": 40000,
      "Dec": 41000
    },
    "sources_of_income": "Regular salary and occasional business revenue."
  },
  "Expenses": {
    "total_debited_amounts": {
      "Jan": 25000,
      "Feb": 26000,
      "Mar": 25500,
      "Apr": 26500,
      "May": 27000,
      "Jun": 27500,
      "Jul": 28000,
      "Aug": 28500,
      "Sep": 29000,
      "Oct": 29500,
      "Nov": 30000,
      "Dec": 30500
    },
    "recurring_expenses": [
      { "description": "Rent", "amount": 15000 },
      { "description": "Utilities", "amount": 3000 }
    ],
    "large_one_time_expenses": [
      { "description": "Medical bills", "amount": 5000, "date": "2023-07" }
    ]
  },
  "Savings": {
    "savings_transfers": 5000,
    "wealth_building_behavior": "Consistent monthly transfers to savings account."
  },
  "Repayments": {
    "existing_loans": [
      { "lender": "Bajaj Finance", "amount": 10000, "due_date": "2023-09-10" }
    ],
    "repayment_timeliness": "All payments made on time."
  },
  "Overdrafts": {
    "overdraft_usage": 0,
    "negative_balances": null
  },
  "Patterns": {
    "cash_transactions": { "deposits": 20000, "withdrawals": 15000 },
    "high_value_transactions": [
      { "amount": 10000, "date": "2023-09", "description": "Home repair" }
    ]
  },
  "Red_Flags": {
    "declined_transactions": 0,
    "high_risk_behavior": null
  }
}
Focus on providing accurate numbers and structured data for easier parsing. Do not include extra commentary or unrelated text in the JSON output. For Income, Expenses, and Balance make sure to have 12 entries for each for the amounts
""",
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
    return output


def get_score(input):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
    Make sure to output just a valid JSON object
    ### Example input:
    {
      "Balance": {
        "average_monthly_balance": 55000.50,
        "end_of_month_balances": {
          "2023-09": 56000.75,
          "2023-08": 53000.25,
          "2023-07": 54000.50
        }
      },
      "Income": {
        "total_credited_amounts": {
          "2023-09": 30000,
          "2023-08": 32000,
          "2023-07": 31000
        },
        "sources_of_income": "Regular salary and occasional business revenue."
      },
      "Expenses": {
        "total_debited_amounts": {
          "2023-09": 25000,
          "2023-08": 26000,
          "2023-07": 25500
        },
        "recurring_expenses": [
          { "description": "Rent", "amount": 15000 },
          { "description": "Utilities", "amount": 3000 }
        ],
        "large_one_time_expenses": [
          { "description": "Medical bills", "amount": 5000, "date": "2023-07" }
        ]
      }, # Construct the directory path inside the container
        output_dir = os.path.join("/app/csv", filename[:-4])
      "Savings": {
        "savings_transfers": 5000,
        "wealth_building_behavior": "Consistent monthly transfers to savings account."
      },
      "Repayments": {
        "existing_loans": [
          { "lender": "Bajaj Finance", "amount": 10000, "due_date": "2023-09-10" }
        ],
        "repayment_timeliness": "All payments made on time."
      },
      "Overdrafts": {
        "overdraft_usage": 0,
        "negative_balances": null
      },
      "Patterns": {
        "cash_transactions": { "deposits": 20000, "withdrawals": 15000 },
        "high_value_transactions": [
          { "amount": 10000, "date": "2023-09", "description": "Home repair" }
        ]
      },
      "Red_Flags": {
        "declined_transactions": 0,
        "high_risk_behavior": null
      }
    }
    You are a loan approval evaluator. Analyze the provided JSON, which contains financial details of a person or business, and generate:

        A score out of 100% indicating the likelihood of loan approval.
        A brief explanation summarizing the reasons for the score, based on financial health, income, expenses, savings, repayment history, overdrafts, and red flags.

    Ensure the score and explanation are fair and clearly tied to the data provided. Prioritize positive behaviors like consistent savings, timely repayments, and stable income, and penalize red flags like overdraft usage, late repayments, or high-risk patterns. Make sure summary is concise
    Give Output in json with attributes score, summary and nothing else
    """,
            },
            {
                "role": "user",
                "content": input,
            },
        ],
    )
    output = completion.choices[0].message.content
    return output


if __name__ == "__main__":
    input = """{
      "Balance": {
        "average_monthly_balance": 55000.50,
        "end_of_month_balances": {
          "2023-09": 56000.75,
          "2023-08": 53000.25,
          "2023-07": 54000.50
        }
      },
      "Income": {
        "total_credited_amounts": {
          "2023-09": 30000,
          "2023-08": 32000,
          "2023-07": 31000
        },
        "sources_of_income": "Regular salary and occasional business revenue."
      },
      "Expenses": {
        "total_debited_amounts": {
          "2023-09": 25000,
          "2023-08": 26000,
          "2023-07": 25500
        },
        "recurring_expenses": [
          { "description": "Rent", "amount": 15000 },
          { "description": "Utilities", "amount": 3000 }
        ],
        "large_one_time_expenses": [
          { "description": "Medical bills", "amount": 5000, "date": "2023-07" }
        ]
      }, # Construct the directory path inside the container
        output_dir = os.path.join("/app/csv", filename[:-4])
      "Savings": {
        "savings_transfers": 5000,
        "wealth_building_behavior": "Consistent monthly transfers to savings account."
      },
      "Repayments": {
        "existing_loans": [
          { "lender": "Bajaj Finance", "amount": 10000, "due_date": "2023-09-10" }
        ],
        "repayment_timeliness": "All payments made on time."
      },
      "Overdrafts": {
        "overdraft_usage": 0,
        "negative_balances": null
      },
      "Patterns": {
        "cash_transactions": { "deposits": 20000, "withdrawals": 15000 },
        "high_value_transactions": [
          { "amount": 10000, "date": "2023-09", "description": "Home repair" }
        ]
      },
      "Red_Flags": {
        "declined_transactions": 0,
        "high_risk_behavior": null
      }
    }"""
    output = get_score(input)
    print(output)
    data = json.load(output)
    print()
