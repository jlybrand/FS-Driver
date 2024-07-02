import pandas as pd
import pickle
import os

df = pd.read_excel("fs-driver/assets/subdivision_sorted.xlsx")

subdivisions = {}

for index, row in df.iterrows():
    key = (row['Elementary'], row['Middle'], row['High'])
    value = row['Subdivision']

    if key in subdivisions:
        subdivisions[key].append(value)
    else:

        subdivisions[key] = [value]

with open('subdivisions.py', "wb") as data_file:
    pickle.dump(subdivisions, data_file)


with open('subdivisions.py', 'rb') as file:
    loaded_data = pickle.load(file)

print('Loaded data:', loaded_data)

