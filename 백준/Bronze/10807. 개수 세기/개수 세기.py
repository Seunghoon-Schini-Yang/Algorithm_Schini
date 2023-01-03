N = int(input())
arr = map(int, input().split())
v = int(input())
print(sum(1 if x==v else 0 for x in arr))