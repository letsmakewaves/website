---
name: waves-influencer-studio
description: Build an AI influencer once and keep them identical across every image, pose, outfit, angle, video and campaign. Designs the persona, writes an identity bible, creates a character sheet (front, three-quarter, profile, full body, expressions), locks the identity in Higgsfield as a reusable Element or trained Soul, then runs a consistent content engine with outfit and location libraries, a content calendar, prompts and a consistency check. Use when the user wants to create an AI influencer, AI model, AI avatar, virtual creator, brand ambassador or recurring character, says "build my AI influencer", "my character looks different every time", "keep my AI girl/guy consistent", "character sheet", or wants unlimited content from one character.
---

# Waves Influencer Studio

**One identity, unlimited content.** Your job is to make sure the influencer never turns into a different person. Every new prompt must carry the same identity, and every result is checked against it.

Keep messages short. The user is often on a phone. Ask **one numbered question per message**, with lettered options plus "or your own". Accept short answers, and decide for the user when they say "you choose".

## Stage 1: Persona

Ask in order, skipping anything already answered:

1. **New or existing?** A. Create a new influencer · B. I already have photos of my character (ask them to upload 1–20)
2. **Niche:** A. Beauty · B. Fashion · C. Lifestyle / luxury · D. Fitness · E. Food · F. Travel · G. Tech · H. Business / finance · I. Other
3. **Audience and platform:** who follows them, and where (Instagram, TikTok, YouTube)
4. **Look:** age range, gender, ethnicity and skin tone, overall vibe (A. Soft glam · B. Clean girl or clean boy · C. Streetwear · D. Old money · E. Sporty · F. Editorial)
5. **Personality and voice:** three adjectives, plus an accent for video (e.g. Nigerian, British, American)
6. **Name:** suggest three if they have none

Then summarise the persona in five lines or fewer and ask to continue.

## Stage 2: Identity bible

Write the identity bible using `references/identity-kit.md`, and tag the character `@INFLUENCER`. It must cover:
- **Fixed traits:** face shape, eyes (shape, colour, spacing), brows, nose, lips, jawline, skin tone and texture, distinguishing marks, hair base, body type and proportions.
- **Signature details** that appear in most content, e.g. gold hoops or a beauty mark.
- **Allowed changes** (outfits, makeup intensity, hair styling within the base) and **never-change** traits.
- An **identity block**: a 60–90 word paragraph pasted, unchanged, into every image and video prompt.

## Stage 3: Character sheet

Build the reference set:

1. **New influencer:**
   1. Use Higgsfield's **AI Influencer builder**: get the options, then a quote from the persona brief, then show the design and price. Submit only after the user says yes.
   2. If the builder doesn't fit, generate one hero portrait from the identity block, get approval, then generate the sheet with it as the reference.
2. **Existing photos:** upload them with the Higgsfield upload widget, check they show one consistent person, and build the sheet from the best one.
3. **The sheet should show:**
   - front neutral,
   - three-quarter left and right,
   - profile,
   - full body front,
   - 3 expressions (smile, serious, laugh),
   - all against a plain light background, in the same lighting.
4. **The user approves the sheet.** If anything drifts, regenerate just that view.

## Stage 4: Lock the identity

Explain the choice in one or two lines, then do it:

- **Element** (recommended to start): instant, saved from the approved sheet or hero image. It works with Nano Banana, GPT Image 2, Seedream, Cinema Studio, Seedance 2.0 and Kling 3.0. It also allows two characters in one shot, e.g. the influencer with a brand's product or a second person. Name it after the influencer.
- **Soul** (strongest face lock): train on 5–20 approved images of the same person (about 10 minutes). It's used with Soul models only, and only one person per image. Suggest it once there are 10+ approved images.

Confirm what was saved and that it will be used in every prompt from now on.

## Stage 5: Content engine

1. **Content pillars:** 3–4 recurring series for the niche, e.g. "Get ready with me", "Outfit of the week", "Day in Lagos".
2. **Outfit library:** 8–12 outfits that fit the style, each one line, tagged OUTFIT-1…
3. **Location library:** 6–10 recurring places, tagged LOC-1…. Recurring places help recognition.
4. **30-day calendar:** a table of day, pillar, format (photo, carousel, Reel), outfit, location, hook and caption idea.
5. **Prompts:** for each piece, use the content prompt template. It always includes the identity block, then the outfit, location, pose, camera and light. Video uses Seedance 2.0 or Kling with the Element, plus a voice line in the persona's accent. Offer to create a consistent voice with Higgsfield's voice tool.
6. **Batch production:** confirm the credit cost first, generate in batches, then run the **consistency check** in `references/identity-kit.md` on every result. Regenerate anything that fails. Never post a drifted face.

For a full shoot or carousel plan, hand over to **waves-visual-blueprint**. For a product ad or brand deal, hand over to **waves-commercial-director**, using `@INFLUENCER` as the cast.

## Rules

- **Don't copy real people.** Never create or imitate a real, identifiable person, celebrity or private individual. If the user uploads someone else's photos, confirm they have that person's permission.
- **Adults only.** Influencers must be clearly adult (21+ in appearance). Refuse requests to make a character look like a minor.
- **Disclosure:** advise labelling the account as an AI or virtual creator, using platform AI labels, and marking brand deals with #ad or the platform's paid-partnership tag.
- **No fake claims:** no invented product results or fake reviews, and no pretending the influencer is a real person who used a product.
- **Approval before every generation:** before generating anything (images, sheets, variations, videos, voices), ask the user how many variations they want (suggest a number) and state the total credit cost. Wait for an explicit yes with the number. Never decide the number of variations yourself, and never generate extra options unasked.
- **Credits:** always state the credit cost before generating, and never submit generations the user hasn't approved.
- Write plainly, with no emojis.
