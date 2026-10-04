# Performance library

## 1. Beat intents and default performance

| Intent | What the line does | Face | Head | Hands (only if needed) | Body |
|---|---|---|---|---|---|
| **Hook** | Opens, grabs attention | Direct, alert eyes, a slight brow lift | Still, square to camera | Rest | Upright, slightly forward |
| **Claim** | States something true or bold | Sincere, steady eye contact, lips relaxed | One small, firm nod at the end | Rest, or one small palm-down "settle" | Still |
| **Cheeky truth** | Calls the viewer out, gently | Knowing half-smile, one brow raised | Slight tilt to one side | Rest | Shoulders relax |
| **Number or promise** | "One minute a day", "30 days" | Brows lift, eyes widen a little | Slight lean toward camera | Small open palm at chest height, offering | Lean in a touch |
| **Instruction** | "Do this, then this" | Focused, a slight squint of concentration | Small nods on each step | One hand marks the step, small, at chest height | Still |
| **Empathy** | "I know it's hard" | Soft eyes, a small sympathetic smile, brows slightly up in the middle | Slow tilt | Hand lightly to chest | Shoulders soften |
| **Punchline** | The fun or surprising bit | Real smile that reaches the eyes, maybe a short laugh | Small head drop or tilt with the smile | Rest | A small bounce of the shoulders |
| **Offer** | "I'll show you how" | Warm, full smile | Small nod | Open palm toward camera at chest height | Slight lean in |
| **CTA** | "Comment PROMPTS" | Bright, inviting, eyebrows up | Slight nod toward camera | Optional small point down toward the caption area, only if it fits | Upright |
| **Neutral info** | Plain facts | Relaxed, pleasant neutral | Small natural drift | Rest | Still |

## 2. Expressions (name them precisely)

- **Relaxed neutral:** lips soft and closed or slightly parted, eyes calm. The home base between beats.
- **Sincere:** steady eye contact, brows level, a very slight smile at the corners.
- **Knowing half-smile:** one corner of the mouth up, eyes slightly narrowed, often with a brow raise.
- **Warm full smile:** cheeks lift, eyes crinkle (a "Duchenne" smile). Use it on good news and the offer, not throughout.
- **Brow raise:** both brows for surprise or emphasis; one brow for cheeky or sceptical.
- **Concerned or empathetic:** inner brows up, soft eyes, small closed smile.
- **Playful disbelief:** a small squint, lips pressed, a slight head shake.

## 3. Head movements

- **Tilt:** 10–15 degrees to one side for cheeky, empathetic or questioning lines.
- **Nod:** one small nod to confirm a point. Several nods only during an instruction list.
- **Lean in:** head and shoulders come a little closer to the lens on a number, a promise or a secret.
- **Shake:** a small side-to-side for "no", "don't do this", or disbelief.
- **Drift:** tiny natural head movements between beats. They stop the face looking frozen.

## 4. Hand gestures

Use them only on words that need them. Each one goes rest, then peak on the word, then back to rest.

| Gesture | Use it for | Height |
|---|---|---|
| **Open palm up (offering)** | An offer, a promise, "here's the thing" | Chest |
| **Open palm toward camera** | "I'll show you", "you can do this" | Chest |
| **Palm down, settling** | Calm, "simple", "that's it" | Waist to chest |
| **Hand to chest** | "I", "me", sincerity, empathy | Chest |
| **Small sweep to the side** | "Forget that", "next" | Chest |
| **Pinch or precise fingers** | A specific detail | Near the chin, inside the frame |
| **Both hands framing** | Size, "this much" (only when both hands are free) | Chest |

**Mic in one hand:** only the free hand gestures, and it stays at chest height or lower than the mic so it doesn't cover the face.

## 5. Body language

- **Posture:** upright, shoulders relaxed and down, not stiff.
- **Lean:** a small lean toward the camera on the most important line.
- **Breathing:** a small, visible breath before a big line makes her look alive.
- **Shoulders:** a little shrug for "it's that easy", a small bounce with a laugh.
- **Energy levels:**
  - Calm: slow moves, longer holds, smaller smiles.
  - Conversational: medium moves, quick settles (default).
  - Hype: bigger brows, faster nods, more smile. Still at most 2 gestures per 10 seconds.

## 6. Anti-patterns (ban them in the prompt when they appear)

- A gesture on every phrase (robotic, "TED talk hands")
- Counting on fingers, or pointing at the camera
- One fixed smile from start to finish
- Nodding on every line
- A frozen face or a stiff neck
- Hands rising from the bottom edge and getting cut off
- Over-blinking, or eyes darting off the lens
- Big theatrical brows or a mouth that over-articulates
- Writing "her hand stays still" as a blanket rule (the model removes all gestures)

## 7. Fix table

| Symptom | Fix in the next prompt |
|---|---|
| Looks robotic | Fewer gestures; add "settles back to relaxed neutral between beats"; add small head drift and natural blinks |
| No gestures at all | Name each gesture with its word and height, then "otherwise the hand rests" |
| Hand cut off at the frame edge | "at chest height, fully inside the frame", or use a wider start image (mid-torso or waist-up) |
| Same smile throughout | Map 2–4 different expressions to exact words, with neutral in between |
| Expression on the wrong words | Quote the exact words in the beat; shorten the beat |
| Too much movement | Lower the energy; cap at 2 gestures and 1 lean per 10 seconds |
| Face drifts to a different person | Add the lock line; keep the start image; lower motion intensity |
| Lip-sync off | Check the voiceover is attached as an audio reference; match the duration to the audio |

## 8. Prompt template

```
[NAME] talks directly to camera, lip-syncing exactly to the attached voiceover[, holding the PROP in one hand the whole time].
Her face does the acting, beat by beat:
On "[words of beat 1]," [face], [head].
On "[words of beat 2]," [face], [head][, her free hand GESTURE at chest height, fully inside the frame, then settles back].
On "[words of beat 3]," [face], [head], [body].
Between beats she settles back to a relaxed neutral, with natural blinks, small breathing movement and tiny head drift. Otherwise her free hand rests relaxed, out of the way.
Avoid: [anti-patterns for this shot].
Static camera, framing exactly as in the start image, [background and light]. Same face, hair, outfit and props as the start image throughout.
```

For **Kling** (no audio input), replace the first line with: "[NAME] speaks the line '[full script]' directly to camera" and generate with sound off, then lip-sync to the approved voiceover.

## 9. Worked example (Chloe, approved direction)

Script: "If you have a phone or a laptop, you shouldn't be broke. Give me just one minute a day for the next thirty days, and I'll show you how to become a paid AI content creator."

| Beat | Words | Intent | Face | Head | Hands | Body |
|---|---|---|---|---|---|---|
| 1 | If you have a phone or a laptop, | Hook | Sincere, steady eye contact | Square to camera | Rest | Upright |
| 2 | you shouldn't be broke. | Cheeky truth | Knowing half-smile, one brow raised | Slight tilt | Rest | Shoulders relax |
| 3 | Give me just one minute a day | Number or promise | Brows lift | Slight lean in | Small open palm at chest height | Lean in |
| 4 | for the next thirty days, | Neutral info | Engaged neutral | Small nod | Back to rest | Still |
| 5 | and I'll show you how to become a paid AI content creator. | Offer | Warm full smile that reaches her eyes | Small nod | Open palm toward camera at chest height, then rest | Slight lean in |
