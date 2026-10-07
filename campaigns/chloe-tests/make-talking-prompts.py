import re, sys
OUT=sys.argv[1]
# (setting name, background, light)
BG=[
("Luxury bedroom","an elegant bedroom with an upholstered cream headboard, white bedding, a warm bedside lamp and white roses","warm soft morning window light from the side"),
("Walk-in closet","a luxury walk-in closet with lit shelves of designer handbags and neatly hung neutral clothes","soft warm key light on her face, glowing shelf lights behind"),
("Marble kitchen","a modern kitchen with a white marble island, brushed gold fixtures and pendant lights","bright, airy daylight from large windows"),
("Hotel suite","a five-star hotel suite with floor-to-ceiling windows and a city skyline at golden hour","warm golden-hour light wrapping around her"),
("Home office","a stylish home office with a light oak desk, a laptop and built-in bookshelves","soft window daylight plus a warm desk lamp"),
("Vanity","a glamorous vanity with a large round mirror, perfume bottles and soft bulb lights","soft, flattering beauty light from the front"),
("Cafe","an upscale minimalist cafe with cream walls, a marble table and arched windows","natural soft daylight, cosy and warm"),
("Balcony","a luxury apartment balcony with glass railings, potted olive trees and a city view at sunset","warm sunset rim light on her hair, soft fill on her face"),
("Spa bathroom","a spa-like bathroom with beige stone walls, a freestanding tub, folded white towels and candles","soft diffused light, calm and clean"),
("Wig boutique","a luxury hair boutique with styled wigs on mannequin heads on lit shelves, blush walls and gold accents","bright, even boutique lighting with warm tones"),
("Luxury car","the inside of a luxury car with cream leather seats, parked, a soft city view through the window","soft daylight through the windshield"),
("Garden terrace","a garden terrace with white climbing roses, cream outdoor furniture and greenery","soft late-afternoon light, dreamy and warm"),
("Penthouse lounge","a penthouse lounge with a curved bouclé sofa, travertine coffee table and panoramic city windows","soft overcast daylight, elegant and calm"),
("Library","a private home library with dark wood shelves, leather armchairs and a brass reading lamp","warm lamp glow with soft window fill"),
("Beach villa","a beach villa terrace with white linen curtains and the ocean softly blurred behind","bright soft coastal daylight"),
("Yacht deck","the deck of a luxury yacht with white cushions and calm blue sea behind","clear midday sun softened by a canopy"),
("Private jet","a private jet cabin with cream leather seats and oval windows","soft daylight through the cabin windows"),
("Wine bar","an intimate wine bar with warm wood, glowing shelves of bottles and candlelight","warm, moody low light with a soft key on her face"),
("Rooftop lounge","a rooftop lounge at blue hour with string lights and a city skyline","cool blue-hour ambience with warm string-light glow"),
("Art gallery","a minimalist art gallery with white walls and large abstract canvases","clean gallery lighting, soft and even"),
("Flower shop","a luxury florist with buckets of peonies and roses and a marble counter","bright, fresh daylight"),
("Bakery","a chic patisserie with pastel macarons in a glass display and cream tiles","soft daylight, warm and inviting"),
("Hotel lobby","a grand hotel lobby with marble floors, a gold chandelier and velvet seating","warm, luxurious ambient light"),
("Dressing room","a backstage dressing room with a bulb-lit mirror and a rack of gowns","warm bulb light from the mirror"),
("Recording studio","a podcast studio with acoustic wall panels, a warm lamp and a plant","soft warm studio light, intimate"),
("Pilates studio","a bright boutique pilates studio with reformers and large windows","bright, clean morning light"),
("Living room at night","a cosy luxury living room at night with a lit fireplace and soft lamps","warm firelight and lamp glow"),
("Window seat","a window seat with plush cushions, sheer curtains and a rainy city view","soft grey rainy-day light, cosy"),
("Poolside","a luxury poolside cabana with white drapes and turquoise water","bright summer light, softened by the cabana"),
("Desert resort","a desert resort terrace with terracotta walls and palm shadows","warm late-afternoon desert light"),
("Lagos penthouse","a modern Lagos penthouse with floor-to-ceiling windows overlooking the lagoon at dusk","warm dusk light with soft city lights behind"),
("Paris apartment","a Parisian apartment with ornate white moulding, herringbone floors and tall windows","soft romantic daylight"),
("London townhouse","a London townhouse sitting room with sage-green walls and a marble fireplace","soft overcast daylight"),
("Dubai skyline","a high-rise apartment with a view of the Dubai skyline","bright, clean desert daylight"),
("Ski chalet","a luxury ski chalet with timber beams, sheepskin throws and snowy mountains outside","soft bright snow light with warm interior glow"),
("Lakeside cabin","a modern lakeside cabin with large glass windows and a calm lake","soft morning light over the water"),
("Conservatory","a glass conservatory filled with palms and white orchids","bright, diffused daylight"),
("Hair salon","a luxury hair salon with velvet chairs, gold mirrors and styling stations","bright, flattering salon light"),
("Nail lounge","a chic nail lounge with blush velvet chairs and marble tables","soft, even pastel light"),
("Jewellery store","a high-end jewellery store with lit glass display cases","bright, sparkling display light with a soft key on her face"),
("Bookstore cafe","a cosy bookstore cafe with stacked books and warm pendant lights","warm, inviting light"),
("Office lounge","a sleek corporate lounge with neutral sofas and glass walls","bright, clean daylight"),
("Boardroom","a modern boardroom with a long walnut table and city views","soft professional daylight"),
("Hotel bathroom","a luxury hotel bathroom with a backlit mirror and marble walls","soft backlit mirror glow"),
("Bedroom vanity at night","a bedroom vanity at night with a fairy-light mirror and candles","warm, soft evening light"),
("Breakfast nook","a sunlit breakfast nook with a round table, fresh flowers and a coffee pot","bright warm morning sun"),
("Courtyard","a Mediterranean courtyard with a stone fountain and bougainvillea","soft dappled sunlight"),
("Studio loft","an industrial-chic studio loft with exposed brick, large windows and plants","bright natural loft light"),
("Wardrobe styling room","a styling room with mood boards, a garment rail and a full-length mirror","soft, clean daylight"),
("Garden gazebo","a white garden gazebo with hanging wisteria","soft spring daylight"),
("Champagne bar","a luxury champagne bar with a gold counter and glass shelves","warm golden ambient light"),
("Theatre lobby","an elegant theatre lobby with red velvet and gold details","warm, rich ambient light"),
("Infinity pool","an infinity pool edge with the ocean at sunset behind","warm sunset glow"),
("Minimal studio","a clean minimal studio with a warm beige backdrop and a single plant","soft, even studio light"),
("Fashion showroom","a fashion showroom with neutral garments on rails and polished concrete floors","bright, even showroom light"),
("Rainy cafe window","a cafe window seat on a rainy evening with blurred city lights outside","moody warm interior light with cool city bokeh"),
("Bedroom balcony doors","a bedroom with open French doors leading to a sunny balcony","bright, airy morning light"),
("Luxury gym","a high-end gym lounge with dark wood, plants and soft lighting","soft, moody ambient light"),
("Hotel breakfast terrace","a hotel breakfast terrace with white tablecloths and a sea view","bright fresh morning light"),
("Velvet lounge","a lounge with an emerald velvet sofa and gold accents","warm, rich ambient light"),
("Tea room","an elegant tea room with porcelain cups and floral wallpaper","soft afternoon light"),
("Modern foyer","a modern home foyer with a sculptural staircase and a statement chandelier","soft, bright ambient light"),
]
WIGS=["30-inch jet-black bone-straight wig with a middle part","26-inch jet-black deep body wave wig with a deep side part","24-inch natural-black loose deep wave wig with a middle part","30-inch honey-blonde 613 straight wig, ultra-glossy, middle part","22-inch natural-black kinky curly wig with curtain bangs","24-inch rose-pink body wave wig with a middle part","14-inch jet-black sleek straight bob wig with blunt ends","28-inch dark-brown water wave wig with a middle part","26-inch jet-black kinky straight blow-out wig with a middle part","30-inch chocolate-brown body wave wig with honey-blonde highlights","22-inch jet-black layered blowout wig with bouncy curled ends","26-inch natural-black glossy loose wave wig with a side part","20-inch copper-auburn body wave wig with a middle part","18-inch jet-black deep curly wig with full volume","24-inch dark-brown straight wig with soft face-framing layers","16-inch jet-black wavy lob wig with a side part","28-inch ash-brown balayage loose wave wig","20-inch burgundy straight wig with a middle part","24-inch natural-black jerry curl wig","26-inch soft-black glossy straight wig with curtain bangs","22-inch caramel-brown loose curl wig","30-inch jet-black ultra-sleek straight wig with a side part"]
TOPS=["cream ribbed knit off-the-shoulder long-sleeve top","soft ivory cashmere V-neck sweater","white fitted square-neck long-sleeve top","champagne silk camisole with thin straps","light beige ribbed turtleneck","blush-pink off-the-shoulder ribbed knit top","oatmeal knit cardigan buttoned as a top, fine gold buttons","white one-shoulder ribbed knit top","taupe fitted scoop-neck long-sleeve bodysuit","cream cowl-neck satin blouse","camel ribbed knit polo-collar top with short sleeves","ivory off-the-shoulder cable-knit sweater","stone-coloured fitted crew-neck knit","white linen button-down shirt, top buttons open, sleeves rolled","dusty-rose silk wrap blouse","sand-beige ribbed tank top with a fine cream cardigan draped on her shoulders","soft grey cashmere crew-neck sweater","ivory satin square-neck top","mocha ribbed boat-neck top","cream knit halter-neck top","white puff-sleeve cotton blouse","beige fitted mock-neck long-sleeve top","pale pink cashmere off-the-shoulder sweater","chocolate-brown fitted ribbed long-sleeve top","champagne satin button-up shirt"]
JEW=["small gold huggie hoop earrings and a fine gold chain necklace","small diamond stud earrings and a thin diamond tennis necklace","gold knot stud earrings and a dainty gold pendant with a small pearl","delicate gold drop earrings and two layered fine gold chains","large sculptural gold hoop earrings, no necklace","pearl stud earrings and a single-strand pearl necklace","small gold dome earrings and a gold herringbone chain","diamond huggie earrings and a fine gold chain with a small diamond pendant","minimal gold bar earrings and a thin gold choker","pearl drop earrings, no necklace","chunky gold hoop earrings and a gold Cuban-link bracelet","rose-gold teardrop earrings and a fine rose-gold chain","emerald stud earrings and a thin gold chain","gold ear cuffs and a layered gold coin necklace","small silver hoops and a fine silver chain","diamond drop earrings and a delicate diamond bracelet","gold chandelier earrings, no necklace","tiny gold studs and a gold initial pendant"]
MIC="In one hand she holds a small black DJI wireless microphone transmitter with a fluffy grey windscreen at chest height; her other hand rests out of frame."
NOMIC=["Both hands relaxed in her lap below the frame; no microphone visible.","One hand lightly touching the ends of her hair at chest height, the other out of frame; no microphone visible.","One hand resting near her collarbone mid-gesture, natural and relaxed; no microphone visible.","Hands loosely clasped at her waist just below the frame edge; no microphone visible.","One hand holding a ceramic coffee cup at chest height, the other out of frame; no microphone visible.","One hand raised at chest height in a small, natural talking gesture, palm softly open; no microphone visible."]
TPL=("Use Image 1 as the identity reference: the same woman with exactly the same face, features, skin tone, brows and makeup as in Image 1. "
"Vertical 9:16 photorealistic still frame from a premium talking-head creator video. "
"FRAMING: waist-up, {pose}, eye level, centred, looking straight into the lens, lips slightly parted mid-sentence, warm and confident expression. "
"HAIR: {wig}; luxury raw human hair, full density, invisible HD lace with a natural hairline and soft baby hairs, glossy healthy shine, clean silhouette, no frizz or flyaways. "
"OUTFIT: {top}, fitted and simple. JEWELLERY: {jew}. HANDS: {hands} "
"BACKGROUND: {bg}, softly blurred with shallow depth of field so she stands out. LIGHT: {light}. "
"STYLE: soft natural glam makeup, nude-brown glossy lip, natural skin texture, 50mm full-frame lens at f/1.8, clean high-end creator look. "
"AVOID: text, captions, logos, watermarks, other people, visible ring lights, extra fingers, distorted hands.")
POSES=["seated","seated","standing","seated","standing"]
out=["CHLOE TALKING-HEAD BACKGROUNDS - 62 prompts (Nano Banana Pro)","Attach Image 1 every time: chloe-reference-livingroom.jpg (her face).","MIC = holding the DJI mic.  NO MIC = no microphone (use these for Omni Flash, which records her voice itself).",""]
risky=re.compile(r"\b(sexy|lingerie|bleach|scalp|teen|young girl|nude\b(?!-))",re.I)
seen=set()
for i,(name,bg,light) in enumerate(BG):
    mic = i<12 and True or (i%2==0)   # first 12 keep the mic; then alternate
    hands = MIC if mic else NOMIC[i%len(NOMIC)]
    wig=WIGS[(i*5)%len(WIGS)] if i>=12 else WIGS[i]
    top=TOPS[i%len(TOPS)]; jew=JEW[(i*7)%len(JEW)] if i>=12 else JEW[i]
    p=TPL.format(pose=POSES[i%len(POSES)],wig=wig,top=top,jew=jew,hands=hands,bg=bg,light=light)
    assert not risky.search(p), (i,risky.search(p))
    assert len(p)<1900, len(p)
    key=(wig,top,bg); assert key not in seen; seen.add(key)
    out.append(f"{i+1}. {name}  [{'MIC' if mic else 'NO MIC'}]")
    out.append(p); out.append("")
