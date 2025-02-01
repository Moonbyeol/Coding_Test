def solution(a, b):
    if 2*a*b >= int(str(a)+str(b)):
        return 2*a*b
    else:
        return int(str(a)+str(b))