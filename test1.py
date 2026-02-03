T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n + 1)]

    x = y = -1
    houses = []

    for i in range(n + 1):
        for j in range(n + 1):
            if a[i][j] == 2:
                x, y = i, j
            elif a[i][j] == 1:
                houses.append((i, j))

    max_d2 = 0
    for hx, hy in houses:
        dx = x - hx
        dy = y - hy
        d2 = dx*dx + dy*dy
        if d2 > max_d2:
            max_d2 = d2

    # R = ceil(sqrt(max_d2)) 를 정수 연산으로 구하기
    R = 0
    while R * R < max_d2:
        R += 1

    print(f"#{tc} {R}")
