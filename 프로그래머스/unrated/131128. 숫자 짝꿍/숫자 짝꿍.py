def solution(X, Y):
    counter_X = {str(i):0 for i in range(10)}
    counter_Y = {str(i):0 for i in range(10)}

    for n in X:
        counter_X[n] += 1
    for n in Y:
        counter_Y[n] += 1
    
    pair = ''
    for i in range(9, -1, -1):
        str_i = str(i)
        pair += str_i * min(counter_X[str_i], counter_Y[str_i])
    
    if not pair:
        return '-1'
    pair = pair.lstrip('0')
    if not pair:
        return '0'
    return pair
