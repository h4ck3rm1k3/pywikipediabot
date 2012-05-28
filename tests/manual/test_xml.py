"""This is a minimal script to parse an XML file such as the sax_parse_bug.dat
dumps that interwiki.py can make if something fails. The only goal of this
program is to get a stack trace listing line number and column of the invalid
character in the XML.

Pass this script the name of an XML file as argument.
"""
#
# (C) Rob W.W. Hooft, 2003
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id: test_xml.py 9836 2012-01-21 13:46:03Z valhallasw $'
#
import sys, xml.sax, xml.sax.handler

h = xml.sax.handler.ContentHandler()
xml.sax.parse(open(sys.argv[1], 'r'), h)

