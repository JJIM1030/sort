
a1 = [(list(map(int, input().split()))) for _ in range(5)]
a2 = [(list(map(int, input().split()))) for _ in range(5)]
a2 = a2[0] + a2[1] + a2[2] + a2[3] + a2[4]
ax = [[0] * 6]
ay = [[0] * 6]
cnt = 0
# for i in a2:
#     for j in i:
#         a3.append(j)

for i in a2:
    for j in range(len(a1)):
        for l in range(len(a1)):
            if a1[j][l] == i:
                ax[j] += 1
                ay[l] += 1
                if ax[j] == 5:
                    cnt += 1
                elif ay[l] == 5:
                    cnt += 1
            if cnt == 3:
                print(a1[j][l])


