#!/bin/bash
filename=$(basename "$1")
directory=$(dirname "$1")
extension="${filename##*.}"
filename="${filename%.*}"
HeatherAudioFilters="equalizer=f=112:width_type=h:width=200:g=18,equalizer=f=164:width_type=h:width=200:g=-5,equalizer=f=393:width_type=h:width=200:g=-3.4,equalizer=f=2540:width_type=h:width=200:g=-3.4,equalizer=f=8520:width_type=h:width=200:g=.7"
AJAudioFilters="-filter_complex equalizer=f=99:width_type=h:width=200:g=18,equalizer=f=148.5:width_type=h:width=200:g=-3.8,equalizer=f=433.7:width_type=h:width=200:g=-7.3,equalizer=f=2120:width_type=h:width=200:g=-5.2,equalizer=f=10810:width_type=h:width=200:g=2.6"
DaveyAudioFilters="-filter_complex equalizer=f=97:width_type=h:width=200:g=18,equalizer=f=137:width_type=h:width=200:g=-4.8,equalizer=f=460.4:width_type=h:width=200:g=-4.8,equalizer=f=2040:width_type=h:width=200:g=-4.6,equalizer=f=8190:width_type=h:width=200:g=1.7"
SoraidaAudioFilters="-filter_complex equalizer=f=98:width_type=h:width=200:g=18,equalizer=f=208:width_type=h:width=200:g=.5,equalizer=f=1710:width_type=h:width=200:g=-6.3,equalizer=f=6450:width_type=h:width=200:g=-5.4,equalizer=f=13180:width_type=h:width=200:g=-5.7"
EmmaAudioFilters="-filter_complex equalizer=f=112:width_type=h:width=200:g=18,equalizer=f=216:width_type=h:width=200:g=-2.8,equalizer=f=835:width_type=h:width=200:g=-3,equalizer=f=3350:width_type=h:width=200:g=-2.6,equalizer=f=13990:width_type=h:width=200:g=2.8"
LUFSOUT="-13"
sourceLUFS=$(ffmpeg -i "$1" -filter_complex ebur128 -f null - 2>&1 | grep -n '.*' | grep -A 5 "size" | grep "I:" | cut -d ':' -f3-)
LUFS=${sourceLUFS//[^0-9._-]/} 
echo $LUFS
LUFSNEG=$(echo $LUFS - $LUFSOUT | bc)
LUFSDIFF=$(echo $LUFSNEG | sed 's/-//g')
echo $LUFSDIFF
volume=',volume='$LUFSDIFF'dB:precision=float'
filters=$HeatherAudioFilters$volume
ffmpeg -y -i "$1" -vn -c:a libmp3lame -b:a 320k -af $filters "$directory"/"$filename".mp3
