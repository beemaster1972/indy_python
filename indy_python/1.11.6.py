from math import ceil
classes = list(map(int,input().split()))
print(sum([ceil(clas/2) for clas in classes]))