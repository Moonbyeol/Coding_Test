import sys

n = int(sys.stdin.readline())

count = 0
while True:
    if n%5 == 0:
        count += n//5
        print(count)
        break
    
    count +=1
    n -= 3
    if n < 0:
        print(-1)
        break