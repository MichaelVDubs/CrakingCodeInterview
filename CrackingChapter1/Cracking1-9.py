# Solution before hints
def isRotation(s1, s2):
    size = len(s2)
    for a in range(size):
        if isSubstring(s2[0:size-a-1], s1):
            if isSubstring(s2[size-a:size-1], s1):
                return True

    return False
# End solution before hints

# Solution after hints


def isRotationAfterHints(s1, s2):
    s2 = s2 + s2
    if isSubstring(s2, s1):
        return True
    return False


def isSubstring(s1, s2):
    return True


print(isRotation('test', 'estt'))
