# 1.short note on access token and access your access token.

#Access Token:An access token is an object that describes the security context of a process.when a user logs on,the
# system verifies the user's password by comparing it with information stored in a security database.If the password
#is authenticated.Even process has a primarytoken describes the security context of the user account associated with
# the process

#4.difference between library and API.

#Library:is a collection of functions/objects that serves one particularpurpose.You could use a library in a variety
# of projects like classes with all code

#An API:is an interface for other programs to interact with your programs or library without having direct access.eg
#if your app needs to vibrate the phone,you must use the Android API method like vibratePhone.

# 2.IP address of google site and facebook.
# a)Name:    google.com
#   Addresses:  2404:6800:4002:807::200e
                # 172.217.161.14
#b) Name:    facebook.com
#   Addresses:  2a03:2880:f137:83:face:b00c:0:25de
                #157.240.23.35

#3.Extract tweets by the help of tweet library.

import tweepy

CONSUMER_KEY='your consumer key'
CONSUMER_SECRET='your consumer secret'
ACCESS_TOKEN='your access token'
ACCESS_TOKEN_SECRET='your access token secret'

auth=tweepy.oAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api=tweepy.API(auth)

status="Testing!"
api.update_status(status=status)

