#!/bin/sh

CURRENT_DIR=$(cd $(dirname $0);pwd)
cat packageList.txt | sed -e '/^$/d' > tmp
mv tmp packageList.txt
project=$1
cd ~/$project
cat $CURRENT_DIR/packageList.txt | while read line
do
    infos=($line)
    package=${infos[0]}
    commit=${infos[1]}
    
    echo "deal with $package"
    mkdir $package
    cd $package

    cp $CURRENT_DIR/service_demo _service
    sed -i "s?your_url?git@gitee.com:src-openeuler/$package.git?" _service
    sed -i "s/commitID/$commit/" _service
        
    cd ..
    osc add $package
    #osc ci -m "init package"
done
osc ci -m "init package"
