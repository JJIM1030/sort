tc = int(input())

for t in range(tc):
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]

    res = {}
    m = 0
    for i in range(n):
        for j in range(n):
            # 내가 보려는 곳. MAP[i][j]
            cur = 0
            for x in range(i + 1, n):
                for y in range(j + 1, n):
                    if MAP[i][j] == MAP[x][y]:
                        cur = (x - i + 1) * (y - j + 1)
                        try:
                            res[cur] += 1
                        except:
                            res[cur] = 1
                        m = max(m, cur)
    print(f"#{t + 1} {res[m]}")