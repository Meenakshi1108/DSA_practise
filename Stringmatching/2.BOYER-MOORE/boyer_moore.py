def bm_match(T, P):
    n = len(T)  # length of text
    m = len(P)  # length of pattern

    #Compute the last occurrence function
    last = {}  
    for i in range(m - 1):
        last[P[i]] = i

    i = 0  # Index in the text
    while i <= n - m:
        j = m - 1  # Index in the pattern

        while j >= 0 and P[j] == T[i + j]:
            j -= 1

        if j < 0:
            return i  # Match found at index i

        # Mismatch
        if T[i + j] in last:
            i += max(1, j - last[T[i + j]])
        else:
            i += j + 1

    return -1  # No match found

text = 'quickbrownfoxjumpedoverthelazydog'
pattern = 'fox'
result = bm_match(text, pattern)
print("Pattern found at index:", result)
