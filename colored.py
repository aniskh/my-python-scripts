#!/usr/bin/env python3
"""
The aim of this module is to provide functions that colors output.
It is usefull for logs, stdout, ...

"""
# define colors
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Colorate log depending on info status: warn, err, ...
def logcol(text, level):
    # function to color text, log printed in shell 
    if level == 'err':
        print(style.RED + text + style.WHITE)
    elif level == 'ok':
        print(style.GREEN + text + style.WHITE)
    elif level == 'warn':
        print(style.YELLOW + text + style.WHITE)


