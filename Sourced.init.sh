#!/bin/bash
# Author: patrickW
# Quick init like script for use with sourced.

COMMAND="${1}"
case "$COMMAND" in
    start )
        ./SourcedMain.py ${COMMAND} & ;;
    stop )
        ./SourcedMain.py ${COMMAND} & ;;
    restart )
        ./SourcedMain.py ${COMMAND} & ;;
    status )
        ./SourcedMain.py ${COMMAND} & ;;

    * )
        echo "USAGE: ./Sourced.init.sh COMMAND"
		echo "Valid commands are start, stop, restart, and status."
		;; 
esac
