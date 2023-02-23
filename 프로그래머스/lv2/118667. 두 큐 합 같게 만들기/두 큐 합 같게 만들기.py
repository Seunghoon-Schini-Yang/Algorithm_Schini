def solution(queue1, queue2):
    answer = 0
    circle_arr = queue1 + queue2
    optimal = sum(circle_arr)
    if optimal % 2:
        return -1
    optimal = optimal // 2
    a, b = 0, len(queue1)
    A = sum(circle_arr[a:b])
    
    # 두 큐의 합이 같을 때 까지 함
    while A != optimal:
        fail = True
        # a를 시계방향으로 이동
        while A > optimal and a <= b:
            A -= circle_arr[a]
            a += 1
            answer += 1
            fail = False
        # b를 시계방향으로 이동
        while A < optimal and b < len(circle_arr):
            A += circle_arr[b]
            b += 1      
            answer += 1
            fail = False   
        # 답이 없음 
        if len(circle_arr) <= a or fail:
            return -1
           
    return answer


print(solution([1, 3, 3, 1], [1, 1, 1, 1]))
