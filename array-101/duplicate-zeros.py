def solution(array):
    i = 0
    while i < len(array):
        if array[i] == 0:
            array.insert(i, 0)
            i += 1
        i += 1
    return array
