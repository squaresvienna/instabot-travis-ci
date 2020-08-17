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
            max_follows_per_day=50,
            max_unfollows_per_day=20,
            max_comments_per_day=50,
            max_likes_to_like=100,
            filter_users=True,
            max_followers_to_follow=2000,
            min_followers_to_follow=10,
            max_following_to_follow=7500,
            min_following_to_follow=10,
            max_followers_to_following_ratio=10,
            max_following_to_followers_ratio=2,
            max_following_to_block=2000,
            min_media_count_to_follow=3,
            like_delay=30,
            unlike_delay=30,
            follow_delay=60,
            unfollow_delay=60,
            comment_delay=120
)
bot.login(
    username=os.getenv("INSTAGRAM_USERNAME"), 
    password=os.getenv("INSTAGRAM_PASSWORD"),
)

bot.like_hashtag("outrun")

bot.comment_hashtag("outrun")

bot.comment("Love it")

bot.follow("activefollower")

bot.unfollow_non_followers()
