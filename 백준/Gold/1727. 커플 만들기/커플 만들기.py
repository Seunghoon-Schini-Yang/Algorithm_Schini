import sys
input = sys.stdin.readline

        
def main():
    n, m = map(int, input().split())
    n_arr = list(map(int, input().split()))
    m_arr = list(map(int, input().split()))
    if n < m:
        n, m = m, n
        n_arr, m_arr = m_arr, n_arr
    n_arr.sort()
    m_arr.sort()

    memo = [abs(m_arr[0] - n_arr[i]) for i in range(n-m+1)]
    miny = min(memo)
    for i in range(1, m):
        miny = memo[0]
        tmp = [0] * (n-m+1)
        for j in range(n-m+1):
            miny = min(memo[j], miny)
            tmp[j] = miny + abs(n_arr[i+j] - m_arr[i])
        memo = tmp

    print(min(memo))

    
if __name__ == '__main__':
    main()
