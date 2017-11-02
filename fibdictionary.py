def fibdict(n, d):
    if n in d:
        return d[n]
    else:
        result = fibdict(n-1, d) + fibdict(n-2, d)
        d[n] = result
        return result
d = {1:1, 2:2}
print(fibdict(5, d))
