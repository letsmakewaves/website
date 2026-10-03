# Blueprint formats

## Scene card (one for every scene or frame)

```
SCENE 1 · ARRIVAL · 0–3s            (no time for photo series)
Action:       Walks through the Zara entrance, glancing up at the window display
Location:     Zara flagship entrance, glass doors, bright window displays
Wardrobe:     Beige fitted knit set, white trainers, gold hoops, tan shoulder bag
Props:        Shoulder bag, phone in hand
Positioning:  Talent left third walking right; doors and logo right third
Lighting:     Bright overcast daylight, soft shadows
Camera:       Full body, eye level, 35mm feel, slight tracking
Notes:        Logo can be soft; don't make it the focus
Says / VO:    "Spend the afternoon with me at Zara."   (video)
On screen:    zara day
IMAGE PROMPT: [one dense paragraph: @TALENT-1 details, action, location, wardrobe, props, positioning, lighting, lens, colour, aspect ratio]
VIDEO PROMPT: [motion and camera only, 1–2 sentences, with the length]   (video)
```

## Locked talent

```
@TALENT-1
Identity:  [age, skin tone, face, makeup]
Hair:      [style, colour]
Wardrobe:  [the outfit; list changes by scene if it changes]
Voice:     [tone, accent] (video)
Source:    [user photo | cast for you: generate one approved image first]
```

## Storyboard table (chat)

| SCENE 1 · ARRIVAL · 0–3s | SCENE 2 · BROWSING · 3–6s | SCENE 3 · OUTFIT PICK · 6–9s | SCENE 4 · FITTING ROOM · 9–12s |
|---|---|---|---|
| Walks in through the glass doors | Runs fingers along the rails | Holds two tops up to the mirror | Steps out, turns in the new outfit |
| Says: "Spend the afternoon with me." | VO: "First, the new arrivals." | No voice | VO: "And this is the one." |
| On screen: zara day | On screen: browsing | On screen: outfit selection | On screen: fitting room |

For a photo series, replace the voice row with the slide text, or leave it out.

## Storyboard sheet image (one image, all frames)

```
A professional storyboard sheet titled "[TITLE]". [N] panels in a neat grid of [4 for 9:16 or 4:5 | 3 for 16:9] columns. Each panel is a [ASPECT] photorealistic still with a thin black border, a small dark header bar above it with the scene number and name, and one short line of caption text printed underneath it. Dark plum background, clean white sans-serif text, generous spacing. Spell every caption exactly as written.
Continuity: [talent, wardrobe, location and grade lock, using @tags]
Panel 1 — header "SCENE 1 · [NAME]". Image: [what we see]. Caption under the panel: "[VO: line | Says: line | On screen: text | short description]"
Panel 2 — ...
Keep the same people, faces, wardrobe, location, lighting and colour grade in every panel.
```

Keep captions under about 12 words so the image model spells them correctly.
