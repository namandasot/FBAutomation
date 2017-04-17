#-*- coding:utf-8 -*-
import facebook
import requests
import json

pageId 		= '829994677140795'
#accessToken = 'EAACEdEose0cBAOCOWMZBZC2XoR7oJhjuUudA8J32kYwPep2nDH8aw393CpCUWt6c9Ilv5V3YlVRLZCGO4OOEnw4Kh0P2XSle5reEZAQo35XcJX5uhCVnkpErL36saLwOPa2hl83DduVb7cloSoE2xHysUYLZC8PMZCyf5Kgcd1X0oNCERdWh7g'
accessToken = 'EAACEdEose0cBAOTJfzwq4f5GHm0YobNUdHPZCzDHkF8YwXXcDjrthO2AqubHV5E60oJDrdALBF3M3ZCNCXPgnalX4cjCbgPzVpF82ZA4uZBVPv5gEZB1SLNJ59Eg68Ufd8XgZCJUZC2QiEfdp4KmF6A3LXsA2zQtcXiO8fnl4rzJcOE7UNn0YH6'
graph 		= facebook.GraphAPI(access_token = accessToken, version='2.2')


def getObject():	
	feeds = graph.get_connections(id=pageId, connection_name='feed')
	returnList = []
	for feed in feeds['data']:
		newDict= {}
		try:
			postText = feed['message']
			postId 	 = feed['id']
			newDict["postText"] = postText
			newDict["postID"] = postId
			newDict["comment"] = []

			try:
				for postComment in feed['comments']['data']:
					commentText = postComment['message']
					commentId 	= postComment['id']
					commentatorName = postComment['from']['name']
					newDict["comment"].append({"commentText" :commentText ,"commentID":commentId, 'commentatorName':commentatorName})
			except:
				pass

		except:
			storyText = feed['story']
			storyId   = feed['id']
			newDict["storyText"] = storyText
			newDict["storyID"] = storyId
			newDict["comment"] = []


			try:
				for storyComment in feed['comments']['data']:
					commentText = storyComment['message']
					commentId   = storyComment['id']
					commentatorName = storyComment['from']['name']
					newDict["comment"].append({"commentText" :commentText ,"commentID":commentId, 'commentatorName':commentatorName})

			except:
				pass

		returnList.append(newDict)
	return returnList
	

def putObject(postId, message=''):
	graph.put_comment(object_id=postId, message=message)


def deleteObject(postCommentId):
	url = 'https://graph.facebook.com/v2.2/{0}/?method=delete&access_token={1}'.format(postCommentId, accessToken)
	req = requests.post(url)
	print req.text


def hideObject(postCommentId):
	url = 'https://graph.facebook.com/v2.2/{0}/?is_hidden=true&access_token={1}'.format(postCommentId, accessToken)
	req = requests.post(url)
	print req.text

def replyObject(postCommentId, message=''):
	graph.put_object(parent_object=postCommentId, connection_name='comments', message=message)

def likeObject(postCommentId):
	url = 'https://graph.facebook.com/v2.2/{0}/likes?access_token={1}'.format(postCommentId, accessToken)
	req = requests.post(url)
	print req.text

def privateReplyObject(postCommentId, message=''):
	graph1 		= facebook.GraphAPI(access_token = accessToken, version='2.8')
	graph1.put_object(parent_object=postCommentId, connection_name='private_replies', message=message)



if __name__ == '__main__':
	# privateReplyObject()
	# likeObject()
	print "main"

