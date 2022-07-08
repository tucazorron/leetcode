def solution(cpdomains):
    subdomainVisitCount = {}
    for cpdomain in cpdomains:
        count, domain = cpdomain.split(' ')
        count = int(count)
        domains = domain.split('.')
        for i in range(len(domains)):
            if '.'.join(domains[i:]) not in subdomainVisitCount:
                subdomainVisitCount['.'.join(domains[i:])] = 0
            subdomainVisitCount['.'.join(domains[i:])] += count
    return [str(count) + ' ' + domain for domain, count in subdomainVisitCount.items()]
