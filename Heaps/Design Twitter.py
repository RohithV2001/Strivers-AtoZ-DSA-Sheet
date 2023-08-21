import heapq
class Twitter:

    def __init__(self):
        self.followmap=collections.defaultdict(set)
        self.postmap=collections.defaultdict(list)
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postmap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        heap=[]
        self.followmap[userId].add(userId)
        for user in self.followmap[userId]:
            for post in self.postmap[user]:
                heap.append(post)
        heapq.heapify(heap)
        while heap and len(res)<10:
            count,tweet=heapq.heappop(heap)
            res.append(tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
