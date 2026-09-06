import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    salary_cutoff = (
        employee.drop_duplicates(["salary", "departmentId"])
        .groupby("departmentId")["salary"]
        .nlargest(3)
        .groupby("departmentId")
        .min()
    )
    employee["Department"] = department.set_index("id")["name"][
        employee["departmentId"]
    ].values
    employee["cutoff"] = salary_cutoff[employee["departmentId"]].values
    return employee[employee["salary"] >= employee["cutoff"]].rename(
        columns={"name": "Employee", "salary": "Salary"}
    )[["Department", "Employee", "Salary"]]

if __name__ == "__main__":
    emp_data = {
        "id":[1,2,3,4,5,6,7],
        "name":["Joe","Henry","Sam","Max","Janet","Randy","Will"],
        "salary":[85000,80000,60000,90000,69000,85000,70000],
        "departmentId":[1,2,2,1,1,1,1]
    }
    dep_data = {"id":[1,2],"name":["IT","Sales"]}
    emp_df = pd.DataFrame(emp_data)
    dep_df = pd.DataFrame(dep_data)
    print(top_three_salaries(emp_df, dep_df))
