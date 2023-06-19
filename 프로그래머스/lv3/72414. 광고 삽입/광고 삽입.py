def ttos(x):
    h, m, s = map(int, x.split(':'))
    return h*3600 + m*60 + s


def solution(play, adv, logs):
    play = ttos(play)
    adv = ttos(adv)
    memo = [0] * (play+1)    
    for log in logs:
        s, e = log.split('-')
        memo[ttos(s)] += 1
        memo[ttos(e)] -= 1
    
    for i in range(play):
        memo[i+1] += memo[i]
    
    cur = sum(memo[:adv])
    maxy = (0, cur)
    for i in range(play-adv):
        cur += memo[i+adv] - memo[i]
        if maxy[1] < cur:
            maxy = (i+1, cur)
    
    h, maxy = divmod(maxy[0], 3600)
    m, s = divmod(maxy, 60)
    return ':'.join(map(lambda x: str(x).rjust(2, '0'), (h, m, s)))
