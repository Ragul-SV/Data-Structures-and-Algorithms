class LRUCache {
public:
    int size;
    list<int> dll;
    unordered_map<int,pair<list<int>::iterator,int>> mp;
    
    LRUCache(int capacity) {
        size = capacity;
    }
    
    int get(int key) {
        if(mp.find(key)==mp.end())
            return -1;
        dll.erase(mp[key].first);
        dll.push_front(key);
        mp[key].first = dll.begin();
        return mp[key].second;
    }
    
    void put(int key, int value) {
        if(mp.find(key)==mp.end())
        {
            if(dll.size()==size)
            {
                int least = dll.back();
                dll.pop_back();
                mp.erase(least);
            }
        }
        else dll.erase(mp[key].first);
        dll.push_front(key);
        mp[key] = {dll.begin(),value};
    }
};
