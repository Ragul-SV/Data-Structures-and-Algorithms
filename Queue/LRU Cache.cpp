#include <bits/stdc++.h>
using namespace std;

struct Node {
    int key;
    int value;
    Node *next, *pre;
    Node(int key, int value) {
        this->key = key;
        this->value = value;
        next = pre = NULL;
    }
};

class LRUCache {
  private:
    list<pair<int,int>> dq;
    unordered_map<int,list<pair<int,int>>::iterator> hmap;
    int capacity;
    
  public:
    LRUCache(int cap) {
        capacity = cap;
        dq.clear();
        hmap.clear();
    }

    int get(int key) {
        if(hmap.find(key) == hmap.end())
            return -1;
        auto it = hmap.find(key);
        dq.erase(it->second);
        int d = (*(it->second)).second;
        dq.push_front({key,d});
        hmap[key] = dq.begin();
        return d;
    }

    void set(int key, int value) {
        if(hmap.find(key) == hmap.end())
        {
            if(dq.size()==capacity)
            {
                int x = dq.back().first;
                int y = dq.back().second;
                dq.pop_back();
                hmap.erase(x);
            }
        }
        else
        {
            auto it = hmap.find(key);
            dq.erase(it->second);
        }
        dq.push_front({key,value});
        hmap[key] = dq.begin();
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {

        int capacity;
        cin >> capacity;
        int queries;
        cin >> queries;

        LRUCache *cache = new LRUCache(capacity);
        while (queries--) {
            string q;
            cin >> q;
            if (q == "SET") {
                int key;
                cin >> key;
                int value;
                cin >> value;

                cache->set(key, value);

            } else {
                int key;
                cin >> key;
                cout << cache->get(key) << " ";
            }
        }

        cout << endl;
    }
    return 0;
} 
