def solution(array, value):
    i = 0
    while i < len(array):
        if array[i] == value:
            array.pop(i)
        else:
            i += 1
    return array
