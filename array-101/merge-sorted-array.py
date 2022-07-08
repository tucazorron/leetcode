def solution(array1, array2):
    array1[len(array2):].clear()
    array1.extend(array2)
    array1.sort()
    return array1
