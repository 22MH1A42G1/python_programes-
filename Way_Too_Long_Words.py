t=int(input())
for _ in range(t):
    s=input()
    l=len(s)-2
    print(s[0]+f'{l}'+s[-1] if len(s)>10 else s)
