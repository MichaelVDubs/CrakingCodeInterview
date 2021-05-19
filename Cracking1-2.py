import unittest
from unittest import result


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


class Test(unittest.TestCase):
    test_cases = [
        ("bads", 'dabs', True),
        ("abddfjiis", "abddfjiiq", False),
        ("abcd", "abc", False)
    ]

    def test_is_permutation(self):
        for str1, str2, result in self.test_cases:
            assert(isPermutation(str1, str2) == result)


if __name__ == "__main__":
    unittest.main()
