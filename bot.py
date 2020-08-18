"""
    Example script that will be executed everyday by Travis-CI.

    
    This script take my likers who don't follow me and like them. 
"""


import os 
import time
import random
import sys

from instabot import Bot


bot = Bot(
            proxy=None,
            max_likes_per_day=200,
            max_unlikes_per_day=50,
            max_follows_per_day=100,
            max_unfollows_per_day=20,
            max_comments_per_day=50,
            max_likes_to_like=500,
            filter_users=False,
            filter_verified_accounts=True,
            max_followers_to_follow=30000,
            min_followers_to_follow=10,
            max_following_to_follow=7500,
            min_following_to_follow=10,
            max_following_to_block=2000,
            min_media_count_to_follow=3,
            like_delay=20,
            unlike_delay=20,
            follow_delay=30,
            unfollow_delay=30,
            comment_delay=50,
            comments_file="comments.txt"
)

bot.login(
    username=os.getenv("INSTAGRAM_USERNAME"), 
    password=os.getenv("INSTAGRAM_PASSWORD"),
)

bot.like_hashtag("cyberpunk")

bot.comment_hashtag("cyberpunk")

bot.follow("activefollower")

bot.unfollow_non_followers()
