#--------------------------------------------------------O
def solution(n):
    return [int(i) for i in reversed(list(str(n)))]

#--------------------------------------------------------
# list.reverse() : none값
# reversed(list) : list

#--------------------------------------------------------O
# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))

#--------------------------------------------------------O
# def digit_reverse(n):
#     return list(map(int, list(str(n))[::-1]))

