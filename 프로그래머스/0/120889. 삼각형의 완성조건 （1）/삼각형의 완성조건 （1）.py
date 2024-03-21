def solution(sides):
    if sum(sides)/2 >max(sides):
        answer = 1
    else:
        answer = 2
    return answer