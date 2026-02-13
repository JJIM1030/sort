# s = input()
#
# if s == s[::-1]:
#     print(1)
# else: print(0)

# t = "BBQBHCKFCMC"
#
# for i in range(len(t)-2):
#     if t[i] == 'K' and t[i+1] == "F" and t[i+2] == "C":
#         print(i)

# T = 'helloworld[92084]answer'
#
# for i in range((T.find("[")) + 1, T.find("]")):
#     print(T[i], end="")

# arr = ['ABCQ', 'B[4]R', 'CCDA', 'BT[15]']
#
# def get_find(text):
#     for i in text:
#         if i.find("[") != -1:
#             print(i[i.find("[")+1 : i.find("]")], end=" ")
#
# get_find(arr)

# T = "B[45]AB[9994]"
# sum_v = 0
# i = 0
#
# while i < len(T):
#     if T[i] == "[":
#         j = i + 1
#         num = ""
#         while T[j] != "]":
#             num += T[j]
#             j +=1
#         sum_v += int(num)
#         i = j
#     i += 1
# print(sum_v)

# T = "ABCDEFABCKKKKKABC"
#
# cnt = 0
# idx = 0
#
# while True:
#     idx = T.find("ABC", idx)
#     if idx == -1:
#         break
#     cnt += 1
#     idx += 1   # 다음 위치부터 다시 탐색
#
# print(cnt)


# T = ['GOLDABCGOLD', 'HELLOWORLD', 'WHITEGOLD']
# cnt = 0
# j = 0
#
# while j < len(T):
#     i = 0
#     while True:
#         i = T[j].find("GOLD", i)
#         if i == -1:
#             break
#         cnt += 1
#         i += 1
#     j += 1
#
# print(cnt)

# T = input()
# sum_v, i = 0, 0
#
# while i < len(T):
#     if T[i] == "[":
#         j = i + 1
#         num = ""
#         while T[j] != "]":
#             num += T[j]
#             j += 1
#         sum_v += int(num)
#         i = j
#     if T[i] == "{":
#         j = i + 1
#         num = ""
#         while T[j] != "}":
#             num += T[j]
#             j += 1
#         sum_v *= int(num)
#         i = j
#     i += 1
#
# print(sum_v)

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = 0

    if N == M:
        for a in arr:
            if a == a[::-1]:
                result = a

        for i in range(N):
            arr1 = ""
            for j in range(N):
                arr1 += arr[j][i]

            if arr1 == arr1[::-1]:
                result = arr1

    else:
        for i in range(N):
            for j in range(N - M + 1):
                if arr[i][j:j + M] == arr[i][j:j + M][::-1]:
                    result = arr[i][j:j + M]

        for i in range(N):  # 열
            for j in range(N - M + 1):  # 시작 행
                s = ''.join(arr[j + k][i] for k in range(M))
                if s == s[::-1]:
                    result = s

    print(f"#{t} {result}")