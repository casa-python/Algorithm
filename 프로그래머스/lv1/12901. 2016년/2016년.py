def solution(a, b):
    
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    
    add = sum(mon[:a-1]) + b
    num = add % 7

    return day[num]