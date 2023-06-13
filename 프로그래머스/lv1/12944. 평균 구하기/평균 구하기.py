#-----------------------------------------------------O
import numpy

def solution(arr):
    return numpy.mean(arr)
    
#-----------------------------------------------------X
# def solution(arr):
#     answer = 0
#     answer = [(answer += arr.pop(0))/len(arr) for i in range(len(arr))]
#     
#     return answer

# comprefension 안에서는 += 연산을 할 수 없다. 대입을 하는 건 못한다.
# len(arr)도 틀림. 이미 리스트는 비어서 길이가 0이므로 나눌 수 없다.

#-----------------------------------------------------O
# def solution(arr):
    
#     ans = 0
#     l = len(arr)
    
#     for i in range(len(arr)):  # 리스트 안의 원소들 더하기
#         ans += arr.pop(0)
        
#     return ans/l

#-----------------------------------------------------O
# def solution(arr):
    
#     return sum(arr)/len(arr)