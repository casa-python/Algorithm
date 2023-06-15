#----------------------------------------O
# 자연수를 한 자리씩 분리해서 합하는 함수
# 컴프리헨션 구문 이용
def solution(n):
    
    return sum([int(i) for i in str(n)])

#----------------------------------------O
# map함수 이용
# def solution(n):

#     return sum(map(int, str(n)))