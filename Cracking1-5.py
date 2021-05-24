def isOneAway(string1, string2):
    if (string1 == string2):
        return True

    str1Length = len(string1)
    str2Length = len(string2)
    flag = False

    if (str1Length < str2Length):  # check if remove
        return removeCheck(string2, string1)
    elif(str2Length < str1Length):
        return removeCheck(string1, string2)
    else:
        for x, y in zip(string1, string2):
            if x != y:
                if flag:
                    return False
                flag = True
        return True

    return False


def removeCheck(longString, shortString):
    offset = 0
    if len(longString) - len(shortString) > 1:
        return False
    for x in range(len(shortString)):
        if shortString[x] != longString[x + offset]:
            if offset == 0:
                offset = 1
            else:
                return False
    return True


print(isOneAway('pale', 'pada'))
