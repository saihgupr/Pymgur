#!/usr/bin/env python

import os
from setuptools import setup, find_packages

terminal_notifier_files = []
for root, dirs, files in os.walk('pync/vendor/'):
    root = '/'.join(root.split('/')[1:])
    for f in files:
        terminal_notifier_files.append(os.path.join(root, f))

package_data = {
    '': ['LICENSE.md', 'README.md'] + terminal_notifier_files,
}

setup(name='Pymgur',
	version='0.8',
	description='A python script to upload images anonymously to imgur.com',
	author='Samuel Alfageme',
	author_email='Samuel.Alfageme@gmail.com',
	url='https://github.com/SamuAlfageme/Pymgur',
	download_url = 'https://github.com/downloads/SamuAlfageme/pymgur/pymgur-0.8.zip',
	license='MIT',
	platforms = "MacOS X",
	package_data = package_data,
	packages = find_packages(),
)