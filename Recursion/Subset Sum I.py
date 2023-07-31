def solve(ind,s,num,ans):
    if ind==len(num):
        ans.append(s)
        return
    solve(ind+1,s+num[ind],num,ans)
    solve(ind+1,s,num,ans)
def subsetSum(num: List[int]) -> List[int]:
    ans=[]
    solve(0,0,num,ans)
    ans.sort()
    return ans
