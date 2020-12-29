bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int i = 0, len = flowerbed.size();
        int count = 0;
        while(i<len)
        {
            if(flowerbed[i]==0 && (i==0 || flowerbed[i-1]==0) && (i==len-1 || flowerbed[i+1]==0))
            {
                count++;
                flowerbed[i] = 1;
            }
            i++;
        }
        return count>=n;
    }
