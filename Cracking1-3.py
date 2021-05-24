# Write a method to replace all spaces in a string with '%20'.

# Begin my solution before hints
def replaceSpaces(myString):
    wordString = ''
    tempString = ''
    for char in myString:
        if char == ' ':
            wordString += tempString + '%20'
            tempString = ''
        else:
            tempString += char
    wordString += tempString
    return(wordString)

# End my solution before hints


print(replaceSpaces("hi my name is jeff"))
