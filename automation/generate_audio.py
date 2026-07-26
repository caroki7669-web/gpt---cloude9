import asyncio, edge_tts, os

VOICE = "ar-EG-ShakirNeural"

async def make_audio(text, out_path):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(out_path)

async def make_scene_audios(scenes, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    for i, text in enumerate(scenes):
        p = os.path.join(out_dir, f"scene_{i}.mp3")
        await make_audio(text, p)
        paths.append(p)
    return paths
