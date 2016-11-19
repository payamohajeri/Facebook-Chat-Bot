#!/bin/bash

install() {
    heroku plugins:install heroku-redis
}

init() {
    git remote rm heroku
    heroku create
    install
    config
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

    echo "Configuring Facebook app access token"
    heroku config:add PAGE_ACCESS_TOKEN=$2

    echo "Configuring Facebook app verify token"
    heroku config:add VERIFY_TOKEN=$3

    echo "Configuring Production env"
    heroku config:add BOT_ENV="production"
}

removeapps() {
    for app in $(heroku apps); do heroku apps:destroy --app $app --confirm $app; done
}

logs() {
    heroku logs -t
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
    "enable:logs")
        logs
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