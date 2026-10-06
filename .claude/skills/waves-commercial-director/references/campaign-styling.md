# Campaign styling

How to make a brand campaign look like a premium, cohesive campaign rather than a set of AI pictures. Learned from the reference creator's campaign work (wigs, jewellery, textiles, baby lotion, wellness tea, property). Use the brand's own name, logo and products, never hers.

## The 7 rules of a premium campaign

0. **Start from real product photos.** Every product in the campaign (each wig, bottle, piece of jewellery) needs a real reference photo from the user or brand, attached to every generation of that product. Text-only products look invented. This is what made the reference creator's wigs look real.
   - **If the user chooses to design the product with AI (no real photos):** write a detailed product spec into the prompt (for hair: grade, density, ends, lace, hairline, shine, colour, texture), generate the **close-up product frame first**, get it approved, and then attach that approved frame as the product reference for every other shot of that product. Never generate a wide shot of an unapproved product.

1. **One visual universe.** Every frame shares the same backdrop, light, colour grade, model and glam. Only the product changes.
2. **The product is the only variable.** Lock everything else: same model, same make-up, same wardrobe uniform, same set. For a collection, each look changes only the product (wig, necklace, outfit).
3. **The brand lives in the wardrobe or set, not in overlays.** For example, a fitted black tee or bodysuit with the brand logo on the chest, or brand-coloured set pieces. Text on screen stays minimal.
   - **Logo placement (lesson from the first test):** the logo only reads as centred when her body faces the camera square-on. In three-quarter turns it shifts to one side of the chest. Prompt it as "printed exactly in the horizontal centre of the tee, directly below the neckline, in line with her chin". Put any frame where the logo must read clearly in a square-on pose, with the hair behind the shoulders and the arms below the chest. In turned or profile poses, accept that the logo will be off-centre or hidden.
   - **Default placement (approved by the user):** a small logo in pink script on the left chest of a **plain tee with no pocket**. Never write "pocket" in a prompt; it makes the model add a pocket.
   - **LOCK THE BRANDING WITH AN IMAGE, NOT WORDS (hard rule).** Text descriptions make the model redraw the logo differently every time (font, size, colour, position), and frames drift off-brand. Once the user approves one branded frame, make **every other frame an edit of that exact image** (image reference plus "keep everything identical; ONLY change X"). For new poses, still attach the approved frame as a reference and say "the same tee and logo exactly as in the reference". Never generate a campaign frame from text alone after a brand frame is approved.
   - **Quality-check before showing the user.** Look at every frame against the approved frame: logo font, size, colour and position, the tee, backdrop and lighting. Regenerate off-brand frames before presenting them. If you can't view images, say so up front and send a small batch for the user to check, not the full set.
4. **Full coverage of each product:** a front beauty shot, a turn, the detail, the payoff. Viewers should understand length, texture, shape or fit without reading anything.
5. **Range in one go.** A collection shows variety (textures, colours, lengths, finishes) inside the same universe, so it reads as a range rather than random pictures.
6. **Beauty-level finish.** Clean, glowing skin with real texture; soft defined brows; lashes; nude or brown lip; neat hair edges. Polished, not plastic.
7. **A finale or hero frame:** a magazine-cover poster or a single hero portrait that could run as the ad on its own.

## The studio look (default for beauty, hair and fashion)

