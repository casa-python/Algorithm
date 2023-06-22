def solution(n):
    
    def is_prime(n):
        """
        n이 소수면 True, 소수가 아니면 False를 반환하는 함수
        """
        for i in range(2, int(n**(1/2)+1)):
            if n % i == 0:
                return False
        return True
    
    ans=[]
    for num in range(2, n+1):
        # 주어진 범위 안에서 소수인 숫자들을 리스트에 추가
        if is_prime(num):
            ans.append(num)
            
    return len(ans)

# 소수인지 판별하기위해 수를 나눌 때 앞에서 구한 소수들을 활용할 수 있을까?
# 그런게 재귀함수인가?