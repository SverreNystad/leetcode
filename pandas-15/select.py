import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    cols = ["name", "age"]
    selected = students.loc[students["student_id"] == 101]
    return selected[cols]


if __name__ == "__main__":
    df = pd.DataFrame(
        columns=["student_id", "name", "age"],
        data=[
            [101, "Ulsses", 13],
            [53, "William", 10],
        ],
    )
    print(selectData(df))
