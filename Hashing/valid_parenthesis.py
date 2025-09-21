class Solution:
    """
    Problem Link: https://leetcode.com/problems/valid-parentheses/
    - 20. Valid Parentheses

    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Learnings:
    - Hashing if used properly,can result in the optimised approach to solve an issue. 
    """
    def isValid(self, s: str) -> bool:
        # Optimal Solution: O(n) to check every pattern
        # Maintaing a stack of open-brackets and poping out the last item when comparing with a closed bracket
        # the function return false, if the brackets is not a valid pair or the stack is empty while the for-loop is running. 
        # Now, the reason this is happening -> `return false when, the stack is empty while the for-loop is running` - is because,
        # either the first item in the string is a closed bracket itself(invalid), or all the other characters are not making any valid pattern
         
        # Hash of closed brackets, called when a closed bracket is found in the string and it's value is compared with the last item of the stack,
        # to check whether the pair is valid
        br_hash = {
            "}":"{",
            "]":"[",
            ")":"(",
        }

        # stack for open brackets
        ob_list = []

        for i in s:
            # If character is an open bracket, it will not be a key in the br_hash (closed brackets map)
            if not br_hash.get(i):
                # inserting the open bracket in ob_list
                ob_list.append(i)
            else:
                # stack will only be empty when the current item i is a closed bracket,
                # and there is no open bracket for the same
                if not ob_list or (br_hash[i] != ob_list.pop()):
                    return False
        # When all the brackets are considered as a valid pair, we return True
        if not ob_list:
            return True
        return False