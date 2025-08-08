#!/usr/bin/env python3
# PYMGUR v0.8 (Python 3, with SSL bypass)

import urllib.request
import urllib.parse
import base64
import json
import sys
import os
import ssl

class Upload:
    def __init__(self, path, uploadName=None):
        self.imgur_api = "https://api.imgur.com/3/upload"
        self.authHeader = {"Authorization": "Client-ID ee3e02d4a3ca764"}
        self.imgEncoded = self.encode(path, uploadName)
        self.reply = self.makeRequest(self.imgEncoded)
        self.info = self.jsonToDict(self.reply)

        if self.info.get("success"):
            self.img_link = self.info["data"]["link"]
            self.setClipboard(self.img_link)
            self.notifySuccess(self.img_link)
        else:
            self.notifyImgurError()

    def encode(self, path, saveN):
        with open(path, 'rb') as f:
            b64img = base64.b64encode(f.read()).decode('utf-8')
        payload = {'image': b64img}
        if saveN:
            payload['title'] = saveN
        dat = urllib.parse.urlencode(payload).encode('utf-8')
        return dat

    def makeRequest(self, imgB64):
        ssl_context = ssl._create_unverified_context()
        req = urllib.request.Request(self.imgur_api, data=imgB64, headers=self.authHeader)
        with urllib.request.urlopen(req, context=ssl_context) as res:
            return res.read().decode('utf-8')

    def jsonToDict(self, text_reply):
        return json.loads(text_reply)

    def setClipboard(self, text_copied):
        with os.popen('pbcopy', 'w') as outf:
            outf.write(text_copied)

    def notify(self, title, subtitle, message):
        script = f'display notification "{message}" with title "{title}" subtitle "{subtitle}"'
        os.system(f"osascript -e '{script}'")

    def notifySuccess(self, img_link):
        self.notify(
            title="Image uploaded to Imgur",
            subtitle="Link copied to clipboard",
            message=img_link
        )

    def notifyImgurError(self):
        self.notify(
            title="Error uploading the image to imgur",
            subtitle="",
            message="Make sure the image can be uploaded to imgur"
        )

Upload(sys.argv[1])