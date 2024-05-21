s1 = input()
s2 = input()
a = list(s1)
a1=s1.find("A")-1
b1=s1.find("B")
a[b1] = "#"
i = 0
while i<len(s1):
    if s1[i] == "A":
        b1+=i
    i+=1
a[b1-a1] = "B"
print(''.join(a)==s2,''.join(a))
