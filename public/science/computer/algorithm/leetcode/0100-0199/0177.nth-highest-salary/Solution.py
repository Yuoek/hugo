import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 1:
        return pd.DataFrame({"getNthHighestSalary(" + str(N) + ")": [None]})
    unique_salaries = employee.salary.unique()
    if len(unique_salaries) < N:
        return pd.DataFrame([np.NaN], columns=[f"getNthHighestSalary({N})"])
    else:
        salary = sorted(unique_salaries, reverse=True)[N - 1]
        return pd.DataFrame([salary], columns=[f"getNthHighestSalary({N})"])

if __name__ == "__main__":
    df = pd.DataFrame({"id":[1,2,3],"salary":[100,200,300]})
    print(nth_highest_salary(df,2))
    print(nth_highest_salary(df,4))
    print(nth_highest_salary(df,0))
