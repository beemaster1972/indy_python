banknotes = [100, 20, 10, 5, 1]
total_euro = int(input())
quantity, i = 0, 0

while total_euro:
    quantity += (total_euro // banknotes[i])
    total_euro -= ((total_euro // banknotes[i]) * banknotes[i])
    i += 1

print(quantity)
