data = [0, 4, 1, 3, 1, 1, 2, 4, 1]

counts = [0] * (max(data) + 1)
counts2 = 0
counts3 = [0] * (max(data) + 1)
temp = [0] * (len(data)+1)

for i in range(len(data)):  # 각 원소별 개수 구하기
    counts[data[i]] += 1

for j in range(len(counts)):
    print(f"{j} : {counts[j]}개", end= "  ")

print()

for l in counts:  # 누적합 구하기
    counts2 = counts2 + l
    print(f"누적 합 : {counts2}", end= "  ")

print()

for m in range(len(data)-1, -1, -1):  # 각 원소를 오름차순으로 배치하기
    counts3[data[m]] -= 1
    temp[counts3[data[m]]] = data[m]
# 뒤부터 읽는 이유 : 각 원소별로 저장된 개수는 마지막을 기준으로 저장되었기 때문

print(temp)