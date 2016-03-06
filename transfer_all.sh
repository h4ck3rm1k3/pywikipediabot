#python  ./pwb.py transferbot -lang:en -tolang:miraheze -tofamily:miraheze  -family:wikipedia "-cat:Linux" --debug
set -e
exec <~/oel/data/allcats.txt
while read x
do echo "$x";
   python  ./pwb.py transferbot -lang:en -tolang:miraheze -tofamily:miraheze  -family:wikipedia "-cat:$x"
   if [ $? -ne 0 ]
   then
       exit
   fi
done
