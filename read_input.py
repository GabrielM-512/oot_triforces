"""
This is only meant for updating the main.py file when the source data is modified, e.g. when finding a new triforce or
changing a description. It is not needed for executing the project.
"""

import csv

filename = "triforces.csv"
def main():
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)

    total = 0

    data = {}

    for row in reader:

        count = int(row[0])
        scene = row[1]
        description = row[2]

        total += count

        if scene not in data:
            data[scene] = [0]

        data[scene][0] += count
        data[scene].append([description, count])


    # I want the scenes sorted alphabetically, so we do all this
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

if __name__ == "__main__":
    main()