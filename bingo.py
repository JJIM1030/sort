
a1 = [(list(map(int, input().split()))) for _ in range(5)]
a2 = [(list(map(int, input().split()))) for _ in range(5)]
a2 = sum(a2, [])
ax = [0] * 5
ay = [0] * 5
d1, d2, cnt = 0, 0, 0

for i in a2:
    for j in range(5):
        for l in range(5):
            if a1[j][l] == i:
                ax[j] += 1
                ay[l] += 1

                if ax[j] == 5:
                    cnt += 1

                if ay[l] == 5:
                    cnt += 1

                if j == l:  # 우하향 대각선
                    d1 += 1
                    if d1 == 5:
                        cnt += 1

                if j + l == 4: # 좌하향 대각선
                    d2 += 1
                    if d2 == 5:
                        cnt += 1

            if cnt >= 3:
                print(i)
                exit()