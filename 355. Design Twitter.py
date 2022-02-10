class Twitter:

    def __init__(self):
        self.followers={}
        self.tweetsID={}
        self.tweetsDict={}
    def getTweets(self, userID):
        tweet_list = []
        if userID in self.tweetsID:
            tweet_list = list(self.tweetsID[userID])
        return tweet_list
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweetsID:
            # print ("here 2", tweetId)
            if tweetId not in self.tweetsID[userId]:
                # print ("here 3", tweetId)
                self.tweetsID[userId].add(tweetId)
                self.tweetsDict[tweetId]=len(self.tweetsDict)
            else:
                return None
        else:
            # print ("here 1", tweetId)
            self.tweetsID[userId]=set()
            self.tweetsID[userId].add(tweetId)
            self.tweetsDict[tweetId]=len(self.tweetsDict)
    
    def sort_tweets(self, tweet_list):
        new_dict = {}
        for tweet in tweet_list:
            new_dict[tweet]=self.tweetsDict[tweet]
        final_dict = dict(sorted(new_dict.items(), key=lambda item: -item[1]))
        final_arr = []
        for k,v in final_dict.items():
            if len(final_arr)==10:
                break
            else:
                final_arr.append(k)
        return final_arr
    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_list = []
        tweet_list.extend(self.getTweets(userId))
        if userId in self.followers:
            for users in self.followers[userId]:
                tweet_list.extend(self.getTweets(users))
        if len(tweet_list)>0:
            return self.sort_tweets(tweet_list)
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if  followeeId not in self.followers[followerId]:
                self.followers[followerId].add(followeeId)
            else:
                return None
        else:
            self.followers[followerId]=set()
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)