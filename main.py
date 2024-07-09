import pandas as pd

AGE_DATA = "data\TS007-2021-3.csv"

if __name__ == "__main__":
    age_data = pd.read_csv(AGE_DATA)

    regions_of_24_32 = age_data.groupby