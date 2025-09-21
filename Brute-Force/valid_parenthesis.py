class Solution:
    """
    Problem Link: https://leetcode.com/problems/valid-parentheses/
    - 20. Valid Parentheses

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Learnings:
        - Sometimes, maintaining a lot of data structures or too deep thinking is not required to approach a problem
        - You may have to unbderstand the problem well and re-think on the approach you have thought on
        - This Solution is primarily provided by **CHATGPT**, after my time constraint was reached, 
           but the solutions that I had thought of were too deep or even closer to this, I got a chance to understand the simplicity to solve it and rethink on 
           the way I use to approach to the solution.
    """
    def isValid(self, s: str) -> bool:
        """
        Brute Force: O(N^2) Solution to check the valid patterns combination.
        Context: When the combination is valid, skip it, otherwise, create another string and recheck the pattern
        # We have used a boolean to check whether any pair was skipped after found as valid pair of brackets,
        # if none found, we check if there are any characters left in the string S, if found, then it won't be a vaid string.
        # Otherwise, we skip the pair, and consider any new character which is not in the pair, and add it to the new string to check later. 
        Why this approach:
        - Even if it is the O(n^2) time complexity solution to the problem, it still is simple and easy to explain, 
        - It gives the simplest approach to solve the valid parentheses problem
        """
        while True:
            is_changed = False
            new_chars = []  # use a list instead of string concatenation
            i = 0

            while i < len(s):
                if ((i + 1) < len(s)) and (s[i] + s[i+1]) in ("()", "{}", "[]"):
                    i += 2          # skip this pair
                    is_changed = True
                else:
                    new_chars.append(s[i])  # append character to list
                    i += 1

            s = ''.join(new_chars)  # join list into string at end of pass
            if not is_changed:
                break

        return len(s) == 0     