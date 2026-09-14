import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(left=person, right=address, how="left", on="personId")[["firstName", "lastName", "city", "state"]]

if __name__ == "__main__":
    p_data = {"personId":[1,2],"lastName":["Wang","Alice"],"firstName":["Allen","Bob"]}
    a_data = {"personId":[2],"city":["New York City"],"state":["New York"]}
    person_df = pd.DataFrame(p_data)
    address_df = pd.DataFrame(a_data)
    res = combine_two_tables(person_df,address_df)
    print(res)
