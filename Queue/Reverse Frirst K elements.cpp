queue<ll> modifyQueue(queue<ll> q, int k)
{
    deque<int> s;
    for(int i=0;i<k;i++)
    {
        s.push_front(q.front());
        q.pop();
    }
    while(!q.empty())
    {
        s.push_back(q.front());
        q.pop();
    }
    while(!s.empty())
    {
        q.push(s.front());
        s.pop_front();
    }
    return q;
}
