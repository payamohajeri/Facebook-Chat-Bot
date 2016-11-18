#!/bin/bash

install() {
    echo "Install"
}

usage() {
    echo "Usage"
}

deploy() {
    git push heroku master
}

buildpack() {
    heroku buildpacks:set heroku/python
}

case "$1" in
    "install")
        install
        ;;
    "deploy")
        deploy
        ;;
    "set:buildpack")
        buildpack
        ;;
    *)
        usage
        ;;
esac

exit 0