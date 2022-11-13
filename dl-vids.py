#!/usr/bin/python3.9

import os

cmd = 'yt-dlp'
filename = 'urls.txt'
# Execute yt-dlp on each line from urls.txt
with open(filename, 'r') as f:
    for line in f:
        os.system(cmd + '   ' + line)
        
