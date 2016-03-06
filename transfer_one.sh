
set -e
#python  ./pwb.py transferbot -lang:en -tolang:miraheze -tofamily:miraheze  -family:wikipedia "-cat:Linux" --debug
IFS=$'\n'
for x in `cat categories.txt`;
do echo $x;
   python  ./pwb.py transferbot -overwrite -lang:en -tolang:en -tofamily:speedydeletion  -family:wikipedia "-catr:$x"
   #python  ./pwb.py list -lang:en  -family:wikipedia "-catr:$x"
    
done
