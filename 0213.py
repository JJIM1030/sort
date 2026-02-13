# 초기 공백 큐 생성 : create_queue()
n = 3
que = [0] * n

# 삽입 : enqueue(item)
rear += 1
que[rear] = 1

while front != rear :  # front == rear : 큐가 비어있는 상태
    front += 1
    tmp = que[front]   # que.append(1)
    print(tmp)



# 삭제 : dequeue()

# 공백 상태 및 포화상태 검사 : is_empty(), is_full()
