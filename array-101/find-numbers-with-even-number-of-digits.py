def solution(array):
    counter = 0
    array = list(map(str, array))
    for i in array:
        if len(i) % 2 == 0:
            counter += 1
    return counter