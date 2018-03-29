order = int(input())

if order % 5 == 0:
    print(order // 5)

elif order % 5 == 3:
    print(order // 5 + 1)

elif order // 5 - 1 >= 0 and order - (5 * (order // 5 - 1)) == 6:
    print((order // 5 - 1) + 2)

elif order // 5 - 1 >= 0 and order - (5 * (order // 5 - 1)) == 9:
    print((order // 5 - 1) + 3)

elif order // 5 - 2 >= 0 and order - (5 * (order // 5 - 2)) == 12:
    print((order // 5 - 2) + 4)

else:
    print(-1)