def kmp_matcher(t, p):
    n = len(t)
    m = len(p)
    pi = compute_prefix_function(p)
    q = 0
    match_found = False  
    for i in range(n):
        while q > 0 and p[q] != t[i]:
            q = pi[q - 1]
        if p[q] == t[i]:
            q = q + 1
        if q == m:
            print("Found pattern at index " + str(i - m + 1))
            q = pi[q - 1]
            match_found = True  

    if not match_found:
        print("Pattern not found in the text.")

def compute_prefix_function(p):
    m = len(p)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = pi[k - 1]
        if p[k] == p[q]:
            k = k + 1
        pi[q] = k
    return pi

t = 'quickbrownfoxjumpedoverthelazydog'
p = 'fox'
q = 'check'
kmp_matcher(t, p)
kmp_matcher(t, q)
