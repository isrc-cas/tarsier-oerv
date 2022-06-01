#!/bin/sh

CURRENT_DIR=$(cd $(dirname $0);pwd)
cat packageList.txt | sed -e '/^$/d' > tmp
mv tmp packageList.txt
cd ~/
cat $CURRENT_DIR/packageList.txt | while read line
do
    infos=($line)
    package=${infos[0]}
    commit=${infos[1]}
    project=$1
    echo "deal with $package"
    osc co $project/$package
    cd $project/$package
    if [ ! -f "_service" ]; then
        cp $CURRENT_DIR/service_demo _service
        sed -i "s?your_url?git@gitee.com:src-openeuler/$package.git?" _service
        sed -i "s/commitID/$commit/" _service
        
        osc add _service
        osc ci -m "init package"
        cd ~/
    else
        echo "$package has _service"
    fi
done

