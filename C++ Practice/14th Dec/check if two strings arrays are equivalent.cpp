class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        int i=0,j=0,ii=0,jj=0;
        while(i<word1.size() && j<word2.size())
        {
            if(word1[i][ii]!=word2[j][jj]) return false;
            ii++;jj++;
            if(ii==word1[i].length()){i++;ii=0;}
            if(jj==word2[j].length()){j++;jj=0;}
            if(i==word1.size() && j==word2.size()) return true;
        }
        return false;
    }
};
