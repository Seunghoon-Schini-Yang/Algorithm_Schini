if __name__ == '__main__':
    print(*[a-b for a,b in zip([1,1,2,2,2,8], map(int, input().split()))])
