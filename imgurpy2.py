import requests, json, base64, os, sys
from pprint import pprint
# from pyperclip import copy
from pync import Notifier

def setClipboard(text_copied):
    outf = os.popen('pbcopy', 'w')
    outf.write(text)
    outf.close()

image_path = sys.argv[1]
f = open(image_path, 'rb')
saveN = os.path.split(image_path)[1]
saveN = os.path.splitext(saveN)[0]
binary_data = f.read()
b64image = base64.b64encode(binary_data)
payload = {'image': b64image,
           'title': saveN}

r=requests.post("https://api.imgur.com/3/image", 
				headers={"Authorization":"Client-ID ee3e02d4a3ca764"},
				data=payload)
j = json.loads(r.text)
reqSucc = j['success']
if reqSucc: 
	imgURL = j['data']['link']
	imgURL.encode('ascii','ignore')
	print imgURL
	Notifier.notify(imgURL, subtitle='Link copied on the clipboard', title='Image uploaded to Imgur')
	setClipboard(imgURL)
else:
	Notifier.notify('Check if everything is right', title='Error uploading the image')

