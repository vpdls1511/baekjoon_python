count = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]
zer = []
onr = []

def fibo(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    zer.append(zero[num])
    onr.append(one[num])

for o in range(count):
    k = int(input())
    fibo(k)

for i in range(len(zer)):
    print(zer[i],onr[i])