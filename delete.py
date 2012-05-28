# -*- coding: utf-8 -*-
"""
This script can be used to delete and undelete pages en masse.
Of course, you will need an admin account on the relevant wiki.

Syntax: python delete.py [-category categoryName]

Command line options:

-page:       Delete specified page
-cat:        Delete all pages in the given category.
-nosubcats:  Don't delete pages in the subcategories.
-links:      Delete all pages linked from a given page.
-file:       Delete all pages listed in a text file.
-ref:        Delete all pages referring from a given page.
-images:     Delete all images used on a given page.
-always:     Don't prompt to delete pages, just do it.
-summary:    Supply a custom edit summary.
-undelete:   Actually undelete pages instead of deleting.
             Obviously makes sense only with -page and -file.

Examples:

Delete everything in the category "To delete" without prompting.

    python delete.py -cat:"To delete" -always
"""
__version__ = '$Id: delete.py 9504 2011-09-04 11:49:02Z xqt $'
#
# Distributed under the terms of the MIT license.
#
import wikipedia as pywikibot
from pywikibot import i18n
import config, catlib
import pagegenerators

class DeletionRobot:
    """ This robot allows deletion of pages en masse. """

    def __init__(self, generator, summary, always = False, undelete=True):
        """ Arguments:
        * generator - A page generator.
        * always - Delete without prompting?

        """
        self.generator = generator
        self.summary = summary
        self.always = always
        self.undelete = undelete

    def run(self):
        """ Starts the robot's action. """
        #Loop through everything in the page generator and delete it.
        for page in self.generator:
            pywikibot.output(u'Processing page %s' % page.title())
            if self.undelete:
                page.undelete(self.summary, throttle = True)
            else:
                page.delete(self.summary, not self.always, throttle = True)

def main():
    pageName = ''
    singlePage = ''
    summary = ''
    always = False
    doSinglePage = False
    doCategory = False
    deleteSubcategories = True
    doRef = False
    doLinks = False
    doImages = False
    undelete = False
    fileName = ''
    gen = None

    # read command line parameters
    for arg in pywikibot.handleArgs():
        if arg == '-always':
            always = True
        elif arg.startswith('-file'):
            if len(arg) == len('-file'):
                fileName = pywikibot.input(
                    u'Enter name of file to delete pages from:')
            else:
                fileName = arg[len('-file:'):]
        elif arg.startswith('-summary'):
            if len(arg) == len('-summary'):
                summary = pywikibot.input(u'Enter a reason for the deletion:')
            else:
                summary = arg[len('-summary:'):]
        elif arg.startswith('-cat'):
            doCategory = True
            if len(arg) == len('-cat'):
                pageName = pywikibot.input(
                    u'Enter the category to delete from:')
            else:
                pageName = arg[len('-cat:'):]
        elif arg.startswith('-nosubcats'):
            deleteSubcategories = False
        elif arg.startswith('-links'):
            doLinks = True
            if len(arg) == len('-links'):
                pageName = pywikibot.input(u'Enter the page to delete from:')
            else:
                pageName = arg[len('-links:'):]
        elif arg.startswith('-ref'):
            doRef = True
            if len(arg) == len('-ref'):
                pageName = pywikibot.input(u'Enter the page to delete from:')
            else:
                pageName = arg[len('-ref:'):]
        elif arg.startswith('-page'):
            doSinglePage = True
            if len(arg) == len('-page'):
                pageName = pywikibot.input(u'Enter the page to delete:')
            else:
                pageName = arg[len('-page:'):]
        elif arg.startswith('-images'):
            doImages = True
            if len(arg) == len('-images'):
                pageName = pywikibot.input(
                    u'Enter the page with the images to delete:')
            else:
                pageName = arg[len('-images'):]
        elif arg.startswith('-undelete'):
            undelete = True

    mysite = pywikibot.getSite()
    if doSinglePage:
        if not summary:
            summary = pywikibot.input(u'Enter a reason for the %sdeletion:'
                                      % ['', 'un'][undelete])
        page = pywikibot.Page(mysite, pageName)
        gen = iter([page])
    elif doCategory:
        if not summary:
            summary = i18n.twtranslate(mysite, 'delete-from-category',
                                       {'page': pageName})
        ns = mysite.category_namespace()
        categoryPage = catlib.Category(mysite, ns + ':' + pageName)
        gen = pagegenerators.CategorizedPageGenerator(
            categoryPage, recurse=deleteSubcategories)
    elif doLinks:
        if not summary:
            summary = i18n.twtranslate(mysite, 'delete-linked-pages',
                                       {'page': pageName})
        pywikibot.setAction(summary)
        linksPage = pywikibot.Page(mysite, pageName)
        gen = pagegenerators.LinkedPageGenerator(linksPage)
    elif doRef:
        if not summary:
            summary = i18n.twtranslate(mysite, 'delete-referring-pages',
                                       {'page': pageName})
        refPage = pywikibot.Page(mysite, pageName)
        gen = pagegenerators.ReferringPageGenerator(refPage)
    elif fileName:
        if not summary:
            summary = i18n.twtranslate(mysite, 'delete-from-file')
        gen = pagegenerators.TextfilePageGenerator(fileName)
    elif doImages:
        if not summary:
            summary = i18n.twtranslate(mysite, 'delete-images',
                                       {'page': pageName})
        page = pywikibot.Page(mysite, pageName)
        gen = pagegenerators.ImagesPageGenerator(page)

    if gen:
        pywikibot.setAction(summary)
        # We are just deleting pages, so we have no need of using a preloading
        # page generator to actually get the text of those pages.
        bot = DeletionRobot(gen, summary, always, undelete)
        bot.run()
    else:
        pywikibot.showHelp(u'delete')

if __name__ == "__main__":
    try:
        main()
    finally:
        pywikibot.stopme()
