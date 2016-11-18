#!/bin/bash

install() {
    # for manuall install
    echo "Install"
    init
}

init() {
    git remote rm heroku
    heroku create
}

test() {
    heroku local
}

usage() {
    echo "Usage"
}

deploy() {
    echo "Be sure that you have commited all the changes ..."
    git push heroku master
}

buildpack() {
    heroku buildpacks:set heroku/python
}

config() {

    #Facebook app access token
    heroku config:add PAGE_ACCESS_TOKEN=$2

    #Facebook app verify token
    heroku config:add VERIFY_TOKEN=$3
}

removeapps() {
    for app in $(heroku apps); do heroku apps:destroy --app $app --confirm $app; done
}

case "$1" in
    "init")
        init
        ;;
    "test")
        test
        ;;
    "deploy")
        deploy
        ;;
    "set:buildpack")
        buildpack
        ;;
    "config")
        config
        ;;
    "removeapps")
        removeapps
        ;;
    *)
        usage
        ;;
esac

exit 0