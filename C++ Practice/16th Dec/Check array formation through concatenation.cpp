vector<int> vec(101,-1);
        for(int i=0;i<pieces.size();i++){
            vec[pieces[i][0]] = i;        
        }   
        int i=0;
        while(i<arr.size())
        {
            int temp = vec[arr[i]],j = 0;
            if(temp==-1)return false;
            while(j<pieces[temp].size())
            {
                if(arr[i++]!=pieces[temp][j++])return false;
            }
        }
        return true;
    }
