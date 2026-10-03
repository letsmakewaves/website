# Templates

## One-take prompt (Seedance 2.0, Kling, Veo)

Write one of these for every part of at most 15 seconds. Fill every section and keep the labels.

```
TITLE: [BRAND] — [CONCEPT NAME] (PART 1 OF N)
DURATION: 15 seconds · ASPECT RATIO: [9:16 | 16:9]
STYLE: [Premium cinematic TV commercial | Social commercial | Raw UGC] · QUALITY: ultra-photorealistic, [grade, e.g. warm film grain]
REFERENCES: @CAST-1 is [role]. @CAST-2 is [role]. @PRODUCT-1 is [product] — preserve it exactly as the uploaded photo, no redesign.

SCENE FLOW:
0–3s: [shot type] — [who does what, where]. [camera move].
3–7s: ...
7–11s: ...
11–15s: [product hero or emotional payoff].

CAMERA: Continuous cinematic movement, smooth gimbal, slow push-ins, gentle orbit, 100mm macro for product. No abrupt cuts.
CONTINUITY LOCK: Keep @CAST-1's face, hair, wardrobe identical throughout. Keep @CAST-2 ... unchanged. Preserve @PRODUCT-1 exactly as the reference. Same location, lighting direction, colour grade from beginning to end.
AUDIO: [music]. [sound effects]. Voiceover, [female/male], [accent] accent, [tone], at [time]: "[line]". [more lines with timecodes]
AVOID: Text inside the shot, extra logos or products, changes to the product design, [lip movement if voiceover only], distorted hands.
```

**Attach list:** name each reference image in the order it should be attached, e.g.
- @PRODUCT-1: front photo, label readable
- @CAST-1: approved headshot of the mother
- @CAST-2: approved headshot of the daughter
- Logo on a plain background (optional)

## Storyboard sheet (one image, all frames, captions underneath)

```
A professional film storyboard sheet titled "[BRAND] — [CONCEPT]". [N] panels in a neat grid of [4 for 9:16 | 3 for 16:9] columns. Each panel is a [9:16 | 16:9] photorealistic cinematic still with a thin black border, a small dark header bar above it with the scene number and name, and one short line of caption text printed underneath it. Dark plum background, clean white sans-serif text, generous spacing. Spell every caption exactly as written.
Continuity: [continuity lock in one or two sentences, using the @tags]
Panel 1 — header "SCENE 1 · [NAME]". Image: [what we see]. Caption under the panel: "VO: [line]" | "Says: [line]" | "On screen: [text]" | "No voice"
Panel 2 — ...
Keep the same people, faces, wardrobe, product, location, lighting and colour grade in every panel.
```

Keep captions short, under about 12 words, so the image model spells them correctly.

**Text version for chat (9:16, 4 per row):**

| SCENE 1 · HOOK · 0–3s | SCENE 2 · LATHER · 3–6s | SCENE 3 · SCRUB · 6–9s | SCENE 4 · LOTION · 9–13s |
|---|---|---|---|
| She holds the wash up by her face | Lather spreads on her shoulder | Scrub rubbed into her arm | Lotion smoothed on, robe on |
| VO: "This is my everything shower." | VO: "Step one, a creamy wash." | No voice | VO: "Lock it in while damp." |
| On screen: everything shower | On screen: 1. cleanse | On screen: 2. exfoliate | On screen: 3. lock in |

## Product identity bible

```
@PRODUCT-1 — [PRODUCT NAME]
REFERENCE AUTHORITY: The supplied product photograph is the absolute reference. Never redesign it.
IDENTITY: [type of container, size, silhouette]
BODY: [main colour and finish]
CAP / CLOSURE: [colour, shape, pump or flip-top]
PRIMARY BRAND MARK: [logo colour, style and position]
LABEL: [key label text and where it sits]
DO NOT: [colours, finishes, text or props that must never appear]
```

## Cast bible

```
@CAST-1 — [ROLE]
LOOK: [age, skin tone, face, hair]
WARDROBE: [exact clothing and accessories]
SOURCE: [user headshot | cast for you: generate one approved headshot first]
```

## Shot-by-shot prompts

- **Image prompt (start frame):** one dense paragraph covering subject and @tag details, action, setting, lighting, lens and depth of field, colour grade, aspect ratio, and the product placed label-forward.
- **Video prompt:** motion and camera move only, 1–2 sentences, plus the clip length, e.g. "She smooths the lotion onto her daughter's hands as the camera slowly pushes in. 4 seconds."

## Worked example (summary)

The Johnson's Baby Lotion social commercial: 15s, 9:16, Seedance 2.0, Nigerian-accent voiceover. Cast was a mother (@CAST-1) and her daughter (@CAST-2) in the same white bath robe, with the bottle as @PRODUCT-1.

Scene flow:
1. The mother pumps lotion into her daughter's hands.
2. The daughter runs through a bright home in her robe.
3. They hug by the window.
4. Macro of the bottle's cap.
5. Hero shot of the bottle with "Love in Every Gentle Touch."

It was generated once with the logo, both headshots and the bottle attached.
