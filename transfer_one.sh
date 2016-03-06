
#python  ./pwb.py transferbot -lang:en -tolang:miraheze -tofamily:miraheze  -family:wikipedia "-cat:Linux" --debug
for x in `cat ~/oel/data/allcats.txt`;
do echo $x;
    python  ./pwb.py transferbot -lang:en -tolang:en -tofamily:miraheze  -family:wikipedia "-cat:$x"
    exit
done
