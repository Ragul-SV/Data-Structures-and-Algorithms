#include<bits/stdc++.h>
using namespace std;
class LRUCache
{
	list<int> dq;
	int size;
	unordered_map<int,list<int>::iterator> mp;
	public:
	LRUCache(int c)
	{
		size = c;
	}
	void refer(int val)
	{
		if(mp.find(val)==mp.end())
		{
			if(dq.size()==size)
			{
				int temp = dq.back();
				dq.pop_back();
				mp.erase(temp);
			}
		}
		else
		{
			dq.erase(mp[val]);
		}
		dq.push_front(val);
		mp[val] = dq.begin();
	}
	void display()
	{
		for(auto i=dq.begin();i!=dq.end();i++)
		{
			cout<<*i<<" ";
		}
		cout<<endl;
	}
};



int main()
{
	LRUCache ca(4); 
    ca.refer(1); 
    ca.refer(2); 
    ca.refer(3); 
    ca.refer(1); 
    ca.refer(4); 
    ca.refer(5); 
    ca.display(); 
	return 0;
}
