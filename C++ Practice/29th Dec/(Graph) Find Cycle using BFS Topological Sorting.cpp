class Solution {
public:
    bool canFinish(int n, vector<vector<int>>& prerequisites) {
        vector<vector<int>> G(n);
        vector<int> degree(n,0);
        for(vector<int> pre:prerequisites)
        {
            G[pre[1]].push_back(pre[0]);
            degree[pre[0]]++;
        }
        queue<int> q;
        for(int i=0;i<n;i++)
        {
            if(degree[i]==0)q.push(i);
        }
        int count = n;
        while(!q.empty())
        {
            int course = q.front();
            q.pop();
            count--;
            for(int i=0;i<G[course].size();i++)
            {
                degree[G[course][i]]--;
                if(degree[G[course][i]]==0)
                    q.push(G[course][i]);
            }
        }
        return (count==0);
    }
};
