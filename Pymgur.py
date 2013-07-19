# PYMGUR v0.7
# A python script to upload images anonimously to imgur.com.
import urllib2, urllib, base64, json, sys, os
from pync import Notifier

class Upload:
	def __init__(self,path,uploadName=None):
		self.imgur_api = "https://api.imgur.com/3/upload"
		self.authHeader = {"Authorization":"Client-ID ee3e02d4a3ca764"}
		self.imgEncoded = self.encode(path,uploadName)
		self.reply = self.makeRequest(self.imgEncoded)
		self.info = self.jsonToDict(self.reply)
		if self.info["success"]:
			self.img_link = self.info["data"]["link"]
			self.setClipboard(self.img_link)
			self.notifySuccess(self.img_link)
		else: 
			self.notifyImgurError()
	def encode(self,path,saveN):
		f = open(path,'rb')
		b64img = base64.b64encode(f.read())
		f.close()
		payload = {'image': b64img}
		if saveN: payload.update({'title':saveN})
		dat = urllib.urlencode(payload)
		return dat
	def makeRequest(self,imgB64):
		req = urllib2.Request(self.imgur_api,data=imgB64,
				headers=self.authHeader)
		res = urllib2.urlopen(req)
		foo = res.read()
		return foo
	def jsonToDict(self,text_reply):
		json_rep = json.loads(text_reply)
		return json_rep
	def setClipboard(self,text_copied):
	    outf = os.popen('pbcopy', 'w')
	    outf.write(text_copied)
	    outf.close()
	def notifySuccess(self,img_link):
		Notifier.notify(img_link,
			subtitle='Link copied to clipboard',
			title='Image uploaded to Imgur',
			open=img_link)
	def nofifyImgurError(self):
		Notifier.notify('Make sure the image can be uploaded to imgur',
			title='Error uploading the image to imgur',
			open='http://imgur.com/help/uploading')

Upload(sys.argv[1])

