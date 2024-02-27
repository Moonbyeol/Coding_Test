def solution(arr):
    a=arr[0]
    answer = []
    answer.append(a)
    for i in arr:
        if i != a:
            answer.append(i)
            a = i
    return answer