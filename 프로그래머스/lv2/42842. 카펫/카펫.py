def solution(brown, yellow):
    brown = brown//2 - 2
    x = (brown + int(pow(pow(brown, 2) - 4*yellow, 0.5))) // 2
    return sorted([x+2, yellow//x+2], reverse=True)