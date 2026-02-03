def counting_sort(DATA, TEMP, k):
    # DATA []  -- 입력 배열(원소는 0 이상 k이하)
    # TEMP []  -- 정렬된 배열
    # COUNTS []  -- 카운트 배열

    COUNTS = [0] * (k + 1)

    for i in range(len(DATA)):  # DATA[i] 발생횟수 기록
        COUNTS[DATA[i]] += 1

    for i in range(1, k+1):  # COUNTS 값 조정 (누적)
        COUNTS[i] += COUNTS[i-1]

    for i in range(len(DATA)-1, -1, -1):  # 3단계
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]

    print(TEMP)

data = [12, 3, 9, 1, 15, 7]

counting_sort(data, [0] * (len(data)+1), max(data))