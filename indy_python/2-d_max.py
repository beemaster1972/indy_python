from random import randint


lst = [randint(-1000, 1000) for _ in range(10_000)]
max_index = 0
second_max_index = 0
index = 1
while index < len(lst):
    if lst[max_index] < lst[index]:
        second_max_index = max_index
        max_index = index
    elif lst[second_max_index] < lst[index] and lst[index] < lst[max_index]:
        second_max_index = index

    index += 1
arr = lst[:]
print(*lst)
print(lst[max_index],max(lst))
print(lst[second_max_index])
print(*sorted(arr, reverse=True))