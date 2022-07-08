def solution(emails):
    uniqueEmails = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.replace('.', '').split('+')[0]
        uniqueEmails.add(local + '@' + domain)
    return len(uniqueEmails)
