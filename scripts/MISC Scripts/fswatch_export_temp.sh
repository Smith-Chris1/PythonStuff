#fswatch -0 IsFile /Volumes/videos/\!export_temp | xargs -0 -n 1 -I {} /Users/chrissmith/Desktop/ffmpeg_720_360_encoder.sh {}
fswatch -0 -x --event IsFile Created /Volumes/videos/\!export_temp | xargs -0 -n 1 -I {} /Users/chrissmith/Desktop/ffmpeg_720_360_encoder.sh {}
