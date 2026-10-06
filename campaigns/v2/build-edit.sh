#!/usr/bin/env bash
# Crown & Co. v2 Reel: trims the approved clips on the beat of music_A (136 bpm, beat 0.441s),
# adds the wig names, an end card and the music. Output: crown-and-co-v2-reel.mp4 (1080x1920).
set -euo pipefail
cd "$(dirname "$0")"
F=../brand/fonts/Cinzel-Bold.ttf
LOGO=../brand/logo-B-bold-caps-transparent.png
B=0.4412   # one beat
W="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1"
TXT="fontfile=$F:fontcolor=white:shadowcolor=black@0.6:shadowx=2:shadowy=2"
mkdir -p build
seg() { # name src start beats label [hook]
  local d; d=$(python3 -c "print(round($4*$B,3))")
  local vf="$W,drawtext=$TXT:fontsize=54:text='$5':box=1:boxcolor=black@0.35:boxborderw=18:x=(w-tw)/2:y=h*0.925:alpha='min(1,max(0,(t-0.25)/0.3))'"
  if [ "${6:-}" = hook ]; then
    vf="$vf,drawtext=$TXT:fontsize=86:text='5 WIGS. 1 CROWN.':x=(w-tw)/2:y=h*0.09:enable='lt(t,2.2)':alpha='min(1,(2.2-t)/0.3)'"
  fi
  ffmpeg -v error -y -ss "$3" -t "$d" -i "$2" -an -vf "$vf" -c:v libx264 -crf 17 -preset medium -pix_fmt yuv420p build/$1.mp4
}
seg 1 look5-curly.mp4     1.20 8 '22" KINKY CURLY' hook
seg 2 look1-straight.mp4  1.90 7 '30" BONE STRAIGHT'
seg 3 look2-bodywave-8s.mp4 0.80 8 '26" DEEP BODY WAVE'
seg 4 look3-pink.mp4      2.35 6 '24" ROSE PINK'
seg 5 look4-honey-5s.mp4  0.10 6 '30" HONEY BLONDE'
# end card: logo on black + tagline
ED=$(python3 -c "print(round(6*$B,3))")
ffmpeg -v error -y -f lavfi -i "color=c=0x0e0e0e:s=1080x1920:r=30:d=$ED" -loop 1 -t "$ED" -i "$LOGO" \
  -filter_complex "[1]scale=900:-1,format=rgba,fade=in:st=0:d=0.4:alpha=1[l];[0][l]overlay=(W-w)/2:(H-h)/2-120,drawtext=$TXT:fontsize=60:text='WEAR YOUR CROWN.':x=(w-tw)/2:y=h*0.66:alpha='min(1,max(0,(t-0.6)/0.4))',setsar=1" \
  -c:v libx264 -crf 17 -pix_fmt yuv420p build/6.mp4
printf "file '%s'\n" 1.mp4 2.mp4 3.mp4 4.mp4 5.mp4 6.mp4 > build/list.txt
ffmpeg -v error -y -f concat -safe 0 -i build/list.txt -c copy build/video.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 build/video.mp4)
FO=$(python3 -c "print(round($DUR-1.5,2))")
ffmpeg -v error -y -i build/video.mp4 -ss 0.33 -i ../music_A.mp3 -map 0:v -map 1:a -c:v copy \
  -af "afade=in:st=0:d=0.2,afade=out:st=$FO:d=1.5" -c:a aac -b:a 192k -shortest crown-and-co-v2-reel.mp4
ffprobe -v error -show_entries stream=codec_type,width,height:format=duration -of compact crown-and-co-v2-reel.mp4
