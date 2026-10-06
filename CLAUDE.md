# Project notes for Claude

## Image generation workflow (as of October 2026)

Images for videos are no longer generated in Higgsfield. The user has Google AI Pro
and makes stills with **Nano Banana Pro** (in the Gemini app) by hand.

How a new video's images get made:

1. Claude writes the image prompts, one per frame or shot. Do **not** call the
   Higgsfield MCP `generate_image` / `generate_image_batch` tools for stills.
2. The user pastes each prompt into Nano Banana Pro, generates, and picks the best take.
3. The user uploads the chosen images to this repo, where Claude picks them up.

Writing prompts for Nano Banana Pro:

- Write in plain descriptive prose (subject, setting, lighting, camera/lens, mood),
  not tag lists or keyword soup.
- State the aspect ratio in the prompt (16:9 for video frames unless told otherwise),
  and remind the user to set it in the tool too.
- For product shots, tell the user which reference images to attach (e.g.
  `puffer front view.jpg`, `puffer back view.jpg`) and say in the prompt that the
  product must match the reference exactly: colours, logo, panels, zips, cuffs.
- When a shot needs to stay consistent with an earlier frame, say which earlier
  image to attach as a reference.
- Put any on-image text in quotes in the prompt.
- Number the prompts so they line up with the shot list.

## Assets in the repo

- `puffer front view.jpg`, `puffer back view.jpg`: product reference shots of the
  yellow/black puffer jacket.
- `hf_*.png`: earlier 16:9 stills generated in Higgsfield.
