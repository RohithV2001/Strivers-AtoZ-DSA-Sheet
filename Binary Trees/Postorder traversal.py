class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''Using One Stack'''
        cur=root
        stack=[]
        ans=[]
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                node=stack[-1]
                temp=node.right
                if not temp:
                    temp=stack[-1]
                    stack.pop()
                    ans.append(temp.val)
                    while stack and temp==stack[-1].right:
                        temp=stack[-1]
                        stack.pop()
                        ans.append(temp.val)
                else:
                    cur=temp
        return ans

        '''Using Two Stacks'''
        '''
        st1=[]
        st2=[]
        res=[]
        if not root:
            return
        st1.append(root)
        while st1:
            node=st1.pop()
            st2.append(node.val)
            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)
        while st2:
            res.append(st2.pop())
        return res
        '''
