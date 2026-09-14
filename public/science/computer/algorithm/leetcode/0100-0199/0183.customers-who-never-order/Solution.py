import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers["id"].isin(orders["customerId"])]
    df = df[["name"]].rename(columns={"name": "Customers"})
    return df

if __name__ == "__main__":
    cust_data = {"id":[1,2,3,4], "name":["Joe","Henry","Sam","Max"]}
    ord_data = {"id":[1,2], "customerId":[3,1]}
    customers_df = pd.DataFrame(cust_data)
    orders_df = pd.DataFrame(ord_data)
    print(find_customers(customers_df, orders_df))
