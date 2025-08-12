import pandas as pd

def big_countries( world: pd.DataFrame) -> pd.DataFrame:
    return world[(world["population"] > 25000000) | (world["area"] > 3000000)][["name", "area", "population"]]
data = {
    "name": ["China", "USA", "India", "Australia", "Iceland"],
    "population": [1400000000, 330000000, 1380000000, 25000000, 350000],
    "area": [9600000, 9834000, 3287000, 7692000, 103000]
}

df = pd.DataFrame(data)

print(big_countries(df))

