The files in this folder were batch-normalized with the following script:

`for /f %f in ('dir /b .') do ffmpeg-normalize %f -ext ogg -c:a libopus`

`ffmpeg-normalize` is a Python script, found here: https://github.com/slhck/ffmpeg-normalize

The original files are preserved in case this process is non-ideal.