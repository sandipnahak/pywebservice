#!/usr/bin/env bash
source version

docker build --force-rm --no-cache --network host --label sdpw -t $VERSION . | tee build.log

if [[ $? -eq 0 ]];then
    image_id=$(tail -n 2 build.log  | grep "Successfully built" | awk '{print $3}')
    docker tag $image_id docker.io/sandipnahak/sdpw:$VERSION
    docker push docker.io/sandipnahak/sdpw:$VERSION
    echo "Build is successful version: $VERSION"
fi


