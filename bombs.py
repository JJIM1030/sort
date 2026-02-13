N, M = map(int, input().split()) # 세로(N), 가로 (M)
K = int(input())  # 화력 K
a = [list(input()) for _ in range(N)]

bombs = []
for i in range(N):
    for j in range(M):
        if a[i][j] == "@":  # 폭탄 설치된 곳 : @
            bombs.append((i, j))  # 폭발된 곳 : %

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for y, x in bombs:
        a[y][x] = "%"
        for dist in range(1, K+1):
            for l in range(4):
                nx = x + dx[l] * dist
                ny = y + dy[l] * dist
                if 0 <= nx < M and 0 <= ny < N:
                    if a[ny][nx] == "#":  # 벽 : #
                        break
                    else: a[ny][nx] = "%"

for i in a:
    print("".join(i))

