# 띄어쓰기를 기준으로 나누기 -> 각각 a와 b로 지정
a, b = map(int, input().strip().split(' '))

# a개수만큼 * 출력 후 줄바꿈 -> b번 반복
print(('*'*a+"\n")*b)