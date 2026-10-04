# Chloe: AI creator persona

The AI face of the page: shows AI ads and how they're made. Openly AI, built by the account owner (credited in the bio).

## Identity (locked)
- **Higgsfield Element:** `Chloe`, character, made from the #11 portrait and Sheet B. Use it in every image and video prompt.
- **Look:** Nigerian woman, about 26, rich deep brown skin, clean clear skin, soft warm approachable expression with a gentle smile.
- **Hair:** long, glossy, jet-black bone-straight, sleek middle part.
- **Styling:** soft, feminine and simple. Fitted mock-necks, off-the-shoulder tops, satin slip dresses and midi skirts, neutral colours. Small gold hoops and a fine gold chain. **No blazer unless asked**; save blazers for announcements. Note: the saved Element's description still says "signature: ivory blazer", so always write "no blazer" into prompts.
- **Makeup rule:** always soft natural glam. Never heavy contour or dramatic lashes, which make her look intense or "scary".
- **Default background:** soft grey seamless studio, or a white marble desk with a grey wall.

## Voice (locked)
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

