'''Isomorphic String'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for i in range(len(s)):
            if s[i] in d1 and d1[s[i]]!=t[i]:
                return False
            if t[i] in d2 and d2[t[i]]!=s[i]:
                return False
            d1[s[i]]=t[i]
            d2[t[i]]=s[i]
        return True

'''If asked to print Isomorphic Strings from the given List'''

from collections import defaultdict
def groupIsomorphic(strs):
    def encode(s):
        d = {}
        return str([d.setdefault(c, len(d)) for c in s])

    groups = defaultdict(list)
    for s in strs:
        groups[encode(s)].append(s)

    return list(groups.values())

print(groupIsomorphic(['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']))
