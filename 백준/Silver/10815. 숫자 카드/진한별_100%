n = int(input())
a = set(map(int, input().split())) # list 로하면 시간초과
m = int(input())
b = list(map(int, input().split()))

result = []
for i in range(m):
    if b[i] in a:  # b[i]가 a 집합에 있는지 확인
        result.append(1)  # 있으면 결과 리스트에 1 추가
    else:
        result.append(0)  # 없으면 결과 리스트에 0 추가

# 결과 출력
print(' '.join(map(str, result)))
