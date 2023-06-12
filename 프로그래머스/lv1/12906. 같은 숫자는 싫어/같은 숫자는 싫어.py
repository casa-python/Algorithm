def solution(arr):
    answer = []                     # 결과를 저장할 빈 리스트 생성
    answer.append(arr[0])           # 첫 번째 요소를 결과 리스트에 추가

    # 두 번째 요소부터 마지막 요소까지 반복문을 수행
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:    # 현재 요소와 이전 요소가 같은지 비교
            continue                # 같으면 건너뛰고 다음 요소로 진행
        else:
            answer.append(arr[i])   # 이전 요소와 다른 경우 결과 리스트에 추가
    
    return answer                   # 결과 리스트 반환
