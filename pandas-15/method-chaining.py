import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    threshold = 100

    heavy_animals = animals.loc[animals["weight"] > threshold]
    heavy_animals = heavy_animals.sort_values(by="weight", ascending=False)
    return heavy_animals[["name"]]
