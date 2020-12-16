vector<int> sortArrayByParityII(vector<int>& A) {
        int j=1,temp;
        for(int i=0;i<A.size();i+=2)
        {
            if(A[i]%2==1)
            {
                while(A[j]%2==1)
                    j+=2;
                
                temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
        }
        return A;
    }
