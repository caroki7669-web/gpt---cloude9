import os, asyncio, random
from generate_content import generate_unique as generate
from generate_visuals import make_scenes
from generate_audio import make_scene_audios
from build_video import build_long_video
from post_to_facebook import post_video as post_fb
from post_to_youtube import post_video as post_yt

HASHTAGS = [
    "#قصص_واقعية", "#قصص_عربية", "#قصص_مصرية", "#قصص_عراقية",
    "#حكايات", "#قصة_قصيرة", "#شورتس", "#قصص_من_الحياة",
]

def build_short_description(title):
    tags = random.sample(HASHTAGS, k=5)
    return f"{title} 🎬\n\nقصة واقعية مؤثرة من الحياة العربية.\n\n{' '.join(tags)}"

def run():
    story = generate()
    title = story["title"]
    scenes = story["scenes"]

    img_paths = make_scenes(scenes, "output/images")
    audio_paths = asyncio.run(make_scene_audios(scenes, "output/audio"))

    final_path = "output/final.mp4"
    build_long_video(img_paths, audio_paths, "output/clips", final_path)

    description = build_short_description(title)

    fb_result = post_fb(final_path, description)
    print("فيسبوك:", fb_result)

    yt_result = post_yt(final_path, title, description)
    print("يوتيوب:", yt_result)

if __name__ == "__main__":
    run()
