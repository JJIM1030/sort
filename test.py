T = int(input())

for t in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    n = []
    for i in range(N):
        for j in range(N):
            if a[i][j] == 2:  # 경비원 위치
                x, y = i, j
                break

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0

    for d in range(4):
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not(0 <= nx < N and 0 <= ny < N):
                break
            if a[nx][ny] == 1:
                break
            if a[nx][ny] == 0:
                a[nx][ny] = 3 # 감시된 칸 처리

    for i in range(N):
        for j in range(N):
            if a[i][j]==0:
                cnt += 1

    print(f"#{t} {cnt}")


