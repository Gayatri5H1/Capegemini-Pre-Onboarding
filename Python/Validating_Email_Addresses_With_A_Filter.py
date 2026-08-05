def fun(s):
    try:
        un, rest = s.split('@')
        web, ext = rest.split('.')
    except ValueError:
        return False
    if not un or not web or len(ext) > 3 or len(ext) == 0:
        return False
    if not all(c.isalnum() or c in "-_" for c in un):
        return False
    if not web.isalnum():
        return False
    if not ext.isalpha():
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
