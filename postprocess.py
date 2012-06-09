

#bucket wikipedia-delete-2012-05
# algorithm 
#  get each wtarchive*.zip, get the list of articles first, check if there are any we need, then download them
url = "http://archive.org/download/wikipedia-delete-2012-05/wtarchive300512081506.zip/enwikipediaorg_w-20120530-wikidump/enwikipediaorg_w-20120530-titles.txt"
#http://ia601203.us.archive.org/zipview.php?zip=/24/items/wikipedia-delete-2012-05/wtarchive300512081506.zip&file=enwikipediaorg_w-20120530-wikidump/enwikipediaorg_w-20120530-titles.tx
conn = boto.connect_s3(host='s3.us.archive.org', is_secure=False)
buckets =conn.get_all_buckets()
for b in buckets:
#            print "compare %s and %s " % (b.name , bucket)
    #if re.search(r'wikipedia-delete-(\d\d\d\d)-(\d\d)',b.name):
    if re.search(r'wikipedia-delete-(\d\d\d\d)-(\d\d)',b.name):
        print "found %s" % b.name
    else:
        print "skip %s" % b.name

