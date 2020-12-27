class Solution {
public:
    void kmp(string needle,int lps[],int n2)
    {
        lps[0] = 0;
        int i = 1;
        int len = 0;
        while(i<n2)
        {
            if(needle[i]==needle[len])
                lps[i++] = ++len;
            else
            {
                if(len!=0)
                    len = lps[len-1];
                else
                {
                    lps[i++] = 0;
                }
            }
        }
    }
    
    int strStr(string haystack, string needle) {
        int n1=haystack.length();
        int n2=needle.length();
        if(n2==0)return 0;
        int lps[n2];
        kmp(needle,lps,n2);
        int i=0,j=0;
        while(i<n1)
        {
            if(haystack[i]==needle[j])
            {
                i++;
                j++;
            }
            if(j==n2)
            {
                return i-j;
                j = lps[j-1];
            }
            if(i<n1 && haystack[i]!=needle[j])
            {
                if(j!=0)
                j = lps[j-1];
                else
                    i++;
            }
        }
        return -1;
    }
};
