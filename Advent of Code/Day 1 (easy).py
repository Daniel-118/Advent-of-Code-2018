total = 0
filename = "day_1_input.txt"
lines = open(filename, "r").read().splitlines()
for i in lines:
    i = int(i)
    total = total + i
print(total)
