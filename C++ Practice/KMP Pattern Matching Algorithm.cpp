#include <bits/stdc++.h>
using namespace std;

void find_lps(string pat,int m,int lps[]);

void KMPSearch(string pat, string txt)
{
	int m = pat.length();
	int n = txt.length();
	int lps[m];
	find_lps(pat,m,lps);
	int i=0,j=0;
	while(i<n)
	{
		if(txt[i]==pat[j])
		{
			i++;
			j++;
		}
		if(j==m)
		{
			cout<<"Pattern Found at "<<i-j<<endl;
			j = lps[j-1];
		}
		else if(i<n and txt[i]!=pat[j])
		{
			if(j!=0) j = lps[j-1];
			else i+=1;
		}
	}
}

void find_lps(string pat,int m,int lps[])
{
	int length = 0;
	lps[0] = 0;
	int i = 1;
	while(i<m)
	{
		if(pat[i]==pat[length])
		{
			length++;
			lps[i] = length;
			i++;
		}
		else
		{
			if(length!=0)
			length = lps[length-1];
			else
			{
				lps[i] = 0;
				i++;
			}
		}
	}
}

int main() {
	char txt[] = "ABABDABACDABABCABAB"; 
    char pat[] = "ABABCABAB"; 
    KMPSearch(pat, txt); 
    return 0; 
}
