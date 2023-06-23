#--------------------------------------------------------O
def solution(d, budget):
    d.sort()
    cnt = 0
    for v in d:
        budget -= v
        cnt += 1
        
        if budget < 0:
            cnt -= 1
            break
            
    return cnt
#--------------------------------------------------------O
# def solution(d, budget):
#     d.sort()

#     for i in range(len(d)):
#         if budget - d[i] < 0:
#             return i
#         budget -= d[i]
#     return len(d)

#--------------------------------------------------------O
# def solution(d, budget):
#     d.sort()

#     for i in range(len(d)):
#         if budget - d[i] < sum(d[:i]):
#             return i
#     return len(d)

#--------------------------------------------------------X
# def solution(d, budget):
#     d.sort()

#     for i in range(len(d)):
#         if budget - d[i] < sum(d[:i+1]) <= budget:
#             return i+1