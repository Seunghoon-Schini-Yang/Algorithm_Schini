import sys
input = sys.stdin.readline
import heapq

def solution(n: int) -> str:
    max_heap, min_heap = list(), [int(input())]
    ans = [0] * n
    ans[0] = str(min_heap[0])

    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    max_len, min_len = 0, 1
    for i in range(1, n):
        num = int(input())

        if min_heap[0] < num:
            heapq.heappush(min_heap, num)
            min_len += 1
        else:
            heapq.heappush(max_heap, -num)
            max_len += 1
        
        if max_len < min_len:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            max_len += 1
            min_len -= 1
        elif max_len > min_len + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            max_len -= 1
            min_len += 1

        ans[i] = str(-max_heap[0])
    
    return '\n'.join(ans)

            
print(solution(int(input())))
