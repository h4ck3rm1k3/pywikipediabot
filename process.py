import os
import glob
import re
import sys



path = '../wikiteamgit/data/'
for infile in glob.glob( os.path.join(path, '*') ):
#    print "current file is: " + infile
    match = re.search(r'(\d\d\d\d)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)',infile)
    match = re.search(r'w\-(\d+)\-wiki',infile)
#    match = re.search(r'.+(dddddddddddddd).+',infile)
#    match = re.search(r'.+(\dddddddddddddd).+',infile)
    if (match) :
        print "match %s" % match
        print "g1 %s" % match.group(1)
#        print "g0 %s" % match.group(0)
        ts=match.group(1)
        fn="enwikipediaorg_w-%s-wikidump/enwikipediaorg_w-%s-history.xml" % (ts, ts)
        cmd = "python speedydeletion.py ../wikiteamgit/data/%s" % fn
        print cmd
        stat=os.system(cmd)
        print stat
        if (stat >0) :
            sys.exit (stat)

        dn="enwikipediaorg_w-%s-wikidump/" % ts
        target= "../wikiteamgit/data/done/%s" % dn
        if not(os.path.exists(target)):
            cmd = "mv ../wikiteamgit/data/%s ../wikiteamgit/data/done/" % dn
            print cmd
            stat = os.system(cmd)
            print stat
            if (stat >0) :
                sys.exit(stat)
        else:
            cmd = "rm -rf ../wikiteamgit/data/%s" % dn
            print cmd
            stat = os.system(cmd)
            print stat
            if (stat >0) :
                sys.exit(stat)

        
    else:
        print "no match %s" % infile
