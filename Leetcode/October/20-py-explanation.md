# PROBLEM STATEMENT
## Flatten Nested List Iterator

You are given a `nested list` of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the `NestedIterator` class:

* `NestedIterator(List<NestedInteger> nestedList)` Initializes the iterator with the nested list `nestedList`.
*   `int next()` Returns the next integer in the nested list.
*   `boolean hasNext()` Returns `true` if there are still some integers in the nested list and `false` otherwise.

Your code will be tested with the following pseudocode:
```
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
```
If `res` matches the expected flattened list, then your code will be judged as correct.

 

Example 1:
```
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
```
Example 2:
```
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
```
 

Constraints:


-   `1 <= nestedList.length <= 500`
-   The values of the integers in the nested list is in the range `[-106, 106]`.


 

<h3>Follow up:</h3> Can you solve it in O(n) time and O(1) space?
<br>
<br>









# Explanation of Nested Iterator for Nested Lists

The code provided is an implementation of a nested iterator that can be used to iterate through nested lists. It assumes the existence of a `NestedInteger` class, which is an interface for handling nested structures.

## NestedInteger Interface
```python
# This is the interface that allows for creating nested lists.
class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
```

The `NestedInteger` class provides three methods to work with nested structures:
1. `isInteger()`: Checks if the `NestedInteger` object holds an integer.
2. `getInteger()`: Retrieves the integer value held by the `NestedInteger` if it's an integer.
3. `getList()`: Retrieves the list of `NestedInteger` objects if it's a nested list.

## NestedIterator Class
```python
class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.__depth = [[nestedList, 0]]
```

The `NestedIterator` class is used to create an iterator for nested lists. It initializes a stack-like data structure (`self.__depth`) to keep track of nested lists.

### Initialization
- The constructor `__init__` takes a `nestedList` as input, which is a list of `NestedInteger` objects.
- It initializes `self.__depth` with a list containing `nestedList` and a pointer `0` to the first element.

```python
    def next(self):
        """
        :rtype: int
        """
        nestedList, i = self.__depth[-1]
        self.__depth[-1][1] += 1
        return nestedList[i].getInteger()
```

### `next` Method
- The `next` method returns the next integer in the nested list.
- It retrieves the current nested list and the pointer from the top of the `self.__depth` stack.
- It increments the pointer to point to the next element.
- It uses the `getInteger` method to get the integer value from the current `NestedInteger`.

```python
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.__depth:
            nestedList, i = self.__depth[-1]
            if i == len(nestedList):
                self.__depth.pop()
            elif nestedList[i].isInteger():
                return True
            else:
                self.__depth[-1][1] += 1
                self.__depth.append([nestedList[i].getList(), 0])
        return False
```

### `hasNext` Method
- The `hasNext` method checks if there is another integer in the nested list.
- It uses a while loop to traverse the nested structure.
- It pops the top element from `self.__depth` if the pointer reaches the end of the current nested list.
- If an integer is encountered, it returns `True`.
- If a nested list is encountered, it updates the `self.__depth` stack to process the nested list's elements.

## Using the NestedIterator
```python
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```

To use the `NestedIterator`, you can instantiate it with a `nestedList`, and then iterate through the nested structure using the `next` and `hasNext` methods.

This iterator allows you to efficiently traverse nested lists and extract integers, making it a useful tool for working with complex data structures.