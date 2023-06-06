if __name__ == '__main__':
    N, M = map(int, input().split())
    pos = list(map(int, input().split()))
    neg = sorted([i for i in pos if i < 0])
    pos = sorted([i for i in pos if i > 0], reverse=True)
    neg.append(0)
    pos.append(0)
    foot = sum(pos[i] for i in range(0, len(pos), M)) - sum(neg[i] for i in range(0, len(neg), M))
    foot <<= 1
    foot -= pos[0] if -neg[0] <= pos[0] else -neg[0]
    print(foot)
    