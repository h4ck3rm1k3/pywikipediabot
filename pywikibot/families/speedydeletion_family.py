# -*- coding: utf-8  -*-
"""Family module for Wikia."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id$'

from pywikibot import family
from pywikibot.tools import deprecated


# The Template Testing Wikia Search family
# user-config.py: usernames['wikia']['wikia'] = 'User name'
class Family(family.SingleSiteFamily, family.WikiaFamily):

    """Family class for speedydeletion Wikia."""

    name = u'speedydeletion'
    code = 'en'
    domain = 'speedydeletion.wikia.com'

    def __init__(self):
        """Constructor."""
        
        self.langs = {
            'en': u'speedydeletion.wikia.com',
        }
        
        self.languages_by_size = [
            'en', 'sv', 'nl', 'de', 'fr', 'ru', 'it', 'es', 
            'vi', 
            'war', 'ceb',
            'pl', 'ja', 'pt', 
            #'pt-br',  not supported yet
            'zh', 
            'uk', 'ca', 
            'no', 
            'fa',
            'fi',
            'id', 
            'ar',
            'cs', 
            'ko', 
            'ms', 
            'hu', 
            'ro', 
            'sr', 
            'tr', 
            'min', 
            'sh', 
            'kk', 
            'eo',
            'sk', 
            'eu', 
            'da', 
            'lt', 
            #'bg', 
            #'he', 
            'hr', 
            'sl', 
            #'uz', 'hy', 'et',
            #'vo', 'nn', 'gl', 'simple', 
            'hi',
            #'la', 
            'el', 
            #'az', 'th', 'oc',
            #'ka', 'mk', 'be', 
            'new', 
            #'tt', 'pms', 
            'tl', 
            #'ta', 'te', 'cy', 'lv',
            #'be-x-old', 'ht', 
            'ur', 
            #'ce', 'bs', 
            'sq', 
            #'br', 
            'jv', 
            #'mg', 
            'lb',
            #'mr', 'is', 
            'ml', 
            #'pnb', 'ba', 'af', 
            'my',
            #'zh-yue', 
            'bn', 
            #'ga',
            #'lmo', 
            'yo', 
            #'fy', 'an', 'cv', 
            'tg', 
            'ky', 
            'sw',
            #'ne', 'io', 'gu',
            #'bpy', 'sco', 
            'scn', 
            #'nds', 'ku', 'ast', 'qu', 'su', 'als', 
            'gd',
            # 'kn', 'am', 'ckb', 'ia', 
            'nap', 
            #'bug', 'bat-smg', 
            'wa', 
            #'map-bms',
            # 'mn', 
            'arz', 
            #'pa', 'mzn', 
            'si', 
            #'zh-min-nan', 
            'yi', 
            'sah', 
            'fo',
            # 'vec', 
            'sa',
            #'bar', 
            'nah', 
            #'os', 'roa-tara', 'pam', 'or', 'hsb',
            # 'se', 'li', 'mrj', 'mi', 'ilo', 
            'co',
            #'hif', 'bcl', 'gan', 'frr',
            'bo',
            #'rue', 'glk', 'mhr', 'nds-nl', 'fiu-vro', 'ps', 'tk', 'pag',
            # 'vls', 'gv', 'xmf', 
            'diq', 
            #'km', 'kv', 'zea', 'csb', 'crh', 'hak',
            # 'vep', 'sc', 'ay', 'dv', 
            'so', 
            #'zh-classical', 'nrm', 'rm', 'udm',
            # 'koi', 'kw', 
            'ug', 
            #'stq', 'lad', 'wuu', 'lij', 'eml', 'fur', 'mt',
            # 'bh', 'as', 
            'cbk-zam', 
            #'gn', 'pi', 'pcd', 'szl', 'gag', 'ksh',
            # 'nov', 'ang', 'ie', 'nv', 'ace', 'ext', 'frp', 'mwl', 'ln', 'sn',
            # 'lez', 'dsb', 'pfl', 'krc', 'haw', 'pdc', 'kab', 'xal', 'rw', 'myv',
            # 'to', 'arc', 'kl', 
            'bjn', 
            #'kbd', 
            'lo', 
            #'ha', 'pap', 'tpi', 'av',
            # 'lbe', 
            'mdf', 
            # 'jbo', 'na', 'wo', 'bxr', 'ty', 'srn', 'ig', 'nso',
            # 'kaa', 'kg', 'tet', 'ab', 'ltg', 'zu', 'za', 'cdo', 'tyv', 'chy',
            # 'tw', 'rmy', 'roa-rup', 'cu', 'tn', 'om', 'chr', 'got', 'bi', 'pih',
            # 'rn', 'sm', 'bm', 'ss', 'iu', 
            'sd', 
            #'pnt', 'ki', 'xh', 'ts', 'ee',
            # 'ak', 'ti', 'fj', 'lg', 'ks', 'ff', 'sg', 'ny', 've', 'cr', 'st',
            # 'dz', 'ik', 'tum', 'ch',

        ]
        super(Family, self).__init__()
        
        

    @deprecated('APISite.version()')
    def version(self, code):
        """Return the version for this family."""
        return "1.19.24"

    def scriptpath(self, code):
         """Return the script path for this family."""
         return ''

    def apipath(self, code):
         """Return the path to api.php for this family."""
         return '/api.php'

    # def protocol(self, code):
    #     return 'http'        
