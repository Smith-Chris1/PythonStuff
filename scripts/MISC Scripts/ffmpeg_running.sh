#!/bin/sh
SERVICE='ffmpeg'
 
if ps aux | grep $SERVICE
then
    echo "$SERVICE service running, everything is fine"
else
    echo "$SERVICE is not running"
    echo "$SERVICE is not running!"
fi