#!/bin/bash



for MP3_FILE in $(ls ./chords/mp3/*.mp3)
do
    FILENAME=${MP3_FILE:13}
    CHORD_NAME_IDX=$((${#FILENAME} - 4))
    CHORD_NAME=${FILENAME:0:CHORD_NAME_IDX}
    ffmpeg -i $MP3_FILE -vn -acodec pcm_s16le -ac 1 -ar 44100 -f wav ./chords/wav/${CHORD_NAME}.wav 
done