class Solution {
public:
    unordered_map<char,vector<char>> mp;
    //     {'2',{'a','b','c'}}, {'3',{'d','e','f'}}, {'4',{'g','h','i'}},
    //     {'5',{'j','k','l'}}, {'6',{'m','n','o'}}, {'7',{'p','q','r','s'}},
    //     {'8',{'t','u','v'}}, {'9', {'w','x','y','z'}}
    // };
    
    void backtrack(string s,string digits,vector<string> & res)
    {
        if(digits.length()==0)
            res.push_back(s);
        else
        {
            for(int i=0;i<mp[digits[0]].size();i++)
            {
                backtrack(s+mp[digits[0]][i],digits.substr(1),res);
            }
        }
    }
    
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        int n = digits.length();
        if(n==0)return res;
        mp['2'] = {'a','b','c'};
        mp['3'] = {'d','e','f'};
        mp['4'] = {'g','h','i'};
        mp['5'] = {'j','k','l'};
        mp['6'] = {'m','n','o'};
        mp['7'] = {'p','q','r','s'};
        mp['8'] = {'t','u','v'};
        mp['9'] = {'w','x','y','z'};
        backtrack("",digits,res);
        return res;
    }
};
