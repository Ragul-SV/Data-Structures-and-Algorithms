#include <bits/stdc++.h>
using namespace std;

bool balanced(string str)
{
	stack<char> s;
	char temp;
	for(int i=0;i<str.length();i++)
	{
		if(str[i]=='(' || str[i]=='[' || str[i]=='{'){
			s.push(str[i]);
			continue;
		}
		if(s.empty()) return false;
		switch(str[i])
		{
			case ')':
			temp = s.top();
			s.pop();
			if(temp!='(')return false;
			break;
			case ']':
			temp = s.top();
			s.pop();
			if(temp!='[') return false;
			break;
			case '}':
			temp = s.top();
			s.pop();
			if(temp!='{') return false;
			break;
		}
	}
	return s.empty();
}

int main() {
	string str = "({()}[])";
	if(balanced(str)) cout<<"Balanced";
	else cout<<"Not Balanced";
	return 0;
}
