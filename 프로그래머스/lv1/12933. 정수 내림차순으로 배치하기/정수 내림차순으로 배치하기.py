#-------------------------------------------------------------O
def solution(n):
    num = [int(a) for a in str(n)]  # 정수를 한자리씩 자르기
    num.sort(reverse=True)          # 큰 수부터 오도록 정렬하기
    m = list(map(str, num))         # 하나의 정수로 합치기

    return int("".join(m))          # 리스트를 정수로 만들기

#-------------------------------------------------------------O
# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))

#-------------------------------------------------------------O
# def solution(n):
#     return int("".join(sorted(list(str(n)), reverse=True)));