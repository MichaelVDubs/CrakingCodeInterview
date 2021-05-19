import unittest
# Implement an algorithm to determine if a string has all unique characters
# What if you cannot use additional data structures?
# Start my solution that definitely does not work
#input = 'Ssabcd'

# for letter in input:
#     input = input[1:]
#     print(input)
#     if (letter in input):
#         isUnique = False
#         break

# print(isUnique)


def checkUnique(myStr):
    myArray = []

    for a in myStr:
        if a in myArray:
            print(a)
            print(myArray)
            return False
        myArray.append(a)

    return True
# End My Solution
# Start book solution


def isUniqueChars(myString):
    if len(myString) > 128:
        return False

    boolArray = [False] * 128
    for x in range(len(myString)):
        val = ord(myString[x])
        if (boolArray[val]):
            return False
        boolArray[val] = True
    return True

# End Book Solution


class Test(unittest.TestCase):
    test_cases = [
        ('abcd', True),
        ('nbvgauiewb', False),
        ('1234abcd', True),
        ('', True),
        (''.join([chr(val) for val in range(128)]), True),
        (''.join([chr(val) for val in range(129)]), False),
    ]

    def test_is_unique_chars(self):
        for myString, myBool in self.test_cases:
            assert(isUniqueChars(myString) == myBool)

    def test_check_unique(self):
        for myString, myBool in self.test_cases:
            assert(checkUnique(myString) == myBool)


if __name__ == "__main__":
    unittest.main()
