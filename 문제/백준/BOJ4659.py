import sys; input = sys.stdin.readline

def is_acceptable(pw):
    vowels = {'a','e','i','o','u'}
    flag = 0
    
    # case 1
    has_vowel = any(i in vowels for i in pw)
    if not has_vowel:
        return False
    else:
        flag += 1
    
    # case 2
    sequence_vowels = 0
    sequence_consonants = 0
    for i in pw:
        if i in vowels:
            sequence_vowels += 1
            sequence_consonants = 0
        else:
            sequence_vowels = 0
            sequence_consonants += 1
            
    if sequence_vowels == 3 or sequence_consonants == 3:
        return False
    else:
        flag += 1
    
    # case 3
    if len(pw) > 1:
        for i in range(1,len(pw)):
            if pw[i] == pw[i-1] and pw[i] not in {'e','o'}:
                return False
            else:
                flag += 1
    
    if flag >= 3:
        return True
        
while True:
    pw = input().strip()
    if pw == "end":
        break
    
    if is_acceptable(pw):
        print(f"<{pw}> is acceptable")
    else:
        print(f"<{pw}> is not acceptable")