N, M = map(int, input().split())  # N: 행(세로), M: 열(가로)
K = int(input())
a = [list(input().rstrip()) for _ in range(N)]

bombs = []
for y in range(N):
    for x in range(M):
        if a[y][x] == "@":
            bombs.append((y, x))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for by, bx in bombs:
    a[by][bx] = "%"  # 폭탄 위치도 폭발 처리
    for d in range(4):
        for dist in range(1, K + 1):
            ny = by + dy[d] * dist
            nx = bx + dx[d] * dist

            # 범위 밖이면 그 방향 종료
            if not (0 <= ny < N and 0 <= nx < M):
                break
            # 벽 만나면 그 방향 종료
            if a[ny][nx] == "#":
                break

            a[ny][nx] = "%"

for row in a:
    print("".join(row))
