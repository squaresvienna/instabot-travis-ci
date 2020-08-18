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
            max_unlikes_per_day=0,
            max_follows_per_day=100,
            max_unfollows_per_day=20,
            max_comments_per_day=50,
            max_likes_to_like=1000,
            filter_users=False,
            filter_verified_accounts=True,
            max_followers_to_follow=30000,
            min_followers_to_follow=10,
            max_following_to_follow=2000,
            min_following_to_follow=10,
            max_following_to_block=2000,
            min_media_count_to_follow=3,
            like_delay=10,
            unlike_delay=10,
            follow_delay=30,
            unfollow_delay=30,
            comment_delay=40,
            comments_file="comments.txt"
)

bot.login(
    username=os.getenv("INSTAGRAM_USERNAME"), 
    password=os.getenv("INSTAGRAM_PASSWORD"),
)

bot.like_timeline()

hashtag = bot.get_hashtag_medias("retrowave")
bot.like_medias(hashtag)

bot.comment_medias(hashtag)

users = bot.get_hashtag_users("retrowave")
bot.follow_users(users)

bot.follow("activefollower")
