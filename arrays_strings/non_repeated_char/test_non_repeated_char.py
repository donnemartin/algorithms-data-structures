import unittest

class TestNonRepeatedChar(unittest.TestCase):
    def test_non_repeated_char(self, func):
        self.assertEqual(func(None), '')
        self.assertEqual(func('a'), 'a')
        self.assertEqual(func('absfasxv'), 'b')
        self.assertEqual(func(''), '')
        print('Success: test_non_repeated_char')

def main():
    test = TestNonRepeatedChar()
    non_repeated_char = NonRepeatedChar()
    test.test_non_repeated_char(non_repeated_char.non_repeated_char)


if __name__ == '__main__':
    main()
