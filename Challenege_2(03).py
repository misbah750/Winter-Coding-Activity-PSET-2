def find_longest_mirror_length(s: str) -> int:
    def helper(i, j):
        # Base cases
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return 2 + helper(i + 1, j - 1)
        return max(helper(i + 1, j), helper(i, j - 1))
    return helper(0, len(s) - 1)

# Test cases
print("Test 1  Simple palindromes:")
print(find_longest_mirror_length("aba"))  
print(find_longest_mirror_length("racecar"))  

print("\nTest 2  Even length palindromes:")
print(find_longest_mirror_length("abba"))  
print(find_longest_mirror_length("noon"))  

print("\nTest 3  Single character:")
print(find_longest_mirror_length("a"))  
print(find_longest_mirror_length("z"))  

print("\nTest 4  Two characters:")
print(find_longest_mirror_length("aa"))