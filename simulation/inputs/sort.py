#!/usr/bin/python3

x_cords, y_cords = [],[]

with open("hospitals.csv", "rt") as fio:
    for line in fio:
        line = [item.strip() for item in line.split(",")]


        x = int(line[1])
        y = int(line[2])
        
        x_cords.append(x)
        y_cords.append(y)

print(
    f"Got min_x: {min(x_cords)}, max_x: {max(x_cords)}\n"
    f"Got min_y: {min(y_cords)}, max_y: {max(y_cords)}"
)
