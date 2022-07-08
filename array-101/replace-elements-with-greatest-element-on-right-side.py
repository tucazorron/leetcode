def solution(array):
    for i in range(len(array) - 1):
        array[i] = max(array[i+1: len(array)])
    array[-1] = -1
    return array
