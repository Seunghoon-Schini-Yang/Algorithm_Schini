import sys
input = sys.stdin.readline
print = sys.stdout.write


def solution(n: int) -> None:
    nums = [0] + list(map(int, input().split()))
    dp = [[i>>1 if i&1 else (i>>1)-1, 0] for i in range(n*2+1)]
    dp[0][1] = dp[-1][1] = 1
    
    m = int(input())
    for _ in range(m):
        s, e = map(int, input().split())
        if s > dp[s+e][0]:
            print('1\n')
            continue
        if dp[s+e][1]:
            print('0\n')
            continue
            
        else:
            c_s = dp[s+e][0]
            c_e = s + e - c_s
            flag = 1
            while c_s >= s:
                if nums[c_s] == nums[c_e]:
                    c_s -= 1
                    c_e += 1
                    dp[s+e][0] = c_s
                    if c_s==0 or c_e>n:
                        break
                else:
                    dp[s+e][1] = 1
                    flag = 0
                    print('0\n')
                    break
            if flag:
                print('1\n')


solution(int(input()))
