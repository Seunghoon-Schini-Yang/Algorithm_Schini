arr = [input() for _ in range(5)]
print(''.join(''.join('' if len(arr[w]) <= i else arr[w][i] for w in range(5)) for i in range(15)))
