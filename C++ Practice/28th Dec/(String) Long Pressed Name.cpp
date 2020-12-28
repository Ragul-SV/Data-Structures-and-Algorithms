class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int i=0,j=0;
        int n1 = name.length();
        int n2 = typed.length();
        while(i<n1 && j<n2)
        {
            if(name[i]==typed[j])
            {
                i++;j++;
            }
            else if(j>=1 && typed[j]==typed[j-1])
                j++;
            else
                return false;
        }
        if(i!=n1)return false;
        else
        {
            while(j<n2)
            {
                if(typed[j]!=typed[j-1])return false;
                j++;
            }
        }
        return true;
    }
};
