import os

import pandas as pd

# Define the relative path to your CSV folder
# directory_path = "csv/1/"

# List to hold the individual DataFrames
dfs = []


def extract_num(filename):
    if "-" in filename:
        return int(filename[filename.index("-") + 1 : filename.index(".")])
    return 1


def combine(directory_path):
    files = sorted(
        [f for f in os.listdir(directory_path)], key=lambda x: extract_num(x)
    )

    # Loop through each file in the directory
    for f in files:
        file_path = os.path.join(directory_path, f)  # Full file path
        print(f"Reading file: {file_path}")
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        dfs.append(df)  # Append the DataFrame to the list

    # Combine all DataFrames into one
    combined_df = pd.concat(dfs, ignore_index=True)

    # Save the combined DataFrame to a new CSV file
    output_file = "combined_output.csv"
    combined_df.to_csv(output_file, index=False)

    print(f"All CSV files aggregated and saved to '{output_file}'.")
