# -*- coding: utf-8 -*-
import feedparser
from medium import Client
import requests
import argparse
import sys

known_posts_url= "XXXXXXXXXXX"
integration_token = "XXXXXXXXXXX"
client_id = "XXXXXXXXXXX"
client_secret = "XXXXXXXXXXX"

#Configure help and options
parser = argparse.ArgumentParser(description='Tool to cross-post from Known to Medium')
parser.add_argument('-a', action='store_true', help='Publish the whole RSS feed of your Known posts.',required=False)
parser.add_argument('-s', action='store_true', help='Publish one particular Known post by pasting its URL.',required=False)
parser.add_argument('-l', action='store_true', help='Publish the most recent Known post from the RSS feed. (default)',required=False)
parser.add_argument('-t', '--type', help='Choose if publication type should be draft ("draft") or published ("public"). Default is draft.',required=False)
args = parser.parse_args()
#Set default post type to draft
post_type = "draft"
if args.type == "public":
	post_type = "public"
elif args.type != "public" and args.type != "draft":
	print("The post type must be either \"draft\" or \"public\". If left blank, \"draft\" will be used.")
	sys.exit()

#Functionalities to add:
#Options to:
# - Choose if direct post or draft
# - Manually go through and validate every post before cross-publishing

rss_feed_url = known_posts_url + "?_t=rss"

#CONNECT TO MEDIUM API
client = Client(application_id=client_id, application_secret=client_secret)
client.access_token = integration_token
user = client.get_current_user()

#PUBLISH THE WHOLE RSS FEED
def publishWholeRSSFeed():
	#Get the last posts from my RSS feed
	feed = feedparser.parse(rss_feed_url)
	for i in range(len(feed.entries)):
		rss_title = feed.entries[i].title
		rss_text = feed.entries[i].description
		print(rss_title.encode("cp850", "ignore"))
		#Publish on Medium
		post = client.create_post(user_id=user["id"], title=rss_title, content=rss_text, content_format="html", publish_status=post_type)
		print("Post created: " + post['url'])

#PUBLISH SPECIFIC KNOWN POST BY PASTING URL
def publishSpecificKnownURL():
	url = raw_input('''
Paste the URL of your Known post here:
(Make sure the URL ends with a '/')
>>> ''')
	url += '?_t=rss'
	feed = feedparser.parse(url)
	for i in range(len(feed.entries)):
		rss_title = feed.entries[i].title
		rss_text = feed.entries[i].description
		print(rss_title)
		#Publish on Medium
		post = client.create_post(user_id=user["id"], title=rss_title, content=rss_text, content_format="html", publish_status=post_type)
		print("Post created: " + post['url'])

#PUBLISH THE MOST RECENT POST OF THE RSS FEED
def publishLastPost():
	feed = feedparser.parse(rss_feed_url)
	rss_title = feed.entries[0].title
	rss_text = feed.entries[0].description
	#Publish on Medium
	post = client.create_post(user_id=user["id"], title=rss_title, content=rss_text, content_format="html", publish_status=post_type)	
	print("Post created: " + post['url'])

#Check if user has not entered more than one flag, and if not, execute
if (args.a==True and args.s==True) or (args.a==True and args.l==True) or (args.l==True and args.s==True):
	print("You can only set one publishing option.")
	print("Please choose between -a, -s or -l.")
	print("Or leave blank to set default option -l (publish most recent Known post).")
elif args.a == True:
	publishWholeRSSFeed()
elif args.s == True:
	publishSpecificKnownURL()
elif args.l == True:
	publishLastPost()
else:
	publishLastPost()