class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        plus=[]
        minus=[]
        for i in asteroids:
            if i>0:
                plus.append(i)
            else:
                while plus and plus[-1]<abs(i):
                    plus.pop()
                if not plus:
                    minus.append(i)
                elif plus[-1]==abs(i):
                    plus.pop()
        return minus+plus
