def solution(operations):
    pq = list()
    
    for query in operations:
        if query[0] == "I":
            pq.append(int(query[2:]))
        elif not pq:
            continue
        elif query[2] == '-':
            pq.remove(min(pq))
        else:
            pq.remove(max(pq))
            
    return [max(pq), min(pq)] if pq else [0, 0]