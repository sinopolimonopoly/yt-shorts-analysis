import yt_dlp
import os

def download_video(url, output_path="data/videos/"):

    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        'format' : 'best',
        'outtmpl' : f'{output_path}%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
    
    return ydl.prepare_filename(info)
