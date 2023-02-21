def solution(cap, n, deliveries, pickups):
    di = pi = n-1
    while 0 <= di and not deliveries[di]:
        di -= 1
    while 0 <= pi and not pickups[pi]:
        pi -= 1
    
    answer = 0
    while 0 <= di or 0 <= pi:
        answer += ( max(di, pi)+1 ) << 1
        dcap = pcap = cap

        while 0 <= di:
            dcap -= deliveries[di]
            if dcap < 0:
                deliveries[di] = -dcap
                break
            deliveries[di] = 0
            di -= 1
        while 0 <= pi:
            pcap -= pickups[pi]
            if pcap < 0:
                pickups[pi] = -pcap
                break
            pickups[pi] = 0
            pi -= 1

    return answer
