#--------------------------------------------------------------O
# numpy를 이용한 함수
import numpy as np

def solution(arr1, arr2):
    a1 = np.array(arr1)
    a2 = np.array(arr2)
    ans = a1 + a2
    return ans.tolist()  
# .tolist(): 배열을 리스트로 바꿔줌. 
# 예시: array([[4], [6]]) -> [[4],[6]]

#--------------------------------------------------------------O
# def solution(arr1, arr2):
#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
#     return answer

# zip을 두 번 쓰면 원소 추출 가능. 같은 자리 원소끼리 더하면 행렬 덧셈 가능.

#--------------------------------------------------------------X
# def solution(arr1, arr2):
#     answer = [[sum(num)] for num in zip(arr1, arr2)]
#     return answer

# zip을 쓰면 [([1, 2], [3, 4]), ([2, 3], [5, 6])]으로 묶여서 sum하기 어렵다.