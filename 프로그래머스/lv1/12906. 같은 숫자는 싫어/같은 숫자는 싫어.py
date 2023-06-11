def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:    # 연속된 값이면 통과(제거)
            continue
        else:                       # 앞과 다른 값이면 추가
            answer.append(arr[i])
    return answer