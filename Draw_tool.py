N = int(input())
T = int(input())

a = [[0] * N for _ in range(N)]

for t in range(T):
    col = list(map(int, input().split())) # 3 1 1 4 4
    for i in range(col[1], col[3] + 1):
        for j in range(col[2], col[4]+1):
            if a[i][j] > col[0]:
                continue
            a[i][j] = col[0]

s = []
for i in range(N):
    for j in range(N):
        if a[i][j] == 0 :
            continue
        for k in range(N):
            if i + k >= N or j + k >= N:
                break
            flag = 1
            for x in range(i, i + k):
                for y in range(j, j + k):
                    if a[i][j] != a[x][y]:
                        flag = 0
            if flag == 1:
                s.append(k * k)

print(max(s))