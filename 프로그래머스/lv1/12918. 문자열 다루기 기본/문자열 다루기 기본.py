#--------------------------------------------------------------------O
def solution(s):
    
    try:
        return (int(s) % 1 == 0) and (len(s) == 4 or len(s) == 6)
        # 문자열 s가 정수이면서 길이가 4 혹은 6 이면 True를 출력

    except ValueError:
        return False
        # 에러가 난다면 False 출력
    
#-------------------------------------------------------------------X
        # return (int(s) % 1 == 0) and (len(s) == 4 or 6)
        # #len(s) == 4 or 6 에서 오류 발생
    
#--------------------------------------------------------------------O
# def solution(s):
        
#     return s.isdigit() and len(s) in [4,6]
#                            # len(s) in [4, 6] 이런 방법도 있음!!!