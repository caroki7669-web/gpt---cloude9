from PIL import Image, ImageDraw, ImageFont
import random, textwrap, os

W, H = 1080, 1920

def random_gradient(seed):
    random.seed(seed)
    c1 = tuple(random.randint(20, 80) for _ in range(3))
    c2 = tuple(random.randint(100, 200) for _ in range(3))
    img = Image.new("RGB", (W, H), c1)
    draw = ImageDraw.Draw(img)
    for y in range(H):
        ratio = y / H
        r = int(c1[0] + (c2[0]-c1[0])*ratio)
        g = int(c1[1] + (c2[1]-c1[1])*ratio)
        b = int(c1[2] + (c2[2]-c1[2])*ratio)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    return img

def make_scene_image(text, out_path, seed):
    img = random_gradient(seed)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    except:
        font = ImageFont.load_default()
    wrapped = textwrap.fill(text, width=22)
    bbox = draw.multiline_textbbox((0, 0), wrapped, font=font)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.multiline_text(((W-tw)/2, (H-th)/2), wrapped, font=font, fill="white", align="center")
    img.save(out_path)

def make_scenes(scenes, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    for i, text in enumerate(scenes):
        p = os.path.join(out_dir, f"scene_{i}.png")
        make_scene_image(text, p, seed=i)
        paths.append(p)
    return paths
