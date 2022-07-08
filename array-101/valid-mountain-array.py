def solution(array):
    size = len(array)
    i = 0
    while i + 1 < size and array[i] < array[i + 1]:
        i += 1
    if i == 0 or i == size - 1:
        return False
    while i + 1 < size and array[i] > array[i + 1]:
        i += 1
    return i == size - 1

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([2, 1]))
print(solution([3, 5, 5]))
print(solution([0, 3, 2, 1]))