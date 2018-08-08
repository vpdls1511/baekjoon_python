dt = [0]*1000
n = int(input())

def min(a,b):
    return a>b and int(b) or int(a)

dt[1] = 0

for i in range(2,n+1):
    dt[i] = dt[i-1]+1
    j = int(i)
    if(j%2==0) : dt[j] = min(dt[j],dt[int(j/2)]+1)
    if(j%3==0) : dt[j] = min(dt[j],dt[int(j/3)]+1)
    
print(dt[n])
