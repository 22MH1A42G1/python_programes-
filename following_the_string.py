for _ in range(int(input())):
    n = int(input())
    ans= [97] * (n+1)
    A = [int(i) for i in input().split()]
    s = ''
    for j in range(n):
        s += chr(ans[A[j]])
        ans[A[j]] += 1
    print(s)
