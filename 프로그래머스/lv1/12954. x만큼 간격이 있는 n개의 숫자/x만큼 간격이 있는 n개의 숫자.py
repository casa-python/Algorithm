def solution(x, n):
    
    return [x*(i+1) for i in range(n)]

#--------------------------------------------------------------------O
# x=0일 때도 값을 구하기 위해 x가 0일 때와 아닐 때로 나누었다.

# def solution(x, n):
    
#     if x == 0:
#         answer = [0 for i in range(n)]
        
#     else:
#         y = x
#         answer = [v for v in range(y, (n+1)*y, y)]
        
#     return answer

#---------------------------------------------------------------------X
# range함수의 증감값 부분에는 0이 올 수 없다.
# 따라서 컴프리헨션 구문 안에 if x != 0 else "None"을 추가했지만
# 위의 경우 x=0일 때는 값을 구할 수 없는 함수다.

# def solution(x, n):
    
#     return [v if x != 0 else "None" for v in range(x, (n+1)*x, x)]