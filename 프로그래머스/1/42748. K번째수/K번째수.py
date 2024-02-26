def solution(array, commands):
    answer=[]
    for command in commands:
        i, j, k = command
        sort_cmd = sorted(array[i-1:j])
        answer.append(sort_cmd[k-1])
    return answer