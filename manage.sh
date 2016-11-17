#!/bin/bash

install() {
    echo "Install"
}

usage() {
    echo "Usage"
}

case "$1" in
    "install")
        install
        ;;
    *)
        usage
        ;;
esac

exit 0