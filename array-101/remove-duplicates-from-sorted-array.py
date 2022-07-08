def solution(array):
    i = 0
    while i < len(array) -1:
        if array[i] == array[i+1]:
            array.pop(i)
        else:
            i += 1
    return array