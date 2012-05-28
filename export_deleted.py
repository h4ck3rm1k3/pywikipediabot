import wikipedia as pywikibot
import pagegenerators
import config
import catlib

import pagegenerators
site = pywikibot.getSite()
for x in ('Candidates_for_speedy_deletion_as_hoaxes',
          'Candidates_for_speedy_deletion_as_importance_or_significance_not_asserted',
          'Candidates_for_speedy_deletion_for_unspecified_reason') :
    cat = catlib.Category(site, x)
    pages = cat.articlesList(False)
    for Page in pagegenerators.PreloadingGenerator(pages,100):
        FILE = open("../PAGES/%s" % Page.urlname(),"w")
        text= Page.get()
        sutf8 = text.encode('UTF-8')
        FILE.write(sutf8)
        
