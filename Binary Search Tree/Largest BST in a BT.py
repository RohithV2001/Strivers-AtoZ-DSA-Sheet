#User function Template for python3

class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        IMIN = float("-inf")
        IMAX = float("inf")
        def solve(root):
            nonlocal IMIN,IMAX
            if root==None:
                return IMAX,IMIN,0
            if (root.left==None and root.right==None):
                return root.data,root.data,1
             
            left=solve(root.left)
            right=solve(root.right)
     
             
            ans=[0,0,0]
             
            if left[1]<root.data and right[0]>root.data:
                ans[0]=min(left[0],right[0],root.data)
                ans[1]=max(right[1],left[1],root.data)
                ans[2]=1+left[2]+right[2]
                return ans
     
            ans[0]=IMIN
            ans[1]=IMAX
            ans[2]=max(left[2],right[2])
            return ans
        return solve(root)[2]


