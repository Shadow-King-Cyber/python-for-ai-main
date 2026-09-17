"""Read sales from a CSV, compute totals, and print a summary."""
from pathlib import Path

import pandas as pd

from sales_analysis.helpers import calculate_total, format_currency

# CSV path relative to this script (independent of the working directory)
DATA_FILE = Path(__file__).resolve().parent / "data" / "sales.csv"


def main() -> None:
    try:
        df = pd.read_csv(DATA_FILE)
    except (FileNotFoundError, OSError):
        print(f"Error: no se encontró el archivo {DATA_FILE}. Asegúrate de que data/sales.csv existe.")
        return
    else:
        # Total for each row (quantity * price)
        df["total"] = df.apply(
            lambda row: calculate_total(row["quantity"], row["price"]), axis=1
        )

    print("Sales Data:")
    for _, row in df.iterrows():
        print(f"{row['product']}: {format_currency(row['total'])}")

    grand_total = df["total"].sum()
    print(f"\nGrand Total: {format_currency(grand_total)}")


if __name__ == "__main__":
    main()
