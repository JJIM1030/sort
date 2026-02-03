T = int(input())

for t in range(T):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n+1)]
    axy = []

    max_v = 0
    for i in range(n+1):
        for j in range(n+1):
            if a[i][j] == 2:
                x, y = i, j
            elif a[i][j] == 1:
                axy.append((i, j))

    for ax, ay in axy:
        dx = abs(x - ax)
        dy = abs(y - ay)
        d2 = dx**2 + dy**2
        if d2 >= max_v:
            max_v = d2

    R = 0
    while R**2 < max_v:
        R += 1

    print(f"#{t+1} {R}")
