#!/usr/bin/env bash

VERSION=$(grep '^TASKS_VERSION =' gamedata/scripts/igi_generic_task.script | sed 's/TASKS_VERSION = "\(.*\)".*/\1/')
LASTCOMMIT=$(git log --oneline | head -n 1 | sed 's/\(.......\).*/\1/')
git tag $VERSION $LASTCOMMIT 
git push origin $VERSION

echo "Authorization: token $GITHUB_TOKEN"
curl \
    -X POST \
    -H "Accept: application/vnd.github.v3+json" \
    -H "Content-Type:application/json" \
    -H "Authorization: token $GITHUB_TOKEN" \
    https://api.github.com/repos/Igigog/Weird_Tasks_Framework/releases \
    -d "{\"tag_name\":\"$VERSION\"}" || exit

NAME="Weird_Tasks_Framework_$VERSION"
NAME_FULL="${NAME}_DEV"
cd .. && zip -r -q "Igi_Tasks/$NAME_FULL.zip" Igi_Tasks && cd -

mkdir ./"$NAME"
cp -r gamedata ./"$NAME"/gamedata
zip -r -q "$NAME.zip" "$NAME"
rm -r ./"$NAME"

./upload_asset.sh owner=Igigog repo=Weird_Tasks_Framework tag=$VERSION filename="$NAME.zip"
./upload_asset.sh owner=Igigog repo=Weird_Tasks_Framework tag=$VERSION filename="$NAME_FULL.zip"

rm ./"$NAME.zip"
rm ./"$NAME_FULL.zip"

echo DONE!
