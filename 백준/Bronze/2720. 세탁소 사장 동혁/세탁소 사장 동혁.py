import sys

T = int(sys.stdin.readline())

changes = [25, 10, 5, 1]

for _ in range(T):
    n = int(sys.stdin.readline())
    answers = []

    for i in changes:
        answers.append(n // i)
        n %= i
        
    print(' '.join(map(str, answers)))