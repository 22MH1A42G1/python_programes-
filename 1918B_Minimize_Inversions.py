t=int(input())
while t >0:
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    d={}
    for i in range(n):
        d[a[i]]=b[i]
    a.sort()
    print(" ".join(map(str,a)))
    print(" ".join(map(str, [d[j] for j in a])))
    t-=1
