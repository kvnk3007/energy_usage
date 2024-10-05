"""Module providing a function printing python version."""

import pandas as pd

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

print("main v2")
print("************* hello   *************\n")

df = pd.read_csv("infiles//HDF_kW_10003448599_05-10-2024.csv")
# print(df.head(3))
df["Read Date and End Time"] = pd.to_datetime(
    df["Read Date and End Time"], format="%d-%m-%Y %H:%M"
)

df = df[["Read Value", "Read Date and End Time"]]
df["date"] = pd.to_datetime(df["Read Date and End Time"]).dt.date
df = df.drop("Read Date and End Time", axis=1)

print (df.head(3))

print(df.groupby(["date"], as_index=False).sum())
print("************* Goodbye *************")
