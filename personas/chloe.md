# Chloe: AI creator persona

The AI face of the page: shows AI ads and how they're made. Openly AI, built by the account owner (credited in the bio).

## Identity (locked)
- **Higgsfield Element:** `Chloe`, character, made from the #11 portrait and Sheet B. Use it in every image and video prompt.
- **Look:** Nigerian woman, about 26, rich deep brown skin, clean clear skin, soft warm approachable expression with a gentle smile.
- **Hair:** long, glossy, jet-black bone-straight, sleek middle part.
- **Styling:** soft, feminine and simple. Fitted mock-necks, off-the-shoulder tops, satin slip dresses and midi skirts, neutral colours. Small gold hoops and a fine gold chain. **No blazer unless asked**; save blazers for announcements. Note: the saved Element's description still says "signature: ivory blazer", so always write "no blazer" into prompts.
- **Makeup rule:** always soft natural glam. Never heavy contour or dramatic lashes, which make her look intense or "scary".
- **Default background:** soft grey seamless studio, or a white marble desk with a grey wall.

## Voice (locked, updated Oct 2026)
- **Current voice: ElevenLabs clone `chloe2` (voice_id `PdIclR2uI4cufRKYnmbu`, tagged en-nigerian)**, cloned from the first Omni Flash living-room video (campaigns/chloe-tests/chloe-omni-voice-sample.wav). The user prefers this voice.
- **Approved method: the Voice Changer (ElevenLabs Speech to Speech, `eleven_multilingual_sts_v2`).** Generate the talking video in Omni Flash, extract its audio, run it through the Voice Changer with chloe2, and put the result back on the video at 0:00. It keeps Omni's exact timing, pacing and accent, so the lip-sync stays perfect, and only the voice changes. About 167 credits per 10 s. First result: campaigns/chloe-tests/library-chloe2-voicechanger-preview.mp4 (user: "very, very close").
- Text to speech with chloe2 plus a [Nigerian accent] tag (eleven_v3) came out higher-pitched and won't sync with an existing video; use it only for voiceovers with no on-screen lips.

## Voice (older)
- **Primary: ElevenLabs cloned voice `Chloe`** (voice_id `p8gH0uEJdvz76yHY6Qfp`, Nigerian English accent), in the user's own ElevenLabs account, generated through the ElevenLabs connector.
- **Model:** Multilingual v2 (approved take A1). v3 is the more expressive alternative.
- **Cost:** about 171 ElevenLabs credits for a 9-second line (about $0.03).
- **Into Higgsfield:** import the ElevenLabs result URL with Higgsfield URL import (the links expire after about 2 hours), then use it as `audio_references` in Seedance.
- **Old:** Higgsfield voice `Chloe-1` (Text to Speech v2, ElevenLabs variant). The user said its accent was lacking, so don't use it. Seed Audio was also rejected.
- **Tone:** warm, confident, friendly Lagos accent.

## Models
- **New looks or new people:** Soul Cinema, with no reference image. When given a reference image it ignored the written prompt.
- **Character sheets and edits:** Nano Banana Pro (Higgsfield sometimes routes to Nano Banana 2).
- **Video with Chloe:** Seedance 2.0 or Kling 3.0 with the Chloe Element. Kling needs a start image.

