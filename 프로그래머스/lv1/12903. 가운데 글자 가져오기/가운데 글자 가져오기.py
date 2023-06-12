def solution(s):
    
    if len(s) % 2 == 0:                          # 문자열의 길이가 짝수인 경우
        answer = s[len(s)//2 - 1:len(s)//2 + 1]  # 가운데 두 문자를 슬라이싱하여 저장
    else:                                        # 문자열의 길이가 홀수인 경우
        answer = s[len(s)//2]                    # 가운데 문자를 저장
        
    return answer  