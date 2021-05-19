# Given two strings, write a method to decide if one is a permutation of the other
import unittest
from unittest import result

# Begin my solution before hints


def isPermutation(str1, str2):
    myDict1 = {}
    myDict2 = {}

    if (len(str1) != len(str2)):
        return False
    for (a, b) in zip(str1, str2):
        myDict1[a] = myDict1.get(a, 0) + 1
        myDict2[b] = myDict2.get(b, 0) + 1

    if myDict2 == myDict1:
        return True

    return False

# End my solution before hints

# Begin my solution with hints


def isPermutationHints(str1, str2):
    if (len(str1) != len(str2)):
        return False
    if (sorted(str1) == sorted(str2)):
        return True
    return False

# End my solution with hints


class Test(unittest.TestCase):
    test_cases = [
        ("bads", 'dabs', True),
        ("abddfjiis", "abddfjiiq", False),
        ("abcd", "abc", False)
    ]

    def test_is_permutation(self):
        for str1, str2, result in self.test_cases:
            assert(isPermutation(str1, str2) == result)

    def test_is_permutation_hints(self):
        for str1, str2, result in self.test_cases:
            assert(isPermutationHints(str1, str2) == result)


if __name__ == "__main__":
    unittest.main()
