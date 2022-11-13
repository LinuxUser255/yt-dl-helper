#!/usr/bin/python3.9

import os

'''
Create a function that will open a text file urls.txt
and Execute yt-dlp on each line from urls.txt
'''

def open_urls_file() -> object:
    cmd = 'yt-dlp'
    filename = 'urls.txt'
    # Execute yt-dlp on each line from urls.txt
    with open(filename, 'r') as f:
        for line in f:
            os.system(cmd + '   ' + line)

            
open_urls_file()
