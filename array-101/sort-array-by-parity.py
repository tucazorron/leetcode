def solution(array):
    i = 0
    odds = []
    while i < len(array):
        if array[i] % 2 == 1:
            odds.append(array[i])
            array.pop(i)
        else:
            i += 1
    array.extend(odds)
    return array
