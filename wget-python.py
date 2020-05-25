#!/usr/bin/env python
#Simple Python script to download files like wget

import urllib.request
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
import sys
import random

def color_text(text, level):
    # function to color text, log printed in shell 
    if level == 'err':
        print('\033[31m' + text + '\033[37m ')
    elif level == 'ok':
        print('\033[32m' + text + '\033[37m ')
    elif level == 'warn':
        print('\033[33m' + text + '\033[37m ')
def python_wget(url):
    # URL request
    try:
        response = urllib.request.urlopen(url)
    except URLError as e:
        color_text('Error while processing the URL.','err')
        color_text('Reason: ' + str(e.code) + '  ' + str(e.reason), 'err')
    except HTTPError as e:
        color_text('The server couldn\'t fulfill the request.', 'err')
        color_text('Error code: ', str(e.code) + '  ' + str(e.reason),'err')
    else:
        
        # every thing is fine
        content = response.read()
        # Parse the output file name from url
        name=urlparse(url).path.split('/')[-1]
        # if no name detected, use index.html
        if name =='':
            name="index.html"
        # create output file
        try:
            outputfile = open(name, "x")
        except FileExistsError:
            name=name+str(random.randint(1000, 9999))
            color_text("File exists, renaming it to " +name, 'warn') 
            outputfile = open(name, "x")
        # append content into it
        outputfile = open(name, "wb")
        outputfile.write(content)
        outputfile.close()
        color_text("File " + name + " downloaded successfully", 'ok')
def main():
    #check if url is provided
    try:
        url=sys.argv[1]
    except IndexError:
        #print ('\033[31m red \033[37m ')
        color_text("please specify the URL", "err")
        sys.exit(1)
    else:
        python_wget(url)

if __name__ == "__main__":
    main()
