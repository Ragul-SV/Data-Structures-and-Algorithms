class Solution {
public:
    bool safeRow(vector<vector<char>> &board,int u,int v,char num)
    {
        for(int i=0;i<9;i++)
        {
            if(i!=u && board[i][v]==num)
                return false;
        }
        return true;
    }
    
    bool safeColumn(vector<vector<char>> &board,int u,int v,char num)
    {
        for(int j=0;j<9;j++)
        {
            if(j!=v && board[u][j]==num)
                return false;
        }
        return true;
    }
    
    bool safeBox(vector<vector<char>> &board,int u,int v,char num)
    {
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                if(i+(u-u%3)!=u && j+(v-v%3)!=v && board[i+(u-u%3)][j+(v-v%3)]==num)
                    return false;
            }
        }
        return true;
    }
    
    bool safe(vector<vector<char>> &board,int i,int j,char num)
    {
        return safeRow(board,i,j,num) && safeColumn(board,i,j,num) && safeBox(board,i,j,num);
    }
    
    bool isValidSudoku(vector<vector<char>>& board) 
    {
         for(int i=0;i<9;i++)
         {
             for(int j=0;j<9;j++)
             {
                 if(board[i][j]!='.' && !safe(board,i,j,board[i][j]))
                     return false;
             }
         }
        return true;
    }
};
