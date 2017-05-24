#!/bin/bash
HOST='ftp.blufirestudios.com'  #This is the FTP servers host or IP address.
USER='studiestransfer@blufirestudios.com'            #This is the FTP user that has access to the server.
PASS=audiosw33t
filename=$(basename "$1")
directory=$(dirname "$1")
extension="${filename##*.}"
filename1="${filename%.*}"
NewName="$filename1""_FinalMix.wav"
recipient=nate@blufirestudios.com 
subject='New audio to be mixed'
body="This file: $filename has been uploaded to your ftp. When you're finished please name your file: $NewName"

ftp -i -n $HOST << EOF
user $USER $PASS
cd to_be_mixed
put $1
put $2
bye
clear
echo $1
echo $2
			
mail -s $subject, $recipient $body

return