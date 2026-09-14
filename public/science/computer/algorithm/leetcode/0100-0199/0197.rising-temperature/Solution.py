import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by="recordDate", inplace=True)
    return weather[
        (weather.temperature.diff() > 0) & (weather.recordDate.diff().dt.days == 1)
    ][["id"]]

if __name__ == "__main__":
    data = {
        "id":[1,2,3,4],
        "recordDate":pd.to_datetime(["2015‑01‑01","2015‑01‑02","2015‑01‑03","2015‑01‑04"]),
        "temperature":[10,20,10,30]
    }
    df = pd.DataFrame(data)
    print(rising_temperature(df))
