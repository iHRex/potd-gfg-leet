# Problem Statement

## Level of Nodes
Given an integer X and an undirected acyclic graph with V nodes, labeled from 0 to V-1, and E edges, find the level of node labeled as X.

Level is the minimum number of edges you must travel from the node 0 to some target.

If there doesn't exists such a node that is labeled as X, return -1.

### Example 1:

Input:

<img alt="Medium" src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/701248/Web/Other/afb73eb4-8c50-4e77-b161-e3fd4d35939c_1685086954.png"/>

X = 4

Output:2

Explanation:

<img alt="Medium" src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/701248/Web/Other/ef6cced7-96f1-46e4-bf8b-4fc091c04ee7_1685086954.png"/>

We can clearly see that Node 4 lies at Level 2.

### Example 2:

Input:

<img alt="Medium" src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/701248/Web/Other/79ea2467-b795-4328-a0aa-d2679f671e55_1685086954.png"/>

X = 1
Output: 1

Explanation: Node 1 lies at level 1, immediate after Node 0.

### Your task:
You dont need to read input or print anything. Your task is to complete the function nodeLevel() which takes two integers V and X denoting the number of vertices and the node, and another adjacency list adj as input parameters and returns the level of Node X. If node X isn't present it returns -1.

##### Expected Time Complexity: O(V)

##### Expected Auxiliary Space: O(V)

Constraints:

    2 ≤ V ≤ 104
    1 ≤ E ≤ 104
    0 ≤ adji, j < V
    1 ≤ X < V
Graph doesn't contain multiple edges and self loops.





# Solution Statement and Explanation of Finding the Level of a Node in a Graph


The provided C++ code calculates the level of a given node in an undirected graph using breadth-first search (BFS). The level of a node in a graph is its distance from the source node, and it is measured in terms of the number of edges in the shortest path.


```cpp
class Solution
{
public:
    // Function to find the level of node X.
    int nodeLevel(int V, vector<int> adj[], int X) 
    {
        // code here
        vector<int> ans(V, 1e9);  // Initialize a vector to store the distance to each node, initially set to a large value.
        
        queue<int> q;  // Create a queue for BFS.
        ans[0] = 0;  // Set the distance of the source node to 0.
        q.push(0);  // Push the source node into the queue.
```

- The code defines a class `Solution` with a method called `nodeLevel`. This method calculates the level of a given node in a graph.
- `V` represents the number of nodes in the graph.
- `adj` is an array of vectors where `adj[i]` represents the neighbors of node `i`.
- `X` is the node for which we want to find the level.

```cpp
        while (!q.empty()) {
            int node = q.front();  // Get the front node from the queue.
            q.pop();
```

- The code starts a `while` loop to perform a breadth-first search (BFS) traversal while the queue is not empty.
- It dequeues the front node from the queue and stores it in the variable `node`.

```cpp
            for (auto child : adj[node]) {  // Iterate through the neighbors of the current node.
                if (ans[child] > ans[node] + 1) {
                    ans[child] = ans[node] + 1;  // Update the distance to the neighbor if a shorter path is found.
                    q.push(child);  // Push the neighbor into the queue for further exploration.
                }
            }
        }
```

- Within the loop, the code iterates through the neighbors (`child`) of the current node.
- It checks if a shorter path to the neighbor is found by comparing the distance to the neighbor (`ans[child]`) with the distance to the current node plus one (`ans[node] + 1`).
- If a shorter path is found, it updates the distance to the neighbor and pushes the neighbor into the queue for further exploration.

```cpp
        return ans[X] == 1e9 ? -1 : ans[X];  // Return the level of the node X. If it's still the initial large value (1e9), it means there is no path to X, and it returns -1.
    }
};
```

- After the BFS traversal, the code returns the level of the node `X`. It checks if the distance to `X` is still the initial large value (1e9). If it is, it means there is no path to `X`, and it returns -1.
- This code efficiently calculates the level of a given node in a graph using BFS and handles cases where the node is unreachable or not in the graph. It returns the shortest distance from the source node to the target node, representing the level of the target node.