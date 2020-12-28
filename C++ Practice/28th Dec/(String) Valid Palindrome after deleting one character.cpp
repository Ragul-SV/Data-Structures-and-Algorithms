class Solution {
public:
    bool isPalindrome(string s,int i,int j)
    {
        for(int k=i;k<=i+(j-i)/2;k++)
        {
            if(s[k]!=s[i+j-k])return false;
        }
        return true;
    }
    bool validPalindrome(string s) {
        int n = s.length();
        for(int i=0;i<n/2;i++)
        {
            if(s[i]!=s[n-1-i])
            {
                return isPalindrome(s,i+1,n-1-i) || isPalindrome(s,i,n-1-i-1);
            }
        }
        return true;
    }
};
