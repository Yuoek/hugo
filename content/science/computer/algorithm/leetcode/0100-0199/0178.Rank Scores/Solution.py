import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)
    result_df = scores.drop("id", axis=1).sort_values(by="score", ascending=False)
    return result_df

if __name__ == "__main__":
    data = {"id":[1,2,3,4,5,6],"score":[3.50,3.65,4.00,3.85,4.00,3.65]}
    df = pd.DataFrame(data)
    print(order_scores(df))
