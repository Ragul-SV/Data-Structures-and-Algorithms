class Solution {
public:
    bool buddyStrings(string a, string b) {
        int n1 = a.length();
        int n2 = b.length();
        if(n1!=n2)return false;
        int m1,m2,c=0;
        bool flag = false;
        int count[26]={0};
        for(int i=0;i<n1;i++)
        {
            if(a[i]!=b[i])
            {
                c++;
                if(c==1)m1 = i;
                else if(c==2)m2 = i;
                else if(c>2)return false;
            }
            else
            {
                count[a[i]-'a']++;
                if(count[a[i]-'a']==2)flag = true;
            }
        }
        return (c==0 && flag) || (c==2 && (a[m1]==b[m2] && a[m2]==b[m1]));
    }
};
