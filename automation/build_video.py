import subprocess, os

def build_scene_clip(image_path, audio_path, out_path):
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", image_path,
        "-i", audio_path,
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        out_path,
    ]
    subprocess.run(cmd, check=True)

def concat_clips(clip_paths, out_path, work_dir):
    list_file = os.path.join(work_dir, "concat_list.txt")
    with open(list_file, "w") as f:
        for p in clip_paths:
            f.write(f"file '{os.path.abspath(p)}'\n")
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", list_file,
        "-c", "copy",
        out_path,
    ]
    subprocess.run(cmd, check=True)

def build_long_video(image_paths, audio_paths, out_dir, final_path):
    os.makedirs(out_dir, exist_ok=True)
    clips = []
    for i, (img, aud) in enumerate(zip(image_paths, audio_paths)):
        clip_path = os.path.join(out_dir, f"clip_{i}.mp4")
        build_scene_clip(img, aud, clip_path)
        clips.append(clip_path)
    concat_clips(clips, final_path, out_dir)
