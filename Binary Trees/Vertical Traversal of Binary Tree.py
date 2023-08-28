# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def f(root,v,h):
            if root is None:
                return
            if not (v in f.ver):
                f.ver[v] = {h:[root.val]}
            elif not (h in f.ver[v]):
                f.ver[v][h] = [root.val]
            else:
                f.ver[v][h].append(root.val)
            
            f(root.left,v-1,h+1)
            f(root.right,v+1,h+1)
        f.ver = {}
        ans = []
        f(root,0,0)
        for i in sorted(f.ver.keys()):
            curr = []
            for val in sorted(f.ver[i].keys()):
                for key in sorted(f.ver[i][val]):
                    curr += [key]
            ans.append(curr.copy())
        return ans
