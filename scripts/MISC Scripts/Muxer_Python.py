import os
indir = ' /Volumes/videos/videos/!muxer'
outdir = '/Volumes/videos/videos/!muxer/Completed/'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        if f.endswith(".mp4"):
            print f
            audio = f[:-17] + "_MIX.wav"
            if os.path.isfile(indir+"/"+audio):
                outName=outdir+f
                print(outName)
                #subprocess.Popen("ffmpeg -i %s -i %s -c:v copy -c:a libfdk_aac -b:a 320k -map 0:v -map 1:a %s" % tuple(map(pipes.quote, [f, audio, videoMatchSourceFileOut])),stdout=subprocess.PIPE,
                 #                   shell=True).communicate()[0]