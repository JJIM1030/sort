T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    cnt = 0

    for b in B:
        start = 0
        end = N - 1

        prev_dir = 0  # 0: 없음, -1: 왼쪽, 1: 오른쪽
        ok = True
        found = False

        while start <= end:
            middle = (start + end) // 2

            if A[middle] == b:
                found = True
                break

            elif A[middle] > b:          # 왼쪽 구간 선택
                if prev_dir == -1:
                    ok = False
                    break
                prev_dir = -1
                end = middle - 1

            else:                         # 오른쪽 구간 선택
                if prev_dir == 1:
                    ok = False
                    break
                prev_dir = 1
                start = middle + 1

        if found and ok:
            cnt += 1

    print(f"#{t} {cnt}")