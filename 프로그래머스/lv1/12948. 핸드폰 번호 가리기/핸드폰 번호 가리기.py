import re

def solution(phone_number):
    
    return re.sub(r'\d(?=\d{4})', '*', phone_number)
    # 정규표현식을 이용하여 뒤의 4자리를 제외한 부분 *로 대체하기