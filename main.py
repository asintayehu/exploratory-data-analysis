import pandas as pd

df = pd.read_csv('Air_Quality.csv')

df.drop(["Message"], axis=1, inplace=True)

measure_info = ["ppb", "mcg/m3"]

for i in df["Measure Info"]:
    df.drop(df[df["Measure Info"] != "ppb"].index, inplace=True)

print(df.head())
print(df.info())

# majority_temp_measure = measure_dict

# print(majority_temp_measure)

# df.drop(df[df["Measure"] != "Mean"].index, inplace=True)

# # df.drop(df[df["Measure Info"] != str(majority_temp_measure)].index, inplace=True)

# df.drop(df[df["Measure Info"] != "ppb"].index, inplace=True)


# print(df.head())




# want the majority
