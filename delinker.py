# Helper script for delinker and image_replacer

__version__ = '$Id: delinker.py 6540 2009-03-24 01:15:50Z nicdumz $'

import wikipedia, config

import sys, os
sys.path.insert(0, 'commonsdelinker')

module = 'delinker'
if len(sys.argv) > 1:
    if sys.argv[1] == 'replacer':
        del sys.argv[1]
        module = 'image_replacer'

bot = __import__(module)
bot.main()