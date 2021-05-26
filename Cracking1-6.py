def countString(myString):
    if not isShorter(myString):
        return myString
    count = 0
    currentChar = myString[0]
    countStr = ''
    for a in myString:
        if a == currentChar:
            count += 1
        else:
            countStr += currentChar + str(count)
            currentChar = a
            count = 1
    countStr += currentChar + str(count)
    return countStr


def isShorter(myString):
    count = 1
    currentChar = myString[0]
    for a in myString:
        if a == currentChar:
            continue
        else:
            currentChar = a
            count += 1
    print(count)
    if count * 2 < len(myString):
        return True
    return False


print(countString('aabcccccaaa'))
