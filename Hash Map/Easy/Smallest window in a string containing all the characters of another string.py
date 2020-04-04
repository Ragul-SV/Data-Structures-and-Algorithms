def smallestWindow(s,p):
    lens = len(s)
    lenp = len(p)
    if lens<lenp:
        return -1
    dp = dict()
    for i in range(lenp):
        if p[i] not in dp:
            dp[p[i]] = 1
        else:
            dp[p[i]] += 1
    start = 0
    start_index = -1
    min_length = 2**31
    ds = dict()
    c = 0
    for i in range(lens):
        if s[i] not in ds:
            ds[s[i]] = 1
        else:
            ds[s[i]] += 1
    
        if s[i] in dp and ds[s[i]]<=dp[s[i]]:
            c+=1
        if c==lenp:
            while s[start] not in dp or ds[s[start]]>dp[s[start]]:
                if s[start] in dp and ds[s[start]]>dp[s[start]]:
                    ds[s[start]]-=1
                start += 1
            len_window = i-start+1
            if min_length>len_window:
                min_length = len_window
                start_index = start
    if(start_index==-1):
        return -1
    return s[start_index:start_index+min_length]
