def solution(array):
    doublesSet = set()
    for i in range(len(array)):
        if array[i] in doublesSet:
            return True
        doublesSet.add(array[i] * 2)
        doublesSet.add(array[i] / 2)
    return False
