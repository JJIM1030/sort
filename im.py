T = int(input())

for j in range(T):
    N, P = map(int, input().split())

    a = [[0] * N for _ in range(N)]  # N*N 2차원 배열 만들기

    for i in range(N):
        a[i] = list(map(int, input().split()))  # a에 2차원 리스트 값 넣기

    best = 0
    dx = [-1, 1, 0, 0]  # 방향 배열 : 좌우
    dy = [0, 0, -1, 1]  # 방향 배열 : 상하
    for x in range(N):
        for y in range(N):
            total = a[x][y]  # 중심이 되는 값
            for dist in range(1, P+1):  # P 값이 포함돼야 하므로 P+1
                for d in range(4):
                    nx = x + dx[d] * dist
                    ny = y + dy[d] * dist
                    if 0 <= nx < N and 0 <= ny < N:  # 사각형 범위 안에 들어간 값들만 계산
                        total = total + a[nx][ny]  # nx, ny는 P까지 거리 안에 있는 칸들 위치
            if total > best:  # 가장 큰 값들을 선별
                best = total

    print(f"#{j+1} {best}")

