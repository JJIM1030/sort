T = int(input())  # 테스트 케이스 개수 받기

for n in range(T):  # 테스트 케이스 받은 만큼 반복
    N = int(input())  # 리스트 개수
    a = list(map(int, input().split()))  # 리스트
    max1 = 0  # 낙차의 최곳값을 찾기 위한 변수
    for i in range(N): # 리스트 개수 만큼 반복(리스트 끝까지 반복)
        drop = 0  # 낙차
        for j in range(i+1, N):  # 첫 시작과 비교하기 위해 i+1에서 시작
            if a[i] > a[j]:
                drop = drop + 1  # 앞 인데스값이 크면 낙차 가능하므로 +1
        if drop > max1:
            max1 = drop  # drop 값이 새로 갱신될 때마다 max 값이 되는지 비교

    print(f"#{n+1} {max1}")