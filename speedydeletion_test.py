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


file_store = Shove('file://mystore_update')


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
    dump = xmlreader.XmlDump(xmlfilename) #, allrevisions=True
    count = 0
    for entry in dump.parse():

        print entry.username
#        print entry.revisionid

        if entry.title != "Main Page" :
            page = pywikibot.Page(mysite, entry.title)


            try :
                if (file_store[entry.title] ) :
                    pywikibot.output(u'skipping at %s' % entry.title)
                    count = count +1                    
            except:
                try :
                    pywikibot.output(u'updating %s' % entry.title)
                    outpage = pywikibot.Page(outsite, entry.title)
                    get  = page.get()
                    contents = entry.text
                    usernames = entry.username
                    print ("http://%s%s" % ( outpage.site().hostname(),        outpage.site().nice_get_address(outpage.title())        ))
                    contents = contents +  "\n{{wikipedia-deleted|%s}}" % usernames
                    status = outpage.put(contents, "adding the username %s" % usernames)
                    file_store[entry.title] = entry.title
                finally:
                    count = count + 1
            finally:
                count = count + 1
                print "done with %s %d" % (entry.title, count)
                
if __name__ == "__main__":
    try:
        main()
    finally:
        pywikibot.stopme()
