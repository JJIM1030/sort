T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split()) # N : 샘플 길이  K : password 길이
    sam = list(map(int, input().split()))
    pas = list(map(int, input().split()))
    a = 0

    for s in sam:
        if a < K and s == pas[a]:
            a += 1
            if a == K:
                break

    if a == K: result = 1
    else: result = 0

    print(f"#{t} {result}")
