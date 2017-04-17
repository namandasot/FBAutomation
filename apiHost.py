from flask import Flask,request,jsonify
from proj1 import *
from urllib import urlopen
import json
import requests
import urllib2
from gevent.wsgi import WSGIServer
app = Flask(__name__)
import time
import datetime
from flask_cors import CORS,cross_origin
from spamAnalysis import urlspam
from  sentimentAnalysis import main
from fbCommands import *
CORS(app)
@app.route('/')


def get():
	print "Naman"
	questionReply = ", we will be happy to solve your issues. Our executive will be in touch soon"
	appreciationReply = ", thank you. Your feedback is appreciated"
	badReply = ", How can we help you?"
        posts = getObject()
	print "get"
	print posts
        for post in posts:
                for comment in  post["comment"]:
			try:
				print "Comment1"
				query = comment["commentText"]
				print "Query ",query.encode('utf-8','ignore ascii')
				a= GoogleTranslator()
				print  "XYZ"
				transQuery=  a.translate(query)
				transQuery = transQuery[0]["translatedText"]
				print transQuery
				spamFilter = urlspam(transQuery)
				if(spamFilter["Action"] == 'SPAM'):
					hideObject(comment["commentID"])
					continue

				if ifQuestion(transQuery):
					repl = "Hi " + str(comment["commentatorName"]).split(" ")[0]+questionReply
					replyObject(comment["commentID"],repl)
					privateReplyObject(comment["commentID"],"Hi")
					continue


				transQuery = main(transQuery) #To detect Sentiment 
				sentimentScore = transQuery["documentSentiment"]["score"]

				if sentimentScore < -0.5 : 
					repl = "Hi " + str(comment["commentatorName"]).split(" ")[0]+ badReply
					replyObject(comment["commentID"],repl)
	#hideObject(comment["commentID"])
					
				elif sentimentScore >= 0.5 :
					repl = "Hi " + str(comment["commentatorName"]).split(" ")[0]+ appreciationReply
					replyObject(comment["commentID"],repl )
					likeObject(comment["commentID"])
			except:
				pass		



        return jsonify({"message": "success"})

def ifQuestion(query):
        if "?" in query:
                return 1
        if "Wh" in query:
                return 1
        if "wh" in query:
                return 1

        return 0

if __name__ == '__main__':
#    app.run(host='0.0.0.0',port=6020)
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()


