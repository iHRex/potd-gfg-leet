# Explanation of Identifying Eventual Safe Nodes in a Directed Graph

## Introduction
The provided Python code finds and returns the eventual safe nodes in a directed graph. An eventual safe node is a node from which you can reach an end node (leaf) by following a path of directed edges. It ensures that traveling from that node will not lead to a cycle.

## Function Definitions
```python
from typing import List

class Solution:
    def eventualSafeNodes(self, V: int, adj: List[List[int]]) -> List[int]:
```

- The code defines a class `Solution` that contains the `eventualSafeNodes` method.
- `V` represents the number of nodes in the graph.
- `adj` is a list of lists that represents the adjacency list of the directed graph.

## Inner Function: `isSafeNode`
```python
        def isSafeNode(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1  # Mark the node as visiting.

            for neighbor in adj[node]:
                if not isSafeNode(neighbor):
                    return False  # If any neighbor is not safe, the current node is not safe.

            visited[node] = 2  # Mark the node as visited and safe.
            return True
```

- The code defines an inner function called `isSafeNode` to check if a given node is an eventual safe node.
- It uses a visited array `visited` to track the status of each node:
  - 0: unvisited
  - 1: visiting
  - 2: visited and safe
- If a node is already marked as visiting (1), it means there's a cycle, so the node is not safe.
- If a node is already marked as visited and safe (2), it is safe.
- Otherwise, the code marks the node as visiting and explores its neighbors:
  - If any neighbor is not safe, the current node is not safe.
  - If all neighbors are safe, the current node is marked as visited and safe.

## Main Function
```python
        result = []
        visited = [0] * V  # Initialize all nodes as unvisited (0).

        for i in range(V):
            if isSafeNode(i):
                result.append(i)

        return sorted(result)
```

- The main function initializes an empty list called `result` to store eventual safe nodes and an array `visited` to track the visited status of nodes.
- It iterates through all nodes in the graph and calls the `isSafeNode` function to determine if each node is an eventual safe node.
- If a node is an eventual safe node, it's added to the `result` list.
- The `result` list is sorted and returned as the eventual safe nodes.

## Driver Code
```python
if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end=' ')
        print()
```

- The driver code reads the number of test cases (`T`).
- For each test case, it reads the number of nodes (`V`) and edges (`E`) and constructs the adjacency list (`adj`) to represent the directed graph.
- It creates an instance of the `Solution` class and calls the `eventualSafeNodes` method to find and print the eventual safe nodes for each test case.

This code efficiently identifies the eventual safe nodes in a directed graph by applying depth-first search (DFS) and checks for cycles. It returns the sorted list of eventual safe nodes for each test case.