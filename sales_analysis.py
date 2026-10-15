import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).with_name("retail_sales.csv")


def main():
    # Load the sample dataset
    sales = pd.read_csv(DATA_FILE)

    # Calculate revenue for each transaction
    sales["Revenue"] = sales["Quantity"] * sales["UnitPrice"]

    # Summarize the dataset
    total_revenue = sales["Revenue"].sum()
    total_units = sales["Quantity"].sum()

    revenue_by_product = (
        sales.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    revenue_by_region = (
        sales.groupby("Region")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    print("RETAIL SALES ANALYTICS")
    print("=" * 30)
    print(f"Total revenue: ${total_revenue:,.2f}")
    print(f"Total units sold: {total_units}")

    print("\nRevenue by product:")
    print(revenue_by_product.to_string())

    print("\nRevenue by region:")
    print(revenue_by_region.to_string())

    print("\nTop product by revenue:")
    print(f"{revenue_by_product.index[0]} (${revenue_by_product.iloc[0]:,.2f})")


if __name__ == "__main__":
    main()
