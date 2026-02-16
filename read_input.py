"""
This is only meant for updating the main.py file when the source data is modified, e.g. when finding a new triforce or
changing a description. It is not needed for executing the project.
"""

import csv

filename = "triforces.csv"

with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)

    total = 0

    data = {}

    for row in reader:
        total += int(row[0])

        if row[1] not in data:
            data[row[1]] = [0]

        data[row[1]][0] += int(row[0])
        data[row[1]].append([row[1], int(row[0])])

    keys = list(data.keys())

    for i in range(len(keys)):
        for j in range(len(keys) - i - 1):
            if keys[j] > keys[j + 1]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]

    overwrite = {"total": total}

    for i in keys:
        overwrite[i] = data[i]

    data = overwrite

    print(data)