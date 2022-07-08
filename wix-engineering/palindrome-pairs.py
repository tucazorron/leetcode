def solution(words):
    size = len(words)
    indexMap = {}
    results = []

    for i in range(size):
        indexMap[words[i]] = i

    if '' in indexMap:
        blankIndex = indexMap['']
        for i in range(size):
            if i != blankIndex and isPalindrome(words[i]):
                results.append([i, blankIndex])
                results.append([blankIndex, i])

    for i in range(size):
        for j in range(i+1, size):
            if isPalindrome(words[i] + words[j]):
                results.append([i, j])
            if isPalindrome(words[j] + words[i]):
                results.append([j, i])


    return results

def isPalindrome(word):
    return word == word[::-1]


print(solution(["abcd", "dcba", "lls", "s", "sssll"]))
