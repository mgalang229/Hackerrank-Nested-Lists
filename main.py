import sys

n = int(input())
a = []

for i in range(n):
    name = str(input())
    grade = float(input())
    temp = [name, grade]
    a.append(temp)

mn1 = sys.maxsize
for x, y in a:
    mn1 = min(mn1, y)

mn2 = sys.maxsize
for x, y in a:
    if y != mn1:
        mn2 = min(mn2, y)

ans = []
for x, y in a:
    if y == mn2:
        ans.append(x)

ans.sort()
for name in ans:
    print(name)

