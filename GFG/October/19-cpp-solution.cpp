//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution
{
	public:
	//Function to find the level of node X.
	int nodeLevel(int V, vector<int> adj[], int X) 
	{
	 // code here
	 vector<int> ans(V, 1e9);
        
        queue<int> q;
        ans[0] = 0;
        q.push(0);
        
        while(!q.empty()){
            int node = q.front();
            q.pop();
            
            for(auto child : adj[node]){
                if(ans[child] > ans[node] + 1){
                    ans[child] = ans[node] + 1;
                    q.push(child);
                }
            }
        }
        
        return ans[X] == 1e9 ? -1 : ans[X];
	}
};

//{ Driver Code Starts.


int main()
{
    
    int t;
    cin >> t;
    while(t--)
    {
    	int V, E, X;
    	cin >> V >> E;

    	vector<int> adj[V];

    	for(int i = 0; i < E; i++)
    	{
    		int u, v;
    		cin >> u >> v;
    		adj[u].push_back(v);
    		adj[v].push_back(u);
    	}
    	cin>>X;

    	Solution obj;
    	cout << obj.nodeLevel(V, adj, X) << "\n";
    }

    return 0;
}


// } Driver Code Ends