open(OUT,'w').write("\n".join(out))
print(len(BG), sum(1 for l in out if l.endswith('[MIC]')), sum(1 for l in out if l.endswith('[NO MIC]')))

# ---------- Lagos edition: braids + Lagos attire, mixed with the luxury looks ----------
BRAIDS=["waist-length black knotless box braids, neat square parts, middle part",
"Fulani braids: two cornrows framing the face into long braids, small gold braid cuffs and a few cowrie accents",
"long black goddess knotless braids with soft curly ends, middle part",
"bob-length black knotless braids, sleek and blunt at the chin",
"long boho knotless braids with loose curly strands throughout",
"neat black cornrows (all-back Ghana weaving) flowing into long braids",
"long black stitch braids with crisp straight-back parts",
"long honey-brown and black French curl braids",
"long black Senegalese twists, sleek and glossy",
"knotless braids swept into a high, elegant top knot with face-framing tendrils",
"long burgundy knotless box braids, middle part",
"long black passion twists, soft and full"]
BRAID_HAIR=("{b}; neat, uniform, tension-free braids with clean parts, smooth edges with softly laid baby hairs, "
"healthy glossy finish, no frizz or flyaways")
LAGOS_TOPS=["an off-shoulder top in vibrant Ankara wax-print fabric (orange, teal and gold pattern), tailored and fitted",
"a fitted aso-oke blouse in rich champagne-gold handwoven fabric with a structured off-shoulder neckline",
"an indigo adire tie-dye blouse with a soft square neckline",
"an ivory Nigerian lace blouse with delicate beading and scalloped edges",
"an emerald-green embroidered bubu kaftan with gold detailing at the neckline",
"a fitted Ankara corset top in a bold geometric print (mustard, black and white)",
"a coral-pink aso-oke off-shoulder blouse with puffed sleeves",
"a royal-blue adire two-piece top with a wide square neckline",
"a white Nigerian lace off-shoulder top with sequinned detailing",
"a burnt-orange and cream Ankara wrap top tied at the waist",
"a deep plum aso-oke fitted blouse with a sculpted sweetheart neckline",
"a soft cream embroidered kaftan with gold thread work"]
LAGOS_JEW=["coral bead statement necklace and gold drop earrings","layered gold necklaces with a small cowrie pendant and gold hoops",
"chunky gold statement earrings shaped like a fan, no necklace","coral and gold bead bracelet and small gold studs",
"gold collar necklace and gold teardrop earrings","brass cuff earrings and a stack of thin gold bangles"]
LAGOS_BG=[("Lekki penthouse","a Lekki penthouse living room with cream sofas, African contemporary art and floor-to-ceiling windows over the Lagos skyline","warm late-afternoon light"),
("Ikoyi living room","an elegant Ikoyi living room with carved wooden accents, woven Aso-oke cushions and potted palms","soft natural daylight"),
("Victoria Island rooftop","a Victoria Island rooftop terrace at sunset with the city lights coming on","warm golden sunset light"),
("Lagos beach club","a luxury Lagos beach club cabana with cream drapes and the Atlantic softly blurred behind","bright soft coastal light"),
("Textile art gallery","a Lagos art gallery with large adire and Ankara textile artworks on white walls","clean, soft gallery light"),
("Fashion atelier","a Lagos fashion designer's atelier with rolls of Ankara and aso-oke fabric, a dress form and a cutting table","bright, warm studio light"),
("Lagos cafe","a stylish Lagos cafe with rattan chairs, green plants and terrazzo tables","soft warm daylight"),
("Ikoyi garden","a lush Ikoyi garden with bougainvillea, palms and a cream garden bench","soft dappled afternoon light"),
("Lagoon view","a modern apartment with a large window overlooking the Lagos lagoon at dusk","warm dusk light with soft city glow"),
("Afrobeats studio","a music studio lounge with warm wood panels, a vinyl wall and soft lamps","warm, moody studio light"),
("Eko Atlantic skyline","a glass-walled high-rise lounge with the Eko Atlantic skyline behind","bright, clean daylight"),
("Owambe lounge","an elegant event lounge with gold chairs, white florals and soft fairy lights","warm, festive ambient light"),
("Hotel suite Lagos","a five-star Lagos hotel suite with cream linens and a city view","soft warm window light"),
("Boutique concept store","a Lagos concept store with curated African designer pieces on rails and woven baskets","bright, warm boutique light")]
start=len(BG)
lagos=[]
k=0
for i in range(40):
    mode = ["braids+lagos","braids+modern","wig+lagos"][i%3]
    name,bg,light = LAGOS_BG[i%len(LAGOS_BG)] if i<len(LAGOS_BG) else (BG[(i*7)%len(BG)])
    if mode.startswith("braids"):
        hair = BRAID_HAIR.format(b=BRAIDS[(i*5)%len(BRAIDS)])
    else:
        hair = WIGS[(i*3)%len(WIGS)] + "; luxury raw human hair, full density, invisible HD lace with a natural hairline and soft baby hairs, glossy healthy shine, clean silhouette, no frizz or flyaways"
    if mode.endswith("lagos"):
        top = LAGOS_TOPS[(i*7)%len(LAGOS_TOPS)]; jew = LAGOS_JEW[i%len(LAGOS_JEW)]
    else:
        top = TOPS[(i*11)%len(TOPS)] + ", fitted and simple"; jew = JEW[(i*5)%len(JEW)]
    mic = (i%2==1)
    hands = MIC if mic else NOMIC[i%len(NOMIC)]
    p=(TPL.replace("HAIR: {wig}; luxury raw human hair, full density, invisible HD lace with a natural hairline and soft baby hairs, glossy healthy shine, clean silhouette, no frizz or flyaways. ","HAIR: {wig}. ")
         .replace("OUTFIT: {top}, fitted and simple.","OUTFIT: {top}.")
         .format(pose=POSES[i%len(POSES)],wig=hair,top=top,jew=jew,hands=hands,bg=bg,light=light))
    assert not risky.search(p),(i,risky.search(p)); assert len(p)<2100,len(p)
    key=(hair,top,bg); assert key not in seen,(i,key); seen.add(key)
    lagos.append(f"{start+i+1}. {name}  [{'MIC' if mic else 'NO MIC'}]  ({mode.replace('+',' + ')})")
    lagos.append(p); lagos.append("")
txt=open(OUT).read().rstrip()+"\n\n=== LAGOS EDITION: braids, Lagos attire and the mix ===\n\n"+"\n".join(lagos)
open(OUT,'w').write(txt)
print("lagos", len(lagos)//3)
