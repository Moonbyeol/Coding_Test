n, m, k = map(int, input().split())
seats = []
for _ in range(n):
    seats.append(input())

count = 0

for row in seats:
    consecutive_free = 0
    for seat in row:
        # 빈 좌석('0')의 개수를 세고, '1'이 나오면 리셋
        if seat == '0':
            consecutive_free += 1
        else:
            consecutive_free = 0
        
        if consecutive_free >= k:
            count += 1 

print(count)
