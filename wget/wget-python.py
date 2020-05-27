#!/usr/bin/env python3
#Simple Python script to download files like wget

import urllib.request
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
import sys
import random
import colored

def python_wget(url):
    # URL request
    try:
        response = urllib.request.urlopen(url)
    except URLError as e:
        colored.logcol('Error while processing the URL.','err')
        colored.logcol('Reason: ' + str(e.code) + '  ' + str(e.reason), 'err')
    except HTTPError as e:
        colored.logcol('The server couldn\'t fulfill the request.', 'err')
        colored.logcol('Error code: ', str(e.code) + '  ' + str(e.reason),'err')
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
            colored.logcol("File exists, renaming it to " +name, 'warn') 
            outputfile = open(name, "x")
        # append content into it
        outputfile = open(name, "wb")
        outputfile.write(content)
        outputfile.close()
        colored.logcol("File " + name + " downloaded successfully", 'ok')
def main():
    #check if url is provided
    try:
        url=sys.argv[1]
    except IndexError:
        #print ('\033[31m red \033[37m ')
        colored.logcol("please specify the URL", "err")
        sys.exit(1)
    else:
        python_wget(url)

if __name__ == "__main__":
    main()
