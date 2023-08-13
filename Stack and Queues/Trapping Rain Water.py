class Solution:
    def trap(self, height: List[int]) -> int:
        lm=0
        rm=0
        l=0
        r=len(height)-1
        res=0
        while l<r:
            if height[l]<=height[r]:
                if height[l]>=lm:
                    lm=height[l]
                else:
                    res=res+lm-height[l]
                l=l+1
            else:
                if height[r]>=rm:
                    rm=height[r]
                else:
                    res=res+rm-height[r]
                r=r-1
        return re
