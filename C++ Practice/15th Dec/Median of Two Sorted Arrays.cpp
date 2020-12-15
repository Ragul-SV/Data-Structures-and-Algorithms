double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int i=0,j=0;
        int n1 = nums1.size();
        int n2 = nums2.size();    
        int med = (n1+n2);
        bool flag;
        double temp;
        int k=0;
        if(med%2!=0) med = med/2, flag=true;
        else med = med/2 - 1, flag = false;
        cout<<med<<" "<<flag<<endl;
        while(i<n1 && j<n2)
        {
            if(nums1[i]<nums2[j])
            {
                cout<<k<<" "<<"i"<<nums1[i]<<endl;
                if(k==med)
                {
                    cout<<"hello"<<endl;
                    if(flag) return (double)nums1[i];
                    else{
                        temp = nums1[i];
                        i++;
                        if(i<n1 && j<n2)
                        {
                            if(nums1[i]<nums2[j])
                            {temp = (temp+nums1[i])/2;return temp;}
                                
                            else
                            {temp = (temp+nums2[j])/2;return temp;}
                        }
                        else if(i<n1){temp = (temp+nums1[i])/2;return temp;}
                        else if(j<n2){temp = (temp+nums2[j])/2;return temp;}
                    }
                }
                i++;
                k++;
            }
            else
            {
                cout<<k<<" "<<"j"<<nums2[j]<<endl;
                if(k==med)
                {
                    if(flag) return (double)nums2[j];
                    else{
                        temp = nums2[j];
                        j++;
                        if(i<n1 && j<n2)
                        {
                            if(nums1[i]<nums2[j])
                            {temp = (temp+nums1[i])/2;
                                return temp;}
                            else
                            {temp = (temp+nums2[j])/2;
                                return temp;} 
                        }
                        else if(i<n1){temp = (temp+nums1[i])/2;return temp;}
                        else if(j<n2){temp = (temp+nums2[j])/2;return temp;}
                    }
                }
                j++;
                k++;
            }
        }
        while(i<n1)
        {
            cout<<k<<" "<<"i"<<nums1[i]<<endl;
            if(k==med)
            {
                if(flag) return (double)nums1[i];
                else{
                    temp = nums1[i];
                    i++;
                    temp = (temp+nums1[i])/2;
                    return temp;
                }
            }
            i++;
            k++;
        }
        while(j<n2)
        {
            cout<<k<<" "<<"j"<<nums2[j]<<endl;
            if(k==med)
            {
                if(flag) return (double)nums2[j];
                else{
                    temp = nums2[j];
                    j++;
                    temp = (temp+nums2[j])/2;
                    return temp;
                }
            }
            j++;
            k++;
        }
        return -1;
    }
