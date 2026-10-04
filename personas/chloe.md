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
- **Higgsfield voice:** `Chloe-1` (your own voice, not the built-in "Chloe" preset), cloned from the ElevenLabs Voice Design voice "Lagos Creator".
- **Engine:** Text to Speech v2 with the **ElevenLabs** variant. Don't use Seed Audio; the user rejected it.
- **Cost:** about 0.45 credits per short line, about 1.5 credits for 30 seconds.
- **Tone:** warm, confident, friendly Lagos accent.
- **Fallback:** the user generates in ElevenLabs (speed 100, stability 50, similarity 75), shares a Google Drive link set to "anyone with the link", and it's imported with Higgsfield's URL import.

## Models
- **New looks or new people:** Soul Cinema, with no reference image. When given a reference image it ignored the written prompt.
- **Character sheets and edits:** Nano Banana Pro (Higgsfield sometimes routes to Nano Banana 2).
- **Video with Chloe:** Seedance 2.0 or Kling 3.0 with the Chloe Element. Kling needs a start image.

## Working rules
- Talking-video look (from the user's reference): Chloe waist-up holding a small wireless handheld mic with a fluffy grey windscreen near her chin in one hand, the free hand gesturing (open palms, small sweeps, counting, pointing). Soft beige and blush luxury living room, warm light, heavily blurred. Clips of 10–15 seconds each, stitched in editing with B-roll of her ads and word-by-word captions with highlighted keywords. About 4.5 credits per second at 720p.
- Talking videos default to natural hand gestures. Frame her waist-up or mid-torso with her hands visible (a chest-up close-up crops the hands out). In the Seedance prompt, time each gesture to a phrase (small wave on the greeting, open palms, hand to chest, palms toward camera). If it still looks robotic, use motion transfer from a clip the user records themselves (never someone else's video).
- Seedance 2.0 at 720p (start image + approved voiceover as audio reference) worked well for the first talking test.
- Before any talking or voiceover video, share the voiceover link and wait for the user to approve it. Never generate the video first.
- Talking-video models: Wan 2.7 failed (low quality, delivered at 768x1344). Next to try: Seedance 2.0 (start image + audio reference), 720p about 40.5 credits or 1080p about 81 credits for 9 seconds.
- Before any generation, state the number of variations and the credit cost, and wait for the user's yes.
- Keep Chloe clearly adult. Keep her styling professional, not sexualised.
- The bio must say she is AI and credit the creator.
