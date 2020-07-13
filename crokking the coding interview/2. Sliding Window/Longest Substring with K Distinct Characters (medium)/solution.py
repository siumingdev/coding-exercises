def solve(s, k):    
    longest_substr_len = 0
    char_count = dict()
    
    start = 0

    for end in range(len(s)):
        if s[end] in char_count:
            char_count[s[end]] = char_count[s[end]] + 1
        else:
            char_count[s[end]] = 1

        while len(char_count) > k:
            if char_count[s[start]] <= 1:
                del char_count[s[start]]
            else:
                char_count[s[start]] = char_count[s[start]] - 1
            start += 1
        
        longest_substr_len = max(longest_substr_len, end - start + 1)

    return longest_substr_len


print(solve("araaci", 2))
print(solve("araaci", 1))
print(solve("cbbebi", 3))

            