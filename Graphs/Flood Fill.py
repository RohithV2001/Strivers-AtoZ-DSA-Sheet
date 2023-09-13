class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        r, c = len(image), len(image[0])
        newcolor = image[sr][sc]
        def dfs(i, j):
            if i < 0 or i>=r or j < 0 or j >= c:
                return
            if image[i][j] == color or image[i][j] != newcolor:
                return
            image[i][j] = color
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i,j+1)
            dfs(i, j-1)
        dfs(sr, sc)
        return image
