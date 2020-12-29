Node* cloneGraph(Node* node) {
        if(node==NULL)return NULL;
        unordered_map<Node*,Node*> mp;
        queue<Node*> q;
        Node* copy = new Node(node->val);
        mp[node] = copy;
        q.push(node);
        while(!q.empty())
        {
            Node* cur = q.front();
            q.pop();
            for(int i=0;i<cur->neighbors.size();i++)
            {
                if(mp.find(cur->neighbors[i])==mp.end())
                {
                    mp[cur->neighbors[i]] = new Node(cur->neighbors[i]->val);
                    q.push(cur->neighbors[i]);
                }
                mp[cur]->neighbors.push_back(mp[cur->neighbors[i]]);
            }
        }
        return copy;
    }
