import webbrowser
import time
import os


for i in range(5):
	#Open a website
	webbrowser.open('https://www.website.com/') 
	#Wait few seconds
	print('Lets wait', 3, 'seconds')
	time.sleep(3)
	#Close the website
	os.system("killall -9 'Google Chrome'")
	print('This is the', i, 'th time www.website.com is opened & closed')


