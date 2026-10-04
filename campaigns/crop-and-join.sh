#!/usr/bin/env bash
# Crop Kling 4:5 clips to a true 9:16 (1080x1920) and join them in order.
# Usage: campaigns/crop-and-join.sh out.mp4 clip1.mp4 clip2.mp4 ...
set -euo pipefail
out=$1; shift
tmp=$(mktemp -d); list="$tmp/list.txt"; : > "$list"; i=0
for f in "$@"; do
  i=$((i+1))
  ffmpeg -loglevel error -y -i "$f" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920:flags=lanczos,fps=30" \
    -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p -an "$tmp/$i.mp4"
  echo "file '$tmp/$i.mp4'" >> "$list"
done
ffmpeg -loglevel error -y -f concat -safe 0 -i "$list" -c copy "$out"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height:format=duration -of compact "$out"
