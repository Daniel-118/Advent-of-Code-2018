total = 0
filename = "input.txt"
lines = open(filename, "r").read().splitlines()
for i in lines:
    i = int(i)
    total = total + i
print(total)
