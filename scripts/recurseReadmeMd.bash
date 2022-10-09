# Cat README.md under file folders.
# May easier to analyze similar components
# in order to avoid make duplicated wheels.
# 
# Author: Alex Rain at PLCT

#!env bash
pwd=`dirname $0`
if [ -x README.md ]; then mv README.md readme-orig.md; fi
for i in `find . -iname "README*"`
do
    echo "[$i]($i)" >> $pwd/README.md
    cat $pwd/$i >> $pwd/README.md
done
