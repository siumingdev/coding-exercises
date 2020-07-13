# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def solve(s: str) -> int:
    start = 0
    char_set = set()
    max_len = 0
    
    for end in range(len(s)):
        rc = s[end]
        while rc in char_set:
            lc = s[start]
            char_set.remove(lc)
            start += 1
        char_set.add(rc)
        max_len = max(max_len, end - start + 1)
        
    return max_len


print(solve("aabccbb"))
print(solve("abbbb"))
print(solve("abccde"))