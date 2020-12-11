#include <bits/stdc++.h>
using namespace std;
int evaluatePostfix(string s)
{
	int len = s.length();
	stack<int> st;
	for(int i=0;i<len;i++)
	{
		if(s[i]==' ')continue;
		if(s[i]>='0' && s[i]<='9')
		{
			int num = 0;
			while(s[i]>='0' && s[i]<='9')
			{
				num = num*10 + int(s[i]-'0');
				i++;
			}
			i--;
			st.push(num);
		}
		else
		{
			int temp1 = st.top();
			st.pop();
			int temp2 = st.top();
			st.pop();
			switch(s[i])
			{
				case '+': st.push(temp2+temp1);break;
				case '-': st.push(temp2-temp1);break;
				case '*': st.push(temp2*temp1);break;
				case '/': st.push(temp2/temp1);break;
				case '^': st.push(temp2^temp1);break;
			}
		}
	}
	return st.top();
}

int main()  
{  
    char exp[] = "100 200 + 2 / 5 * 7 +";  
    cout << evaluatePostfix(exp);  
    return 0;  
}
