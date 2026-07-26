import os, asyncio
from generate_content import generate_unique as generate
from generate_visuals import make_scenes
from generate_audio import make_scene_audios
from build_video import build_long_video
from post_to_facebook import post_video as post_fb
from post_to_youtube import post_video as post_yt

def run():
    story = generate()
    title = story["title"]
    scenes = story["scenes"]

    img_paths = make_scenes(scenes, "output/images")
    audio_paths = asyncio.run(make_scene_audios(scenes, "output/audio"))

    final_path = "output/final.mp4"
    build_long_video(img_paths, audio_paths, "output/clips", final_path)

    full_text = " ".join(scenes)
    fb_description = f"{title}\n\n{full_text}"

    # يوتيوب بيحدد أقصى طول للوصف بـ5000 حرف
    yt_description = full_text[:4500]

    fb_result = post_fb(final_path, fb_description)
    print("فيسبوك:", fb_result)

    yt_result = post_yt(final_path, title, yt_description)
    print("يوتيوب:", yt_result)

if __name__ == "__main__":
    run()
