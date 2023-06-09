def solution(a, b):
    answer = 0
    
    if a <= b:
        n1 = a
        n2 = b
        
        for i in range(n1, n2+1):
            answer += i
        
    else:
        n1 = b
        n2 = a
        
        for i in range(n1, n2+1):
            answer += i
        
    return answer