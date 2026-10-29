# Understand: 
# -input: two strings
# -output:true or false
# - edge case: if you input something that isnt string
#
# Plan:
# 1. create and array of 26 positions to count the letters through a and z
# 2. Go through the magazine and count how many times each letter appears
# 3. Go through the ransomnote and subtract one for each letter needed
# 4. if any count becames negative, return false because that wouldnt fit enough letters
# 5. otherwise, return true 
# 
# Implement:
# (below)
# 


def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
    count = {}
        
    for char in magazine:
        count[char] = count.get(char, 0) + 1

    for char in ransomNote:
        if count.get(char, 0) == 0:
            return False 
        
        count[char] -= 1 
    return True 

# Basic failures
assert canConstruct("a", "b") == False
assert canConstruct("aa", "ab") == False

# Basic success
assert canConstruct("aa", "aab") == True

# Empty ransomNote
assert canConstruct("", "abc") == True

# Empty magazine
assert canConstruct("a", "") == False

# Exact match
assert canConstruct("abc", "abc") == True

# Magazine has extras
assert canConstruct("abc", "aabbcc") == True

# Multiple same letters
assert canConstruct("aaa", "aaaa") == True
assert canConstruct("aaaa", "aaa") == False

# Different letters entirely
assert canConstruct("abc", "def") == False

# Longer ransom note
assert canConstruct("abcdef", "abc") == False