class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''USING SINGLE PASS EFFICIENT'''
        st=[]
        mx=-9999999999
        for i in range(len(heights)+1):
            while st and (i==len(heights) or heights[st[-1]]>heights[i]):
                height=heights[st[-1]]
                st.pop()
                width=0
                if st:
                    width=i-st[-1]-1
                else:
                    width=i
                mx=max(mx,width*height)
            st.append(i)
        return mx

        ''' USING TWO PASSES MONOTONIC STACK'''
        left=[-1]*len(heights)
        right=[-1]*len(heights)
        st=[]
        n=len(heights)
        for i in range(n):
            while len(st)!=0 and heights[st[-1]]>=heights[i]:
                st.pop()
            if len(st)==0:
                left[i]=0
            else:
                left[i]=st[-1]+1
            st.append(i)
        while len(st)!=0:
            st.pop()
        for i in range(n-1,-1,-1):
            while len(st)!=0 and heights[st[-1]]>=heights[i]:
                st.pop()
            if len(st)==0:
                right[i]=n-1
            else:
                right[i]=st[-1]-1
            st.append(i)
        maxi=0
        for i in range(n):
            maxi=max(maxi,(right[i]-left[i]+1)*heights[i])
        return maxi
