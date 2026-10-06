# Crown & Co. v2: video plan (edit path and motion prompts)

Deliverable: one **9:16 Reel/TikTok, about 25–30 seconds**, cut to music. Each look gets an emotional moment, not just a movement. The benchmark is the reference creator's collection video: full-body shots, big hair motion, and an emotional payoff.

## 1. The story (why people keep watching)

The video is a **feeling journey**. Every look is a different mood of the same woman, so viewers want to see the next one:

| # | Look | The emotion | The hair moment |
|---|---|---|---|
| 1 (hook) | 4: 30" honey blonde, glossy | **Release and joy**: she lets go | A huge slow-motion flip, the blonde fanning out like silk |
| 2 | 1: 30" bone straight, jet black | **Power**: "main character" | A 360° spin, the hair opening like a cape |
| 3 | 2: 26" deep body wave | **Swagger** | A runway walk at the camera, the waves bouncing every step |
| 4 | 3: 24" rose-pink body wave | **Soft and dreamy** | A turn and look back over the shoulder, the pink waves swinging round |
| 5 | 5: 22" kinky curly | **Pure happiness** | A spin that ends in a real laugh, the curls bouncing |
| 6 (finale) | Your favourite look | **Pride: she's wearing her crown** | Arms cross, chin lifts, a slow push-in |

## 2. The edit path (how the clips join)

| Time | Shot | What happens | Text on screen |
|---|---|---|---|
| 0.0–2.5s | **Hook: Look 4 flip** | Open mid-motion, the hair already flying. No slow start | "5 wigs. 1 crown." |
| 2.5–3.0s | Look 4 close-up (4B) | A fast punch-in on the glossy hair | `30" Honey Blonde` |
| 3.0–7.0s | **Look 1 spin** | **Spin transition:** cut while her back is to the camera, so she "spins into" the new wig | `30" Bone Straight` |
| 7.0–7.5s | 1B close-up | Punch-in, on the beat | — |
| 7.5–11.5s | **Look 2 walk** | She walks into the camera; cut when she nearly fills the frame | `26" Deep Body Wave` |
| 11.5–12.0s | 2B close-up | Punch-in | — |
| 12.0–16.0s | **Look 3 look-back** | Hair swinging round; cut on the smile | `24" Rose Pink` |
| 16.0–16.5s | 3B close-up | Punch-in | — |
| 16.5–21.0s | **Look 5 spin and laugh** | Cut right after the laugh | `22" Kinky Curly` |
| 21.0–21.5s | 5B close-up | Punch-in | — |
| 21.5–26.0s | **Finale** | Arms cross, slow push-in | "Crown & Co." / "Wear your crown." |

**Joining rules:**
- **Cut on movement,** never on stillness: the cut lands in the middle of a spin, flip or step, so the motion carries across.
- **Every cut lands on a music beat.** The B close-ups are the short "drum hits" between looks.
- **B close-ups cost nothing:** I animate them from the stills with a quick zoom in ffmpeg. No credits.
- Same light, backdrop and outfit in every shot, so the only thing changing is the hair.
- I join everything with ffmpeg: trim each clip, cut to the beat, add the text, mix the music with a fade at the end, and export 1080x1920. I check the size with ffprobe before sending it to you.

## 3. The motion prompts (Kling 3.0 Pro, start image = that look's A frame)

Every prompt ends with the same **lock line:**
> Same woman, same face, same wig, same black tee with "Crown & Co." in pink script on the left chest, same leggings, same charcoal studio backdrop as the start image. Photorealistic, natural hair physics, real weight and shine. No morphing, no extra people, no text changes.

**Look 4: the flip (hook)**
> Cinematic luxury hair commercial. She stands with her head tilted forward, her long glossy honey-blonde hair falling in front of her, eyes closed, a small breath of anticipation. Then, with a burst of joy, she throws her head back in one huge hair flip: the 30-inch blonde hair fans out in a wide, glossy arc in slow motion, every strand catching the light like liquid gold, then cascades down her back. She opens her eyes, looks straight into the camera and breaks into a free, radiant smile, as if she just fell in love with herself. A gentle wind keeps the hair moving. The camera pushes in slightly as the hair lands. Full body in frame. [lock line]

**Look 1: the spin**
> Cinematic luxury hair commercial. She stands tall facing the camera with a calm, powerful stare, then starts a slow, confident 360-degree spin. Her 30-inch jet-black bone-straight hair lifts and opens out around her like a silk cape, a perfect glossy sheet catching the light. As she comes back to face the camera, the hair swings round and settles perfectly straight down her back, and she lifts her chin with a knowing, main-character smile. Slow motion on the spin. The camera is locked off, full body in frame. [lock line]

**Look 2: the walk**
> Cinematic luxury hair commercial. She walks straight toward the camera in a confident runway stride, hips moving naturally, shoulders back. Her 26-inch jet-black deep body waves bounce and swing with every step, full and glossy, the waves catching the light. Halfway, she runs one hand through the side of her hair and the waves fall back perfectly. She stops close to the camera with a playful, self-assured smile and a slight raise of the brow. The camera tracks back slowly with her. [lock line]

**Look 3: the look-back**
> Cinematic luxury hair commercial, soft and dreamy. She stands with her back three-quarters to the camera, her 24-inch rose-pink body waves glowing softly. She slowly turns her head and shoulders to look back over her shoulder at the camera, and the pink waves swing round with her in slow motion, full, glossy and bouncing. Her face moves from a soft, faraway look to a gentle, warm smile as her eyes meet the camera, like she has just heard her name. A light breeze moves the hair. The camera is locked off, full body. [lock line]

**Look 5: the spin and laugh**
> Cinematic luxury hair commercial, full of joy. She does a playful 360-degree spin, her 22-inch natural-black kinky curls bouncing out with huge volume and springing back with every move. As she comes back to face the camera, she bursts into a real, happy laugh, touches the curls at the side of her face with her fingertips, and shakes them gently so they bounce. Pure happiness, carefree and alive. The camera is locked off, full body. [lock line]

**Finale: the crown moment**
> Cinematic luxury hair campaign finale. She stands square to the camera, knee-up, wearing the wig from the start image. She takes a slow breath, crosses her arms below her chest, lifts her chin and gives a slow, proud, confident smile, the look of a woman wearing her crown. The hair settles softly over her back. "Crown & Co." stays clearly visible on her left chest, above her arms. The camera pushes in slowly. Minimal motion. [lock line]

## 4. The plan for making it (test first)

1. **First test: Look 4, the flip** (the hook). If the hook doesn't stop the scroll, nothing else matters, and a flip is the hardest hair motion to get right. You upload **4A** (the start frame) and **4B** (to check the wig against it).
2. I check the result against the reference video: 9:16 size (ffprobe), full body, the hair motion, the face, the logo and the emotion.
3. Once it passes, we do the other 5 clips, one look at a time, with your approval each time.
4. I build the edit and send it to you before anything is final.

## 5. Cost (Higgsfield credits)

- Kling 3.0 Pro, 5 seconds: about **8.75 credits per take**.
- Test: 1 take of Look 4 = **8.75 credits** (or 2 takes = 17.5).
- Whole video: 6 clips × 1 take = **about 52.5 credits**. The B close-up zooms and the edit are free.
- Balance last checked: 1,744 credits.
