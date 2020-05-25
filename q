#!/usr/bin/env python
#Simple Python script to download files like wget

import urllib.request
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
import sys
import random

def python_wget(url):
    # URL request
    try:
        response = urllib.request.urlopen(url)
    except URLError as e:
        print('Error while processing the URL.')
        print('Reason: ' + str(e.code) + '  ' + str(e.reason))
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', str(e.code) + '  ' + str(e.reason))
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
            print("File exists, renaming it to " +name) 
            outputfile = open(name, "x")
        # append content into it
        outputfile = open(name, "wb")
        outputfile.write(content)
        outputfile.close()
        print("File " + name + " downloaded successfully")
def main():
    #check if url is provided
    try:
        url=sys.argv[1]
    except IndexError:
        print('please specify the URL')
        sys.exit(1)
    else:
        python_wget(url)

if __name__ == "__main__":
    main()