- **Backdrop:** a hand-painted, mottled grey or charcoal canvas (a classic portrait-studio backdrop), slightly darker at the edges.
- **Light:** a large soft key from the front-left, gentle fill, a subtle rim on the hair so texture and shine show. No hard shadows on the face.
- **Lens feel:** 85mm portrait, f/2.8, eye level or slightly below; vertical 4:5 or 9:16.
- **Grade:** neutral to cool shadows, warm, true skin tones, rich blacks.
- **Wardrobe uniform:** a fitted black short-sleeve tee or bodysuit (with the brand's logo if wanted), so nothing competes with the product.

### Alternative sets (pick one per campaign; don't mix)
| Set | Use for | Look |
|---|---|---|
| **Warm gold gradient** | A hero single for hair or beauty | Seamless gradient from gold to bronze, a white or ivory tank top, an over-the-shoulder glance |
| **Luxury boutique** | Jewellery, watches, accessories | Marble, mauve or lilac display cases, an ivory satin off-shoulder dress, warm practical lights, beauty dish, octabox highlights in frame |
| **Purple or coloured smoke studio** | Fabric, gowns, editorial fashion | Coloured smoky backdrop matching the fabric, full-length gown with a dramatic train, a magazine masthead |
| **Bright family home** | Baby care, home, wellness | Big arched windows, sheer curtains, cream knitwear, white bathrobes, soft morning light |
| **Luxury penthouse** | Real estate, lifestyle | Floor-to-ceiling city views at dusk, marble, a statement staircase, pendant lights; the presenter in bold printed fashion |

## Shot list per product (collection or hero)

For each look or product, 3–6 frames:
1. **Front beauty portrait:** chest-up, square to camera, calm confident face.
2. **Three-quarter turn:** body angled, face toward camera, one hand lifting or touching the hair or product.
3. **Profile or over-the-shoulder:** shows length, back, texture or the side detail.
4. **Full-length or knee-up:** for long lengths, gowns or full outfits (bare feet or simple heels, nothing distracting).
5. **Confidence pose:** arms crossed, or a hand at the collarbone or neck. For jewellery, the hand sits near the piece.
6. **Motion:** a hair flip, turn or walk (a video clip, or a slight motion blur in a still).

Plus for **jewellery or small products:** 2–3 macro details (on the skin, light catching stones, a ring on the hand at the collarbone).

## Campaign formats (the "format" question)

| Format | What it is | Structure |
|---|---|---|
| **Collection campaign** | Several products or looks shown as one cohesive premium collection | Same model, set and uniform; 3–5 frames per look (the shot list above); 4–8 looks; a final group or poster frame |
| **Hero product campaign** | One signature product given the full luxury treatment | Detail macros, then the product in use, then a beauty portrait, then the hero poster |
| **Transformation campaign** | Elevated before-to-after storytelling, with the finished product as the payoff | An honest "before" (plain, flat light), the process (applying, styling), the "after" in the studio look. No fake or medical claims |
| **Editorial campaign** | Fashion-forward, magazine energy | Striking poses and compositions, dramatic sets, a masthead or cover frame |
| **Lifestyle campaign** | The product inside an aspirational world | Interiors, fashion, accessories, elevated everyday moments; the product appears naturally |
| **Brand launch** | The official visual launch of a brand or new collection | Brand-coloured set, logo in the wardrobe or set, the hero frame, the range, the launch poster with the name and date |
| **Surprise me** | The director picks the strongest format and builds around it | — |

## The poster or magazine-cover frame

```
Vertical 4:5 luxury magazine-style ad for [BRAND]. The brand name "[BRAND]" in large elegant high-contrast serif capitals at the top, with "[CITY or TAGLINE]" in small spaced capitals beneath. A [model description] portrait framed by a thin gold rectangular border, on a soft white or cream satin background. The product line "[PRODUCT NAME]" in serif at the bottom with one short line of small text. Generous margins, premium and minimal.
```
Keep the words short and spell them exactly. Check the spelling in the result, because image models often misspell long text.

## Collection prompt template (studio look)

```
Premium hair/beauty campaign photo, vertical 4:5. [@TALENT-1 identity block]. She wears a fitted black short-sleeve tee[ with the "[BRAND]" logo in pink script on the chest]. Hand-painted mottled charcoal-grey canvas studio backdrop. Large soft key light from front-left, gentle fill, subtle hair rim light; 85mm portrait lens, f/2.8. Clean glowing skin with real texture, soft defined brows, lashes, nude-brown lip. PRODUCT: [exact product, e.g. 30-inch jet-black bone-straight wig with a natural middle part]. POSE: [one of the shot list]. Same model, same glam, same set and same lighting as the rest of the collection.
```
Change only the PRODUCT and POSE lines between frames.

## Video for campaigns

- **Plan the video first, then the stills (lesson from Crown & Co. v1, which looked boring next to the reference).** Before any still is generated, decide: (1) the video aspect ratio (9:16 for Reels and TikTok), (2) full-body framing for any hero motion, and (3) the motion per shot. Make the start frames for those shots in that ratio and framing.
- **Use big, product-showing motion, not small head turns.** For hair, fashion and apparel, a talking-head crop wastes the product. Use:
  - **360° spin:** she turns all the way around, slowly, and the hair or garment swings out and settles. Full body, camera locked.
  - **Walk toward the camera:** a confident runway walk from mid-ground to the camera, the hair bouncing with each step.
  - **Full hair flip or turn-and-look-back:** whole-body rotation with the hair whipping round.
  - **Fabric or hair in a breeze:** a wind machine with flowing movement, for a hero shot.
- **The reference's collection camera language (studied from her wig campaign):** each look is about 2 seconds, cut fast to music. Most shots **open chest-up on the face and the camera glides back to reveal the full length of the hair and the full body**; others orbit to profile, tilt down the length of the hair, or push in slowly. The model moves slowly and with control like a fashion model: eyes down then up to the lens, fingertips lifting or running down the hair, a slow turn to profile and a look back over the shoulder, hand on hip, a light breeze. The energy comes from the cutting, not big actions. Build these with Kling's **start image (the approved close-up) and end image (the full-body frame in a calm, finished pose)**, generate 5 seconds and trim to the best 2.5–3.5 seconds.
- **Start + end frame lesson (Crown & Co. v2, honey blonde test, rejected):** a waist-up start frame with a hand in the hair plus a full-body end frame in a different, mid-action pose (head tilted, eyes closed) made Kling rush to match the end pose: she shrank in frame, swung her arm awkwardly, the logo became unreadable and the clip ended on an odd head-tilt. Use an end frame only when it's a calm pose that follows naturally from the start pose, with a similar head and arm position. Otherwise use **the start frame only** and describe the camera pull-back in the prompt.
- **A full-body start frame needs the full outfit.** Lock the bottoms too (e.g. black fitted leggings or wide-leg trousers, bare feet or simple heels), so the outfit matches across clips.
- **Test one clip before running the set,** and compare it against the reference creator's motion and framing, not just against our own stills.

- **Make the stills in the video's aspect ratio from the start.** If the campaign will become a 9:16 Reel or TikTok, generate every still at 9:16, so the stills can be used directly as video start frames. (Lesson from the first test: 4:5 stills had to be stretched to 9:16.) Check the target video format before generating stills.
- **Kling with a start image keeps the start image's shape and ignores the aspect-ratio setting.** Always check the real width and height of the downloaded file (ffprobe), never the job metadata. If a clip comes out 4:5, centre-crop it to 9:16 for free (`crop=ih*9/16:ih`, then scale to 1080x1920), after checking that the face, product and logo sit inside the centre.

- 3–5 second slow-motion clips per look: a hair flip, a turn to camera, a hand through the hair, fabric moving, light catching jewellery.
- Cut to music in the same order as the collection. End on the poster frame.
- Keep motion simple and the camera mostly locked, with a slow push-in at most.

## Selling it (how she pitches it)

A campaign like this is a **service you can sell**. For a wig brand, for example: try-ons, hair transformations, product reels and campaign videos. Build one sample campaign per niche for the portfolio, then pitch brands in that niche.
