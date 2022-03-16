import sys
input = sys.stdin.readline

def solution(n: int, distances: str, stations: str) -> int:
    distances = map(int, distances.split())
    stations = map(int, stations.split())

    answer = next(distances) * (station := next(stations))
    for distance in distances:
        answer += (station := min(station, next(stations))) * distance

    return answer


print(solution(int(input()), input(), input()))
