# -*- coding: utf-8  -*-
"""Family module for Wikia."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id$'

from pywikibot import family
from pywikibot.tools import deprecated


# The Template Testing Wikia Search family
# user-config.py: usernames['wikia']['wikia'] = 'User name'
class Family(family.SingleSiteFamily):

    """Family class for templatetesting Wikia."""

    name = u'templatetestingwikia'
    domain = 'templatetesting.wikia.com'

    @deprecated('APISite.version()')
    def version(self, code):
        """Return the version for this family."""
        return "1.19.20"

    def scriptpath(self, code):
        """Return the script path for this family."""
        return ''

    def apipath(self, code):
        """Return the path to api.php for this family."""
        return '/api.php'
