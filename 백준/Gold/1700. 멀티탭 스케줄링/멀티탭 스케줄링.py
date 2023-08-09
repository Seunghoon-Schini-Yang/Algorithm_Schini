class Extension():
    def __init__(self, N, K):
        if K <= N:
            self.answer = 0
        else:
            waitings = list(map(int, input().split()))
            in_use = set() # [False] * (K+1)
            idx_info = [[] for _ in range(K+1)]
            cnt = 0
            for i in range(K-1, -1, -1):
                idx_info[waitings[i]].append(i)
            for i in range(K):
                idx_info[waitings[i]].pop()
                if waitings[i] in in_use:
                    continue
                if len(in_use) == N:
                    farthest = (0, 0)
                    for product in in_use:
                        if not idx_info[product]:
                            farthest = (product, K)
                            break
                        if farthest[1] < idx_info[product][-1]:
                            farthest = (product, idx_info[product][-1])
                    if farthest[0] == 0:
                        in_use.pop()
                    else:
                        in_use.remove(farthest[0])
                    cnt += 1
                in_use.add(waitings[i])
            self.answer = cnt


if __name__ == '__main__':
    extension = Extension(*map(int, input().split()))
    print(extension.answer)
