import re


def urlspam(words):
	type_msg={"Action":"","Message":""}
	urlRegex="(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
	number="(\+91[\-\s]?)?[0]?(91)?[789]\d{9}"
	if re.search(number,words):
		#words=words[:re.search(number,words).start()+2]+"******"+words[re.search(number,words).end()-2:]
		#words=re.sub(number,"**********",words)
		type_msg["Action"]="SPAM"
		return type_msg

	if re.search(urlRegex,words):
		url= words[re.search(urlRegex,words).start():re.search(urlRegex,words).end()]
		if "hdfc" in url:
			type_msg["Action"]="OK"
			type_msg["Message"]=words
		else:
			type_msg["Action"]="SPAM"
			return type_msg
	else:
		type_msg["Action"]="OK"
		type_msg["Message"]=words

	return type_msg



