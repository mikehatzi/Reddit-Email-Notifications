import praw
import time
from time import strftime, localtime
import smtplib
from email.mime.text import MIMEText

# Setup Reddit info
reddit = praw.Reddit(client_id = '') # Your client id here
	client_secret = ''				 # Your client secret here
	username = ''					 # Your username
	password = ''					 # Your password
	user_agent = 'FirstScript_1.1'
	
subreddit = reddit.subreddit("buildapcsales")
oldResult = 0

def checkTheSub():
	for submission in subreddit.new(limit=1):
		analyze = submission.title
		
		# Anything 1080ti related
		if analyze.find("1080Ti") > 0 or analyze.find("1080 Ti") > 0:
			paired = {'1080ti': analyze}
			return paired
			
		if analyze.find("1080ti") > 0 or analyze.find("1080 ti") > 0:
			paired = {'1080ti': analyze}
			return paired
			
		if analyze.find("1080TI") > 0 or analyze.find("1080 TI") > 0:
			paired = {'1080ti': analyze}
			return paired
		
		
		# Dell Monitor
		if analyze.find("S2716DG") > 0:
			paired = {'S2716DG': analyze}
			return paired
			return
		
		
		# 240 Hz Monitor
		if analyze.find("240 HZ") > 0 or analyze.find("240 Hz") > 0:
			paired = {'240 Hz Monitor': analyze}
			return paired
			
		if analyze.find("240HZ") > 0 or analyze.find("240Hz") > 0:
			paired = {'240 Hz Monitor': analyze}
			return paired
			
		return 0
		
def sendTheEmail(pairing):

	if '1080ti' in pairing:
		msg = MIMEText(pairing['1080Ti'])
		msg['Subject'] = "1080Ti Result"
		print("Found a 1080Ti!")
	elif 'S2716DG' in pairing:
		msg = MIMEText(pairing['S2716DG'])
		msg['Subject'] = "S2716DG Result"
		print("Found a S2716DG!")
	elif '240 Hz Monitor' in pairing:
		msg = MIMEText(pairing['240 Hz Monitor'])
		msg['Subject'] = "240 Hz Monitor Result"
		print("Found a 240 Hz Monitor!")
		
	msg['From'] = "pythonbot888@gmail.com"
	msg['To] = "pythonbot888@gmail.com"
	
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login("pythonbot888@gmail.com", "thisisabot")
	server.send_message(msg)
	print("Email sent!")
	return
	
while True:
	result = checkTheSub()
	if result == oldResult and result != 0:
		pass
	elif result:
		sendTheEmail(result)
		oldResult = result
	print(strftime("%I:%M", localtime()), end="")
	print("...")
	time.sleep(30)
