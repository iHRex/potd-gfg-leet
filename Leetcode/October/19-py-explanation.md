# PROBLEM STATEMENT
## Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:
```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
```
Example 2:
```
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
```
Example 3:
```
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
```
 

Constraints:

- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.

 

<h3>Follow up:</h3> Can you solve it in O(n) time and O(1) space?


# Explanation of Backspace String Compare

## Introduction
The provided code is for a class `Solution` that contains a method `backspaceCompare`. This method is used to compare two strings, `S` and `T`, after applying backspace operations. Backspace is represented by the character `#`, and it means removing the character before it (if any).

Apologies for the confusion. Here's a detailed explanation of the provided Python code:

```python
import itertools


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
```

- `itertools` is a Python module that provides a collection of fast, memory-efficient tools for working with iterators. It contains various functions and classes to help you work with iterators, such as creating iterators, combining them, and applying various operations efficiently. These tools are useful for tasks like creating permutations, combinations, filtering, and transforming data within iterators

- This code defines a class called `Solution`. Inside this class, there's a method named `backspaceCompare`. The method takes two strings, `S` and `T`, as input and returns a boolean value indicating whether the two strings are equal after applying backspace operations.

```python
        def findNextChar(S):
            skip = 0
            for i in reversed(xrange(len(S))):
                if S[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield S[i]
```

- Within the `backspaceCompare` method, there's an inner function called `findNextChar(S)`. This function is used to find the next character in the string `S` after applying backspace operations. It uses a generator (yielding values).

- `skip` is a variable used to count the number of backspaces encountered. It starts as 0.

- The function iterates over the characters of the string `S` in reverse order (right to left). If it encounters a `#`, it increments the `skip` count. If there are characters to be skipped (due to backspaces), it decrements the `skip` count. Otherwise, it yields the character, meaning it's the next character to consider.

```python
        return all(x == y for x, y in
                   itertools.izip_longest(findNextChar(S), findNextChar(T)))
```

- After defining the `findNextChar` function, the `backspaceCompare` method uses the `itertools.izip_longest` function to pair up the characters from the two strings, `S` and `T`, returned by the `findNextChar` function. This function ensures that both strings are aligned from right to left.

- Finally, the code checks if all paired characters are equal (after applying backspace operations) using the `all(x == y for x, y in ...)` statement. If all paired characters are equal, the method returns `True`, indicating that the two strings are equivalent after backspace operations. Otherwise, it returns `False`.

Overall, this code efficiently handles backspace operations and performs a comparison between two strings. It's a useful function for scenarios where you need to compare strings while considering backspaces.