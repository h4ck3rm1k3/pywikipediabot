import os
import glob
import re
import sys
import signal
import sys

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)
#print 'Press Ctrl+C'
#signal.pause()


path = '../wikiteamgit/data/done'

for infile in glob.glob( os.path.join(path, '*') ):
    match = re.search(r'(\d\d\d\d)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)',infile)
    match = re.search(r'w\-(\d+)\-wiki',infile)
    if (match) :
        print "match %s" % match
        print "g1 %s" % match.group(1)
        ts=match.group(1)
        fn="enwikipediaorg_w-%s-wikidump/enwikipediaorg_w-%s-history.xml" % (ts, ts)
        cmd = "python speedydeletion_test.py ../wikiteamgit/data/done/%s" % fn
        print cmd
        stat=os.system(cmd)
        if (stat >0) :
            print "exiting"
            sys.exit (stat)

        dn="enwikipediaorg_w-%s-wikidump/" % ts
        cmd = "mv ../wikiteamgit/data/done/%s ../wikiteamgit/data/done2/" % dn
        print cmd
        stat = os.system(cmd)

        if (stat >0) :
            print "exiting"
            sys.exit(stat)
        
    else:
        print "no match %s" % infile
