int i=a.length()-1,j=b.length()-1;
        string res;
        int sum,carry=0;
        while(i>=0 && j>=0)
        {
            sum = (a[i]-'0')+int(b[j]-'0')+carry;
            if(sum==2){carry = 1;sum = 0;}
            else if(sum==3){carry = 1;sum = 1;}
            else if(sum==0){carry = 0;sum = 0;}
            else {carry =  0;sum = 1;}
            res+=to_string(sum);
            i--;j--;
        }
        while(i>=0)
        {
            sum = (a[i]-'0')+carry;
            if(sum==2){carry = 1;sum = 0;}
            else if(sum==0){carry = 0;sum = 0;}
            else {carry =  0;sum = 1;}
            res+=to_string(sum);
            i--;
        }
        while(j>=0)
        {
            sum = (b[j]-'0')+carry;
            if(sum==2){carry = 1;sum = 0;}
            else if(sum==0){carry = 0;sum = 0;}
            else {carry =  0;sum = 1;}
            res+=to_string(sum);
            j--;
        }
        if(carry)res+='1';
        reverse(res.begin(),res.end());
        return res;
    }
//-----------------------------------------------------------------------------
string addBinary(string a, string b) {
        int i=a.length()-1,j=b.length()-1;
        string res;
        int carry=0;
        while(i>=0 || j>=0 || carry==1)
        {
            carry+=(i>=0)?(a[i--]-'0'):0;
            carry+=(j>=0)?(b[j--]-'0'):0;
            res = char(carry%2 +'0') + res;
            carry /= 2;
        }
        return res;
    }
