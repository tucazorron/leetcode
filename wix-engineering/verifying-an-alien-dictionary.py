def solution(words, order):
    for i in range(len(words) - 1):
        first, second = words[i], words[i + 1]
        j = 0
        while j < len(first) and j < len(second):
            if order.index(first[j]) > order.index(second[j]):
                return False
            elif order.index(first[j]) < order.index(second[j]):
                break
            j += 1
        if (j >= len(first) or j >= len(second)) and len(first) > len(second):
            return False
    return True
