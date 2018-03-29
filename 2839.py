a = int(input())


if a/5 < 1:
    print("-1")
elif a % 5 >= 1:
    c = int(a / 5) + 1
    b = a / 3
    if c > b:
        print(b)
    elif c < b:
        print(c)
else:
    print(int(a/5))