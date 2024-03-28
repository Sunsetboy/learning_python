import unittest

'''
Pad for Asiya Shakhmametova - Software Engineer - Backend Generalist

Let's write a function with the following signature:

bool isMatch(string pattern, string word)
This function returns true if (and only if) word is a complete match for pattern.

If pattern contains only letters, this function should just do a string comparison:

isMatch("datadog", "datadog") => true
isMatch("datadog", "datadogs") => false
If pattern contains a number, we'll treat it as a wildcard. In the number's position, a matching word can contain any letters, as long as there are as many letters as the number.

isMatch("3", "aaa") => true
isMatch("3", "aa") => false
isMatch("d3dog", "datadog") => true
isMatch("d3dog", "dtdog") => false
The expected functionality can be summarized in a table:

pattern  |   word   | output
===========================
datadog  | datadog  | true
datadog  | datadogs | false
3        | aaa      | true
3        | aa       | false
d3dog    | datadog  | true
d3dog    | dtdog    | false

- if no numbers -> len(pattern) == len(word)
- both not empty
- word: lowercase alphabetic

Approach:
- decode pattern -> d3dog => d...dog // d300dog => d...dog (followup)
- new_pattern vs word char by char
- multiple digits -> need to convert string to number:
how: init k = 0, final number k = p[i] * 10 + p[i+1]
for the ex. d300dog it gives:
1: k = 0 * 10 + 3
2: k = 3 * 10 + 0 = 30
3: k = 30 * 10 + 0 = 300

'''


class Solution:
    def validate_string(self, pattern: str, word: str)->bool:
        p_pattern = p_word = 0

        while p_pattern < len(pattern) and p_word < len(word):
            if word[p_word] == pattern[p_pattern]:
                p_pattern += 1
                p_word += 1
                continue
            if pattern[p_pattern].isdigit() == False and word[p_word] != pattern[p_pattern]:
                # mismatch, return false
                return False
            # digit in the pattern
            current_number_digits = []
            while p_pattern<len(pattern) and pattern[p_pattern].isdigit():
                current_number_digits.append(pattern[p_pattern])
                p_pattern += 1
            chars_to_skip = int(''.join(current_number_digits))
            p_word += chars_to_skip
            

        if p_pattern != len(pattern) or p_word != len(word):
            return False

        return True

class D3Test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        self.assertTrue(solution.validate_string("d3dog", "datadog"))

    def test_case3(self):
        solution = Solution()
        self.assertFalse(solution.validate_string("d3dog", "dtadog"))

    def test_case4(self):
        solution = Solution()
        self.assertFalse(solution.validate_string("d3dog", "datadogs"))

    def test_case5(self):
        solution = Solution()
        self.assertTrue(solution.validate_string("3", "aaa"))

    def test_case6(self):
        solution = Solution()
        self.assertTrue(solution.validate_string("datadog", "datadog"))

    def test_case7(self):
        solution = Solution()
        self.assertTrue(solution.validate_string("d1t2og", "datadog"))

    def test_case_number(self):
        solution = Solution()
        self.assertTrue(solution.validate_string("d10g", "daaaaaaaaaag"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
