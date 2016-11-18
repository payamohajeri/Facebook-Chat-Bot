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

case "$1" in
    "install")
        install
        ;;
    "deploy")
        deploy
        ;;
    *)
        usage
        ;;
esac

exit 0