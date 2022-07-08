def solution(array):
    i = 0
    counter = 0
    while i < len(array):
        if array[i] == 0:
            array.pop(i)
            counter += 1
        else:
            i += 1
    array.extend([0] * counter)
    return array
