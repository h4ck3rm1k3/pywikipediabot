# -*- coding: utf-8 -*-
__version__='$Id: speedydeletion.py 9692 2011-10-30 15:03:29Z xqt $'
#
import re, sys, string
import wikipedia as pywikibot
from pywikibot import i18n
import config, pagegenerators, catlib
import replace
import xmlreader


from shove import Shove

mem_store = Shove()
file_store = Shove('file://mystore')


def main(*args):
    genFactory = pagegenerators.GeneratorFactory()
    # If xmlfilename is None, references will be loaded from the live wiki.
    xmlfilename = None
    user = None
    skip = False
    timestamp = None
    # read command line parameters
    for arg in pywikibot.handleArgs(*args):
        xmlfilename = arg

    print xmlfilename 

    importsite = "speedydeletion"

    outsite = pywikibot.getSite("en",importsite)
    outsite.forceLogin()

    mysite = pywikibot.getSite()
    dump = xmlreader.XmlDump(xmlfilename)
    count = 0
    for entry in dump.parse():
        if entry.title != "Main Page" :
            page = pywikibot.Page(mysite, entry.title)
#            pywikibot.output(u'Looking at %s' % entry.title)

            try :
                if (file_store[entry.title] ) :
                    count = count +1
                    #pywikibot.output(u'was cached %s' % entry.title)
            except:
                try :
                    outpage = pywikibot.Page(outsite, entry.title)
                    if outpage.exists():
                        pywikibot.output(u'is there at %s' % entry.title)
                    else:
                        pywikibot.output(u'is not there  %s' % entry.title)
                        contents = entry.text
                        usernames = entry.username
                        contents = contents +  "\n{{wikipedia-deleted|%s}}" % usernames
                        outpage.put(contents)
                    file_store[entry.title] = entry.title
                finally:
                    count = count + 1
            finally:
                count = count + 1
                #print "done with %s %d" % (entry.title, count)

if __name__ == "__main__":
    try:
        main()
    finally:
        pywikibot.stopme()
