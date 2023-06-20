#-----------------------------------------------------------------O
def solution(array, commands):
    
    return [sorted(array[a[0]-1:a[1]])[a[2]-1] for a in commands]

#-----------------------------------------------------------------O
# for a in commands:
#     arr = array[a[0]-1:a[1]]  # slicing
#     arr.sort()                # sort
#     print(arr[a[2]-1])