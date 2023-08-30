class Goods():
    def __init__(self, N):
        arr = sorted(map(int, input().split()))
        sarr = []
        v, cnt = arr[0], 1
        for i in range(1, N):
            if arr[i] == v:
                cnt += 1
            else:
                sarr.append((v, cnt))
                v, cnt = arr[i], 1
        sarr.append((v, cnt))
        N = len(sarr)
        
        cnt = 0
        for i in range(N):
            l, r = 0, N-1
            while 0 <= l <= r < N:
                if sarr[l][0] + sarr[r][0] < sarr[i][0]:
                    l += 1
                elif sarr[l][0] + sarr[r][0] > sarr[i][0]:
                    r -= 1
                else:
                    if i == l == r:
                        if 2 < sarr[i][1]:
                            cnt += sarr[i][1]
                        break
                    if l == r:
                        if 2 <= sarr[i][1]:
                            cnt += sarr[i][1]
                        break
                    if i == l or i == r:
                        if 2 <= sarr[i][1]:
                            cnt += sarr[i][1]
                            break
                        l += 1; r -= 1
                    else:
                        cnt += sarr[i][1]
                        break
        self.count = cnt


if __name__ == '__main__':
    goods = Goods(int(input()))
    print(goods.count)
