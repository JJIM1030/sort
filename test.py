# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print("#", end="")
#     print()


# a = ["A", "B", "Q", "T"]
#
# for i in range(len(a)):
#     for j in range(len(a)-1, -1, -1):
#         print(a[j], end="")
#     print()


# a = [[0] * 4 for _ in range(4)]
# t = 0
#
# for x in a:
#     for y in x:
#         y = t
#         print(y, end="")
#     t += 1
#     print()


# for i in range(1, 4):
#     for j in range(1, 5):
#         print(i, j)


# a = list(map(int, input().split()))
# cnt = 0
#
# for i in a:
#     if i ==7:
#         cnt += 1
#
# print(cnt)


# a = [[0] * 4 for _ in range(4)]
# count = 0
#
# a[0][0] = 7
# a[1][3] = 1
# a[2][1] = 3
# a[3][3] = 9
#
# for i in range(len(a)):
#     print(a[3][i], end= " ")


# a = [
#     [7, 1, 3, 5],
#     [9, 5, 9, 1],
#     [1, 3, 1, 5],
#     [3, 5, 9, 9],
# ]
#
# for i in a:
#     for j in range(len(i)):
#         if j == 2:
#             print(i[j], end= " ")


# a = [
#     [5, 4, 2, 1],
#     [3, 7, 7, 7],
#     [2, 2, 1, 1],
# ]
#
# for j in range(len(a) + 1):
#     for l in range(len(a)):
#         print(a[l][j], end=" ")
#     print()


# a = []
#
# for _ in range(4):
#     a.append(list(map(int, input().split())))
#
# for i in range(len(a)-1, -1, -1):
#     for j in range(len(a)-1, -1, -1):
#         print(a[i][j], end= " ")
#     print()


# a = []
# cnt = 0
#
# for _ in range(5):
#     a.append(list(map(int, input().split())))
#
# max_v, min_v = a[0][0], a[0][0]
# sum_v = 0
#
# for i in a:
#     for j in i:
#         if j == 2:
#             cnt += 1
#         if j > max_v:
#             max_v = j
#         if j < min_v:
#             min_v = j
#
# for i in range(len(a)):
#     for j in range(len(a)):
#         if j == i:
#             sum_v += a[i][j]
#
# print(cnt)
# print(max_v, min_v)
# print(sum_v)



a = list(map(int, input().split()))

def is_baby_gin(a):
    arr = sorted(a)
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2] and arr[3] == arr[4] == arr[5]:
        return True
    if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5] and arr[0] == arr[1] == arr[2]:
        return True
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2] and arr[3] + 1 == arr[4] and arr[4] == arr[5]:
        return True
    if arr[0] == arr[1] == arr[2] and arr[3] == arr[4] == arr[5]:
        return True
    else:
        return False

if is_baby_gin(a) == True:
    print("Yes")
else: print("No")


