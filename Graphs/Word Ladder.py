class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
        '''
        def replace(word,i,ch):
            l=list(word)
            l[i]=ch
            return ''.join(l)
        s=set(wordList)
        q=[]
        q.append([beginWord,1])
        #s.remove(beginWord)
        while q:
            word,step=q.pop(0)
            if word==endWord:
                return step
            for i in range(len(word)):
                origin=word[i]
                for j in range(ord('a'),ord('z')+1):
                    ch=chr(j)
                    cha=replace(word,i,ch)
                    if cha in s:
                        s.remove(cha)
                        q.append([cha,step+1])
        return 0'''
