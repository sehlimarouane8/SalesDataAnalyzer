import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "sales_data.csv"

def load_data():
    return pd.read_csv(DATA_FILE)

def top_products(df, n=5):
    return df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(n)

def monthly_revenue(df):
    df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M")
    return df.groupby("Month")["Revenue"].sum()

def plot_revenue(revenue):
    revenue.plot(kind="bar", title="Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_data()
    print("Top 5 Products by Revenue:")
    print(top_products(df))
    
    revenue = monthly_revenue(df)
    print("\nMonthly Revenue:")
    print(revenue)
    
    plot_revenue(revenue)
