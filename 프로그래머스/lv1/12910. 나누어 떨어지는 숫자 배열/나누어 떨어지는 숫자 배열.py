#------------------------------------------------------------------------O
def solution(arr, divisor):
    
    return [v for v in sorted(arr) if v % divisor == 0] or [-1]

#------------------------------------------------------------------------O
# def solution(arr, divisor):

# 오름차순으로 정렬한 배열에서 하나씩 뽑아서 divisor로 나눠 떨어진다면 리스트에 추가
#     ans = [v for v in sorted(arr) if v % divisor == 0]

#     if len(ans) != 0:  # 리스트에 원소가 있다면 리스트를 그대로 출력
#         answer = ans
#     else:              # 리스트에 원소가 없다면 [-1]을 출력
#         answer = [-1]
        
#     return answer