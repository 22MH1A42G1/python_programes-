t = int(input())
for _ in range(t):
    T = input()
    h, m = map(int, T.split(':'))
    p = "AM" if h < 12 else "PM"
    h = h % 12
    if h == 0:
        h = 12
    print(f"{h:02d}:{m:02d} {p}")
