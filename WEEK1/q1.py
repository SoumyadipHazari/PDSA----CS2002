def fun(s):
    p = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] not in s[:i]:
            p += 1
    return p