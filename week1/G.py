a = input()

def balanced_string(string):
    s = []
    s.append(string[0])
    for i in range(1, len(string)):
        if s and string[i] == s[-1]:
            s.pop()
        else:
            s.append(string[i])
    if not s:
        return True
    return False

print("YES" if balanced_string(a) else "NO")