## Working rules
- Talking-video look (from the user's reference): Chloe waist-up holding a small wireless handheld mic with a fluffy grey windscreen near her chin in one hand, the free hand mostly still (see the hands rule below). Soft beige and blush luxury living room, warm light, heavily blurred. Clips of 10–15 seconds each, stitched in editing with B-roll of her ads and word-by-word captions with highlighted keywords. About 4.5 credits per second at 720p.
- Hands move only when needed: the free hand rests still by default, with at most one small, natural gesture where the line truly calls for it. No constant, choreographed or per-phrase gestures (user rule).
- **Performance:** plan every talking video with the waves-performance-director skill (beat map, then a word-anchored prompt). At most 2 purposeful gestures per 10 seconds, at chest height; never a blanket "hand stays still" (that removed her gestures in take 2).
- **Expression map (from the user's reference):** the face does the acting. Before each video, mark the script's beats and write them into the prompt:
  - a **smile** that comes with the words when the line deserves it (a punchline, good news, the offer);
  - a **slight head tilt** with a knowing look or a raised brow on a playful, cheeky or "be honest" line;
  - a **raised brow or small lean in** on a key number or promise;
  - a **neutral, sincere** face on straight information.
  Two or three beats per 10 seconds is enough. Don't smile through the whole clip. The reference was framed mid-torso, which is why the brief two-hand gestures stayed fully in frame.
- If a shot needs visible hands, frame her waist-up or mid-torso (a chest-up close-up crops them out). If movement still looks robotic, use motion transfer from a clip the user records themselves (never someone else's video).
- Seedance 2.0 at 720p (start image + approved voiceover as audio reference) worked well for the first talking test.
- Before any talking or voiceover video, share the voiceover link and wait for the user to approve it. Never generate the video first.
- Talking-video models: Wan 2.7 failed (low quality, delivered at 768x1344). Seedance 2.0 is the approved model (see the recipe below); 1080p costs double.
- Before any generation, state the number of variations and the credit cost, and wait for the user's yes.
- Keep Chloe clearly adult. Keep her styling professional, not sexualised.
- The bio must say she is AI and credit the creator.

## Approved talking-video recipe (first video, "So perfect")
1. Still: tight close-up, DJI mic with grey windscreen at chin, outfit #2, soft studio light (no ring light), blurred background. Start image job `4059d70b-f514-4b25-a56f-a73174bbd1ac`.
2. Voiceover: ElevenLabs `Chloe` on Multilingual v2. The user approves it before any video.
3. Video: Seedance 2.0, mode std, 720p, 9:16, duration = voiceover length rounded up (10s = 45 credits). Inputs: start_image + audio_references.
4. Prompt core: "talks directly to camera, lip-syncing exactly to the attached voiceover... free hand stays relaxed and still... moves only once, if natural... expression carries the delivery: warm, confident, easy smile, soft small nods, natural blinks. Camera static, framing exactly as in the start image, background softly blurred, soft studio light, no ring light."
5. Result: job `c378e57e-938b-4a72-9478-cec4c30008f3`.


## Gemini Omni Flash talking video (user: "even better than Seedance")
- Tool: Gemini app (Google AI Pro), Gemini Omni Flash, with the living-room DJI-mic still attached as the reference. Omni makes its own voice and lip-sync, so no ElevenLabs step is needed.
- Result: 1080x1920 (9:16), 24 fps, exactly 10.0 s, voice included. Saved as campaigns/chloe-tests/omni-flash-intro-10s.mp4.
- Prompt structure that worked: written as crew direction. Frame and camera (waist-up, locked-off), then look (blurred beige/blush living room, warm window light), then action (the line in quotes plus the Lagos accent, and expression cues anchored to words), then sound (voice only, close mic, room tone, no music), then text (no captions or on-screen text). "Duration: 10 seconds" plus "finishes speaking at about 9 s and holds a smile" fitted a 26-word line.
- Edit in the same chat to change one thing at a time (pace, accent, push-in).
- **Voice consistency in Omni (checked online, Oct 2026):** the Gemini app accepts only images and video (no audio files). Attaching a voice-only MP4 caused "Unable to edit the speech"; attaching the original living-room video with "create a brand-new video; the attached video is only a voice reference" worked and sounded close (median pitch 190 Hz vs 188 Hz original). But reports say uploaded audio references are not supported and reference-video audio is ignored in the current release, and a 1.1 update weakened voice continuity across clips. Treat the match as unreliable: test it over a few clips, and use a cloned voice plus a speech-to-speech voice changer when the voice must be exact.
- **Omni Flash captions fix:** naming "no subtitles, no captions, no on-screen text" in the prompt caused Omni to burn in subtitles. Leave that line out and write it positively instead: "Image: a clean, natural frame that shows only her and the room, exactly like a real creator's raw phone video before any editing." Introduce dialogue as "She speaks these words aloud (spoken dialogue only, heard not shown):". To fix an existing take, in the same chat: "Same video, keep everything exactly the same... Only remove the text at the bottom of the frame and fill that area with the clean background."
