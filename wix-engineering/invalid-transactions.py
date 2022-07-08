def solution(transactions):
    transactionsDict = {}
    invalidTransactions = set()
    for i in range(len(transactions)):
        name, time, amount, city = transactions[i].split(',')
        if name not in transactionsDict:
            transactionsDict[name] = {
                'index': [],
                'time': [],
                'amount': [],
                'city': []
            }
        transactionsDict[name]['index'].append(i)
        transactionsDict[name]['time'].append(int(time))
        transactionsDict[name]['amount'].append(int(amount))
        transactionsDict[name]['city'].append(city)
    for name in transactionsDict:
        for i in range(len(transactionsDict[name]['index'])):
            if transactionsDict[name]['amount'][i] > 1000:
                invalidTransactions.add(transactionsDict[name]['index'][i])
            else:
                for j in range(len(transactionsDict[name]['index'])):
                    if abs(transactionsDict[name]['time'][i] - transactionsDict[name]['time'][j]) <= 60:
                        if transactionsDict[name]['city'][i] != transactionsDict[name]['city'][j]:
                            invalidTransactions.add(
                                transactionsDict[name]['index'][i])
                            invalidTransactions.add(
                                transactionsDict[name]['index'][j])
    return [transactions[i] for i in invalidTransactions]
