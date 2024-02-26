def solution(nums):
    n = len(nums)/2
    if n <= len(set(nums)):
        answer = n
    else:
        answer = len(set(nums))
    return answer