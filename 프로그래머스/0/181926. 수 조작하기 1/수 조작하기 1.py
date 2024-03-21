def solution(n, control):
    answer = 0
    wasd = []
    for i in control:
        wasd.append(i)
    n += (wasd.count('w')-wasd.count('s'))+(wasd.count('d')-wasd.count('a'))*10
    return n