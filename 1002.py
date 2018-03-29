import math

count = int(input())
min = 1

pResult = [1] * count

while min <= count:
    x1, y1, r1, x2, y2, r2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    r1 = int(r1)
    r2 = int(r2)

    distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

    if distance == 0:
        if r1 == r2:
            pResult[min-1] = -1
        else:
            pResult[min-1] = 0
    else:
        if abs(r1-r2) < distance:
            if r1+r2 < distance:
                pResult[min-1] = 0
            elif r1+r2 == distance:
                pResult[min-1] = 1
            elif r1+r2 > distance:
                pResult[min-1] = 2

        elif abs(r1-r2) > distance:
            pResult[min-1] = 0
        elif abs(r1-r2) == distance:
            pResult[min-1] = 1

    min += 1

for o in pResult:
    print(o)