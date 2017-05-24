#!/bin/sh
ps -ef | grep ffmpeg | grep -v grep
[ $?  -eq "0" ] && echo "process is running" || echo "process is not running"