PYMGUR
==================
A simple python script + a MAC OS Service to right-click uploading images anonymously to [imgur.com][imgur]

## Dependences
* [**Request**][requests]: a python module that handles https request to the imgur API.
* [**pync**][pync]: the python-wrapper around the [**terminal-notifier**][trmn] awesome tool to deliver notifications in MAC OS 10.8
* [**pyperclip**][pyperclip]: the module in charge of handling the clipboard (it'd be not longer needed in v0.2)
## Installation & Usage
```git clone
```
Double-click on the `Pymgur.workflow` Service in order to install it.
Simple right-click on any imgur-supported image and select `Upload to imgur` in the contextual menu to upload it anonymously, it's link would be displayed as a notification and automatically copied to the clipboard. Once the notification is hidden, you can see it stored in the notification center of your mac, simply by clicking the icon at the top-right corner of your screen:
![Screenshot](http://i.imgur.com/ZGqvtwC.png)

##License
All the repository content is available under the MIT license, **except** for the Automator service which is property of Apple Inc.
See [LICENSE.md][license] for details.

[imgur]: http://imgur.com/
[requests]: http://docs.python-requests.org/en/latest/
[pync]: https://github.com/setem/pync
[trmn]: https://github.com/alloy/terminal-notifier
[pyperclip]: https://github.com/asweigart/pyperclip
[license]: https://github.com/SamuAlfageme/pymgur/LICENSE.md