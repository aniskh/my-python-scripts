#!/usr/bin/env python
#Python script to just display the example part of ansible modules

import subprocess
import sys

def ans_example():
    #check if user mentionned module name
    try:
        args=sys.argv[1]
    except IndexError:
        print('please specify module name')
        sys.exit(1)
    command='ansible-doc'
    # run ansible-doc command
    text=subprocess.Popen([command, args], stdout=subprocess.PIPE)
    print('Module: ' + args)
    # retrieve Examples part
    documentation=str(text.stdout.read().decode('utf-8'))
    try:
        print(documentation.split('EXAMPLES:')[1])
    except IndexError:
        print('Could not retrieve module documentation')
        sys.exit(1)
def main():
    ans_example()

if __name__ == "__main__":
    main()
