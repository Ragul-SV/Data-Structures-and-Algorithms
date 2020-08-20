#include<bits/stdc++.h>
using namespace std;

void freq(string s,char c,int num)
{
	int count = 0;
	for(int i=0;i<s.length();i++)
	{
		if(s[i]==c)
		{
			count++;
			if(count==num)
			{
				if(i==s.length()-1) cout<<"Empty String";
				else
				cout<<s.substr(i+1,s.length()-(i+1));
				return;
			}
		}
	}
}

int main()
{
	string s;
	getline(cin,s);
	char c;
	cin>>c;
	int num;
	cin>>num;
	freq(s,c,num);
	return 0;
}
