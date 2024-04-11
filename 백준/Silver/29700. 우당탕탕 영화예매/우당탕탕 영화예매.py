n, m, k = map(int, input().split())
seats = []
for _ in range(n):
    seats.append(input())

count = 0

# 각 행에 대해 연속된 k개의 빈 좌석('0')이 몇 번 나오는지 카운트
for row in seats:
    consecutive_free = 0
    for seat in row:
        if seat == '0':
            consecutive_free += 1
        else:
            consecutive_free = 0
        
        if consecutive_free >= k:
            count += 1  # 가능한 시작 위치를 카운트합니다. 사용하는 변수는 'k'입니다.

print(count)