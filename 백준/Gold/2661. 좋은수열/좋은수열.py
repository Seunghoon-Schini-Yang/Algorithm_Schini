N = int(input())


def main():
    recursive('')


def recursive(seq):
    if len(seq) == N:
        print(seq)
        exit()
    
    for i in ('1', '2', '3'):
        sseq = seq + i
        n = len(sseq)
        for j in range(1, (n>>1)+1):
            if sseq[-j:] == sseq[-(j<<1):(-j)]:
                break
        else:
            recursive(sseq)


if __name__ == '__main__':
    main()
