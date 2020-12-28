class Solution {
public:
    string reverseWords(string s) {
        string res;
        int n = s.length();
        int i = 0,j;
        while(i<n)
        {
            while(i<n && s[i]==' ')i++;
            j = i;
            while(j<n && s[j]!=' ')j++;
            res = s.substr(i,(j-i)) + " " + res;
            while(j<n && s[j]==' ')j++;
            i = j;
        }
        return res.substr(0,res.length()-1);
    }
};
