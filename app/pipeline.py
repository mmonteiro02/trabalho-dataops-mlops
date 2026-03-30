import pandas as pd
import os

def process_data():
    df = pd.read_csv("data/sales.csv")

    summary = df.groupby("product")["amount"].sum().reset_index()

    os.makedirs("output", exist_ok=True)
    summary.to_csv("output/summary.csv", index=False)

    return summary

if __name__ == "__main__":
    process_data()