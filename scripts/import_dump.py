# -*- coding: utf-8 -*-
__version__='$Id$'
#
import re, sys, string
#import wikipedia as pywikibot
import pywikibot
from pywikibot import i18n
import  pywikibot.pagegenerators
#, pywikibot.catlib
#import replace
import pywikibot.xmlreader


from shove import Shove
file_store = Shove('file://wikiaupload')

import signal
import sys
# def signal_handler(signal, frame):
#         print 'You pressed Ctrl+C!'
#         sys.exit(0)
#         exit(0)
#         raise Exception("foo")
# signal.signal(signal.SIGINT, signal_handler)

import unicodedata

def decode(link) :
    b = link
    link = unicode(link, 'utf-8')
    link = unicodedata.normalize('NFKD', link)
    return strip(link)

def decodeuc(link) :
    b = link
    link = unicode(link)
    link = unicodedata.normalize('NFKD', link)
    return strip(link)


def strip(link) :
    b = link
    link = link.encode('ascii','ignore')
    return link


import subprocess    
import pprint

def main(*args):

    print "ARGS:%s\n" % sys.argv

    genFactory = pywikibot.pagegenerators.GeneratorFactory()
    # If xmlfilename is None, references will be loaded from the live wiki.
    xmlfilename = None
    user = None
    skip = False
    timestamp = None
    # read command line parameters
    local_args = pywikibot.handle_args(args)
    importsite = "speedydeletion"
    for x in local_args :
            if x.startswith("-site:"):
                    importsite = x[6:]
                    print ("Going to import into :" +importsite)
            elif x.startswith("-import:"):
                    xmlfilename = x[8:]

    insite = pywikibot.getSite("en","wikipedia")

    outsite = pywikibot.getSite("en",importsite)
    outsite.forceLogin()
   
    try :
        print "try to open %s\n" % xmlfilename
        with open(xmlfilename) as f: pass
    except :
        print "cannot open %s\n" % xmlfilename
        exit (0)

    dump = pywikibot.xmlreader.XmlDump(xmlfilename)
    count = 0
    
    for entry in dump.parse():
        title=entry.title.encode("utf8","ignore")
	title = decode(title)
        print ("Process" + title)
        outpage = pywikibot.Page(source=outsite, title=entry.title)
	exists =False
	exists = outpage.exists()
        contents = entry.text
        usernames = entry.username        
        outpage._site=outsite
	outpage.put(contents)
        count = count + 1

if __name__ == "__main__":
    try:
        main()
    finally:
        pywikibot.stopme()

##See also 
# http://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
