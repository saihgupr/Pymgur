PYMGUR
==================
Since I share so many images directly from my desktop with imgur I've made this simple python script + a MAC OS Service to right-click upload images anonymously to [imgur.com][imgur]

## Tech:
* [**pync**][pync]: the python-wrapper around the [**terminal-notifier**][trmn] awesome tool to deliver notifications in MAC OS 10.8.

## Installation & Usage: 
*Not quite ready yet*
```bash
git clone
cd Pymgur
python setup.py install
sh serviceInstall.sh

```
Just right-click on any [imgur-supported image][imgsup] and select `Upload to imgur` in the contextual menu to upload it anonymously.

![Screenshot](http://i.imgur.com/omEeUhl.png)

It's link would be displayed as a notification and automatically copied to the clipboard. Once the notification is hidden, you can see it stored in the notification center of your mac, simply by clicking the icon at the top-right corner of your screen:

![Screenshot](http://i.imgur.com/b9I4ddO.png)

If you uploaded multiple images, clicking on any of them at the notification center will open it in your default web browser.

## TODO:
- Make also available the private upload to your imgur account.
- Make the pymgur.py module installable.

## License
All the repository content is available under the MIT license, **except** for the Automator service which is property of Apple Inc. and the Imgur icon displayed on the notifications, property of Imgur LLC.
See [LICENSE.md][license] for details.

[imgur]: http://imgur.com/
[pync]: https://github.com/setem/pync
[imgsup]: http://imgur.com/help/uploading
[trmn]: https://github.com/alloy/terminal-notifier
[license]: https://raw.github.com/SamuAlfageme/Pymgur/master/LICENSE.md
