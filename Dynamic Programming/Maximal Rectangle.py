class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * (n + 1)
        mx=-9999999999
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            st=[]
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
