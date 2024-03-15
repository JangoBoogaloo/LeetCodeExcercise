namespace LinkedListTests;

internal class Twitter
{
    private IDictionary<int, User> _twitterUsers;
    private int _timestamp;
    public Twitter()
    {
        _twitterUsers = new Dictionary<int, User>();
        _timestamp = 0;
    }
    
    public void PostTweet(int userId, int tweetId) 
    {
        if (!_twitterUsers.ContainsKey(userId))
        {
            _twitterUsers[userId] = new User(userId);
        }

        _timestamp++;
        _twitterUsers[userId].Post(tweetId, _timestamp);
    }
    
    public IList<int> GetNewsFeed(int userId)
    {
        var newsFeed = new List<int>();
        var pq = new PriorityQueue<Tweet, int>();
        if (!_twitterUsers.TryGetValue(userId, out var user)) return newsFeed;
        foreach (var followeeId in user.FolloweeIds)
        {
            var latestTweet = _twitterUsers[followeeId].LatestTweet;
            if (latestTweet is not null)
            {
                //Get all latest tweet for all followee
                pq.Enqueue(latestTweet, -latestTweet.Timestamp);
            }
        }

        while (pq.Count >0 && newsFeed.Count < 10)
        {
            var tweet = pq.Dequeue();
            newsFeed.Add(tweet.TweetId);
            if (tweet.Next is not null)
            {
                pq.Enqueue(tweet.Next, -tweet.Next.Timestamp);
            }
        }
        return newsFeed;
    }
    
    public void Follow(int followerId, int followeeId) {
        if (!_twitterUsers.ContainsKey(followerId))
        {
            _twitterUsers[followerId] = new User(followerId);
        }
        if (!_twitterUsers.ContainsKey(followeeId))
        {
            _twitterUsers[followeeId] = new User(followeeId);
        }
        
        _twitterUsers[followerId].Follow(followeeId);
    }
    
    public void Unfollow(int followerId, int followeeId) {
        if (_twitterUsers.ContainsKey(followerId))
        {
            _twitterUsers[followerId].Unfollow(followeeId);
        }

    }

    private class Tweet
    {
        public readonly int TweetId;
        public readonly int Timestamp;
        public Tweet? Next { get; set; }

        public Tweet(int tweetId, int timestamp)
        {
            TweetId = tweetId;
            Timestamp = timestamp;
            Next = null;
        }
    }

    private class User
    {
        public IReadOnlyList<int> FolloweeIds => _followeeIds.ToList();

        public Tweet? LatestTweet { get; private set; }

        private int _userId;
        private HashSet<int> _followeeIds;

        public User(int userId)
        {
            _userId = userId;
            _followeeIds = new HashSet<int>();
            Follow(_userId);
        }

        public void Follow(int followeeId)
        {
            _followeeIds.Add(followeeId);
        }

        public void Unfollow(int followeeId)
        {
            if (followeeId != _userId)
            {
                _followeeIds.Remove(followeeId);
            }
        }

        public void Post(int tweetId, int timestamp)
        {
            var tweet = new Tweet(tweetId, timestamp)
            {
                Next = LatestTweet
            };
            LatestTweet = tweet;
        }
    }
}