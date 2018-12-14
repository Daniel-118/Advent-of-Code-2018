total = 0
a = 0
totals = []
filename = "input.txt"
lines = open(filename, "r").read().splitlines()
found = False
while not found:
    for i in lines:
        i = int(i)
        total = total + i
        if total in totals:
            print(total)
            found = True
            break
        else:
            totals.append(total)
print(total)
