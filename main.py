_author_ = "Marcus Salinas"
import praw
from urllib import request
import os
import time
# this will go to reddit and download the top 100 items of the week from whatever subreddit you want into a folder that I will set to my
# background every week.

# define user agent
user_agent = "RedditExperiment/1.0 by /u/PM_ME_UNWANTED_MONEY"

clientID = ""
clientSecret = ""
userName = ""
passWord = ""

with open("info.txt",'r') as inputfile:
    line = inputfile.readline()
    line = line.split(",")
    clientID = line[0]
    clientSecret = line[1]
    userName = line[2]
    passWord = line[3]


reddit = praw.Reddit(client_id=clientID,
                     client_secret=clientSecret,
                     password=passWord,
                     username=userName,
                     user_agent=user_agent)

os.chdir("C:\\Users\\Marcus\\Google Drive\\DankMemes")
newDir = os.getcwd() + "\\Dank Memes - " + str(time.strftime("%Y-%m-%d"))

if not os.path.exists(newDir):
    os.mkdir(newDir)

os.chdir(newDir)

dankmemes = reddit.subreddit("dankchristianmemes").top(time_filter="week",limit=150)
memeCount = 1


for meme in dankmemes:
    print("On Meme: " + str(memeCount))
    try:
        url = meme.url
        request.urlretrieve(url,str(memeCount)+'.jpg')
        memeCount+=1
    except Exception as e:
        print("Not working. ")

