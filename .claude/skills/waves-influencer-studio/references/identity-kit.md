# Identity kit

## Identity bible

```
@INFLUENCER — [NAME]
Persona:        [niche] creator for [audience] on [platform]. Personality: [3 adjectives].
Age:            [e.g. 26, clearly adult]
Skin:           [tone in words, undertone, texture: e.g. deep brown, warm golden undertone, smooth with visible pores]
Face shape:     [oval / heart / square / round]
Eyes:           [shape, colour, spacing, lashes]
Brows:          [shape, thickness, arch]
Nose:           [bridge, tip, width]
Lips:           [fullness, shape, natural colour]
Jaw / chin:     [soft / defined, chin shape]
Marks:          [beauty mark position, freckles, dimples — or none]
Hair base:      [length, texture, colour, parting]
Body:           [height feel, build, proportions]
Signature:      [details in most content: e.g. thin gold hoops, nude almond nails]
Voice:          [tone, accent]
ALLOWED TO CHANGE: outfits, makeup intensity, hair styling within the base (sleek, curled, bun), locations, lighting
NEVER CHANGE:   face shape, eye shape and colour, nose, lips, skin tone, marks, body proportions, age
```

## Identity block (paste into every prompt, unchanged)

60–90 words, written once from the bible. For example:

> Amara, a 26-year-old Nigerian woman with deep brown skin with a warm golden undertone and natural texture, an oval face, almond-shaped dark brown eyes with long lashes, softly arched full brows, a straight nose with a rounded tip, full lips with a defined cupid's bow, a soft jawline, a small beauty mark above the left corner of her lips, sleek long jet-black hair with a centre part, slim athletic build, thin gold hoop earrings.

## Character sheet prompt

```
Character reference sheet of the same person, [identity block]. Plain light grey studio background, soft even front lighting, photorealistic, natural skin texture, consistent face in every view.
Row 1: front neutral headshot, three-quarter left, three-quarter right, left profile.
Row 2: full body front in a simple black fitted outfit, smiling, serious, laughing.
Thin white gutters between views, no text.
```

## Content prompt template

```
[identity block]
OUTFIT: [OUTFIT-n description]
LOCATION: [LOC-n description]
POSE / ACTION: [what she is doing, where she looks]
CAMERA: [shot size, angle, lens feel, aspect ratio]
LIGHT: [direction, quality, time of day]
STYLE: photorealistic, natural skin texture, [grade]
Keep her face, skin tone, marks and proportions exactly as the reference.
```

For video, add: `MOTION:` [one or two sentences, with the length] and `AUDIO:` [voice line with accent, or music only].

## 30-day calendar columns

| Day | Pillar | Format | Outfit | Location | Hook | Caption idea |
|---|---|---|---|---|---|---|

## Consistency check (run on every result)

Compare each new image with the approved sheet. It passes only if every answer is yes:

1. Same face shape and jawline?
2. Same eye shape, colour and spacing?
3. Same nose and lips?
4. Same skin tone and undertone, not lighter, darker or greyer?
5. Marks present and in the same place?
6. Same apparent age?
7. Body proportions consistent?
8. Hair within the allowed base?
9. Hands and fingers natural?
10. No stray text, logos or extra people?

Any "no" means regenerate that image. Tighten the prompt by repeating the failed trait, or reduce the outfit and location detail that's pulling the face off.
