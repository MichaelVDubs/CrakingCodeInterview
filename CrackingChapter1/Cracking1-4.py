

# Begin my solution before hints
def isPermutationOfPalindrome(myString):
    letters = {}
    length = 0
    flag = False
    for a in myString:
        if a == ' ':
            pass
        else:
            letters[a] = letters.get(a, 0) + 1
            length += 1
    print(letters)
    if(length % 2 == 1):  # if string is odd length
        for key, value in letters.items():
            if value % 2 == 1:
                if flag == True:
                    return False
                flag = True
    else:
        for key, value in letters.items():
            if value % 2 == 1:
                return False
    return(True)

# End my solution before hints


print(isPermutationOfPalindrome("red rum sir is murder"))
