def solution(enroll, referral, seller, amount):
    mapping = {name: i for i, name in enumerate(enroll)}
    seller = [mapping[name] for name in seller]
    referral = [mapping[name] if name != '-' else -1 for name in referral]
    answer = [0] * len(enroll)
    for name, sell in zip(seller, map(lambda x: x*100, amount)):
        while name != -1 and sell:
            sell, r = divmod(sell, 10)      
            answer[name] += sell*9 + r
            name = referral[name]
    return answer