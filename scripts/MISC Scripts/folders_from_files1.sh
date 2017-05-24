#!/bin/bash
set -x
project="/Volumes/videos/!Templates/Premiere Pro Templates/GenericTemplate/projectname/02_project/projectname.prproj"
input="/Users/chrissmith/Desktop/POD_VIDEOS_AWS/Scripts/OTE_Folders.csv"
destination="/Volumes/videos/Ads_Info/OTE/Texas"
file1="/Volumes/videos/!Templates/Premiere Pro Templates/GenericTemplate/projectname/01_assets/02_graphics/outroslate.mp4"
file2="/Volumes/videos/!Templates/Premiere Pro Templates/GenericTemplate/projectname/01_assets/02_graphics/SW_Interview_Intro_Music.mov"
file3="/Volumes/videos/!Templates/Premiere Pro Templates/GenericTemplate/projectname/01_assets/02_graphics/SW_VFT_Intro_Music.mov"
file4="/Volumes/videos/!Templates/Premiere Pro Templates/GenericTemplate/projectname/01_assets/02_graphics/01_Pictures/BUG.png"
file5="/Volumes/videos/!Templates/Premiere Pro Templates/GenericTemplate/projectname/01_assets/02_graphics/01_Pictures/Introslate.jpg"
file6="/Volumes/videos/!Templates/Premiere Pro Templates/GenericTemplate/projectname/01_assets/02_graphics/01_Pictures/outroslate_2016.psd"
OLDIFS=$IFS
IFS=,
while read folder
do
#    filename=$(basename "$f")
#    extension="${filename##*.}"
#    folder="${filename%.*}"
echo -e "Creating folders for: " "$folder"
    newname="/Volumes/videos/!Templates/Premiere Pro Templates/GenericTemplate/projectname/02_project/$folder.prproj"
    mkdir $destination/$folder
    mkdir $destination/$folder/01_assets
    mkdir $destination/$folder/01_assets/01_audio
    mkdir $destination/$folder/01_assets/01_audio/01_VO
    cp $f $destination/$folder/01_assets/01_audio/01_VO
    mkdir $destination/$folder/01_assets/01_audio/02_production
    mkdir $destination/$folder/01_assets/01_audio/03_music
    mkdir $destination/$folder/01_assets/01_audio/04_OMF
    mkdir $destination/$folder/01_assets/01_audio/05_final_mix
    mkdir $destination/$folder/01_assets/02_graphics
    mkdir $destination/$folder/01_assets/02_graphics/01_Pictures
    mkdir $destination/$folder/01_assets/02_graphics/02_render_replace
    cp $file1 $destination/$folder/01_assets/02_graphics
    cp $file2 $destination/$folder/01_assets/02_graphics
    cp $file3 $destination/$folder/01_assets/02_graphics
    cp $file4 $destination/$folder/01_assets/02_graphics/01_Pictures
    cp $file5 $destination/$folder/01_assets/02_graphics/01_Pictures
    cp $file6 $destination/$folder/01_assets/02_graphics/01_Pictures
    mkdir $destination/$folder/01_assets/03_video
    mkdir $destination/$folder/01_assets/03_video/01_A_Cam
    mkdir $destination/$folder/01_assets/03_video/02_B_Cam
    mkdir $destination/$folder/01_assets/03_video/03_B_Roll
    mkdir $destination/$folder/02_project
    cp $project $destination/$folder/02_project
    mv $destination/$folder/02_project/projectname.prproj $destination/$folder/02_project/$folder.prproj
    mkdir $destination/$folder/02_project/"Adobe Premiere Pro Auto-Save"
    mkdir $destination/$folder/02_project/"Adobe Premiere Pro Preview Files"
    mkdir $destination/$folder/03_final
    #echo $filename
 done
 IFS=$OLDIFS
 