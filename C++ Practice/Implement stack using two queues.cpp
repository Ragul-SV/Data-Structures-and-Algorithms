#include <bits/stdc++.h>
using namespace std;

class Stack
{
	queue<int> q1,q2;
	int cur_size;
	public:
	Stack()
	{
		cur_size = 0;
	}
	void push(int val)
	{
		q2.push(val);
		cur_size++;
		while(!q1.empty())
		{
			q2.push(q1.front());
			q1.pop();
		}
		queue<int> q = q1;
		q1 = q2;
		q2 = q;
	}
	void pop()
	{
		if(q1.empty())
		{
			cout<<"Stack is Empty"<<endl;
			return;
		}
		q1.pop();
		cur_size--;
	}
	int top()
	{
		if(q1.empty())
		{
			return -1;
		}
		return q1.front();
	}
	int size()
	{
		return cur_size;
	}
};

int main() {
	Stack s; 
    s.push(1); 
    s.push(2); 
    s.push(3); 
  
    cout << "current size: " << s.size() 
         << endl; 
    cout << s.top() << endl; 
    s.pop(); 
    cout << s.top() << endl; 
    s.pop(); 
    cout << s.top() << endl; 
  
    cout << "current size: " << s.size() 
         << endl; 
    return 0; 
}
