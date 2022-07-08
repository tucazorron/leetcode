def solution(products, searchWord):
    searches = range(len(searchWord))
    searchResults = [[] for i in searches]
    products.sort()
    for i in searches:
        for p in products:
            if searchWord[0:i+1] == p[0:i+1]:
                if len(searchResults[i]) >= 3:
                    break
                searchResults[i].append(p)
    return searchResults
