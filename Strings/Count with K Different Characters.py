'''Three Approaches'''
    s = list(s)
    
    def atMost(k):
        count = defaultdict(int)
        left = 0
        ans = 0
        for right, x in enumerate(s):
            count[x] += 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            ans += right - left + 1
        return ans
    return atMost(k) - atMost(k-1)
    '''d={}
    ans=0
    for i in range(k):
        d[s[i]]=d.get(s[i],0)+1
    if len(d)==k:
        ans+=1
    for i in range(k,len(s)):
        d[s[i]]=d.get(s[i],0)+1
        d[s[i-k]]-=1
        if d[s[i-k]]==0:
            del d[s[i-k]]
        if len(d)==k:
            ans+=1
    return ans'''
    '''ans=0
    for i in range(len(s)):
        dist_count=0
        c=[0]*26
        for j in range(i,len(s)):
            if c[ord(s[j])-97]==0:
                dist_count+=1
            c[ord(s[j])-97]+=1
            if dist_count==k:
                ans+=1
    return ans   ''' 
