def solution(n):
    answer = 0

    for i in range(1, int(n**0.5)+1):  # i의 범위를 (n**0.5)까지로 제한 
        if n % i == 0:
            answer += i
            if i != n // i:  # i가 제곱근이 아닌 경우에만 반대편 약수도 더한다
                answer += n // i
    
    return answer

#------------------------------------------------------------------------O
# i의 범위를 n까지로 설정했으므로 n값이 클 경우엔 성능상의 문제가 있을 수 있다
# def solution(n):
#     answer = 0

#     for i in range(n+1):
#         if i == 0:           # i가 0이면 약수는 없다
#             answer = 0
#         elif n % i == 0:     # i의 약수가 있을 때마다 +1
#             answer += i
    
#     return answer