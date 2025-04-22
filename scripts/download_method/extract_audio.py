from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path, output_audio_path="data/audio/"):
    os.makedirs(output_audio_path, exist_ok=True)

    video_filename = os.path.basename(video_path)
    audio_filename = video_filename.replace(".mp4", ".wav")

    audio_path = os.path.join(output_audio_path, audio_filename)
    
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    return audio_path

if __name__ == "__main__":
    video_path = input("Enter the path to the video file:")
    audio_file = extract_audio(video_path)
    print(f"Audio extracted to: {audio_file}")


