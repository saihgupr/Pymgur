# Pymgur

> **Note:** This is a fork of [SamuAlfageme/Pymgur](https://github.com/SamuAlfageme/Pymgur).  
> I have updated this project to work properly on modern macOS and Python versions.  
> See below for details on the changes and improvements.

## About

Pymgur is a Python script + macOS Service to right-click upload images anonymously to imgur.com.

## Updates in This Fork

- Fixed compatibility issues with recent macOS and Python versions
- Updated dependencies and installation instructions
- Bug fixes and improved reliability

## Installation & Usage: 
```bash
git clone https://github.com/saihgupr/Pymgur.git
cd Pymgur
python3 setup.py install
sh serviceInstall.sh

```
Just right-click on any [imgur-supported image][imgsup] and select `Upload to imgur` in the contextual menu to upload it anonymously.

<img src="https://i.imgur.com/ylwrRuF.png" alt="Right-Click" width="50%" />

It's link would be displayed as a notification and automatically copied to the clipboard. Once the notification is hidden, you can see it stored in the notification center of your mac, simply by clicking the icon at the top-right corner of your screen:

<img src="https://i.imgur.com/iX5SjX7.png" alt="Notification" width="50%" />

If you uploaded multiple images, clicking on any of them at the notification center will open it in your default web browser.

## Install terminal-notifier
```bash
brew install terminal-notifier

```

## Main Menu Right Click
If the “Upload to imgur” option doesn’t appear in the main right-click menu, here’s how to add it.

```bash
use AppleScript version "2.4" -- Yosemite (10.10) or later
use scripting additions

--based on Erik Johnson's post: 
-- https://apple.stackexchange.com/questions/445872/is-it-possible-to-move-quick-action-from-the-separate-tab-directly-to-context-me/453044#453044

on run
	set libPath to POSIX path of (path to library folder from user domain)
	set strPath to libPath & "Services/"
	set inFile to choose file with prompt "Select a Quick Action file to modify" of type "workflow" default location strPath
	set inPosix to POSIX path of inFile --no slash at end
	try
		do shell script "plutil -remove NSServices.0.NSIconName" & space & quoted form of (inPosix & "/Contents/Info.plist")
		display dialog "Success." & return & return & "The workflow should now appear on the contextual menu, not the Quick Actions menu." buttons {"OK"}
	on error err
		if err contains "no value to remove" then
			display dialog "No change was required. The workflow should appear on the contextual menu, not the Quick Actions menu." buttons {"OK"}
		else
			display dialog err
		end if
	end try
end run

```

## License
All the repository content is available under the MIT license, **except** for the Automator service which is property of Apple Inc. and the Imgur icon displayed on the notifications, property of Imgur LLC.
See [LICENSE.md][license] for details.

[imgur]: http://imgur.com/
[pync]: https://github.com/setem/pync
[imgsup]: http://imgur.com/help/uploading
[trmn]: https://github.com/alloy/terminal-notifier
[license]: https://raw.github.com/SamuAlfageme/Pymgur/master/LICENSE.md
