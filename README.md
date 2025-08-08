# Pymgur

> **Note:** This is a fork of [SamuAlfageme/Pymgur](https://github.com/SamuAlfageme/Pymgur).  
> Updated for modern macOS and Python versions.  
> Changes and improvements are listed below.

## Overview

Pymgur is a Python script and macOS Service that lets you right-click an image and upload it anonymously to imgur.com.

## Changes in This Fork

- Works with recent macOS and Python versions  
- Updated dependencies and install process  
- Bug fixes and stability improvements

## Installation

```bash
git clone https://github.com/saihgupr/Pymgur.git
cd Pymgur
python3 setup.py install
sh serviceInstall.sh
```

## Usage

Right-click any [Imgur-supported image][imgsup] and choose `Upload to imgur` from the menu.  
The image uploads anonymously, and the link appears as a notification and is copied to your clipboard.  

You can view the link later in macOS Notification Center. Clicking the notification opens the image in your browser.

<img src="https://i.imgur.com/ylwrRuF.png" alt="Right-Click" width="50%" />  
<img src="https://i.imgur.com/iX5SjX7.png" alt="Notification" width="50%" />

If you upload multiple images, each will appear in Notification Center and open on click.

## Install `terminal-notifier`

```bash
brew install terminal-notifier
```

## Show in Main Right-Click Menu

If `Upload to imgur` only appears under Quick Actions, run this AppleScript to move it to the main right-click menu:

```applescript
use AppleScript version "2.4"
use scripting additions

-- Based on Erik Johnson's post:
-- https://apple.stackexchange.com/questions/445872/is-it-possible-to-move-quick-action-from-the-separate-tab-directly-to-context-me/453044#453044

on run
	set libPath to POSIX path of (path to library folder from user domain)
	set strPath to libPath & "Services/"
	set inFile to choose file with prompt "Select a Quick Action file to modify" of type "workflow" default location strPath
	set inPosix to POSIX path of inFile
	try
		do shell script "plutil -remove NSServices.0.NSIconName" & space & quoted form of (inPosix & "/Contents/Info.plist")
		display dialog "Success. The workflow should now appear in the main contextual menu." buttons {"OK"}
	on error err
		if err contains "no value to remove" then
			display dialog "No change needed. The workflow should already appear in the main contextual menu." buttons {"OK"}
		else
			display dialog err
		end if
	end try
end run
```

## License

The code in this repository is under the MIT License, **except** the Automator service (property of Apple Inc.) and the Imgur icon used in notifications (property of Imgur LLC).  
See [LICENSE.md][license] for details.

[imgur]: http://imgur.com/  
[pync]: https://github.com/setem/pync  
[imgsup]: http://imgur.com/help/uploading  
[trmn]: https://github.com/alloy/terminal-notifier  
[license]: https://raw.github.com/SamuAlfageme/Pymgur/master/LICENSE.md  
