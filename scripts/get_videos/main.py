from channel_id_getter import get_channel_id
from uploads_playlist_getter import get_uploads_playlist_id
from playlist_to_vids import get_videos
from video_id_getter import get_video_ids
from video_info_getter import get_videos_info


handle = "maxthemeatguy"

channel_id = get_channel_id(handle)

channel_uploads_playlist = get_uploads_playlist_id(channel_id)

video_ids = get_video_ids(channel_uploads_playlist, 5)

video_info = get_videos_info(video_ids)

print(f"{'Video ID':<15} {'Title':<80} {'Upload Date':<15} {'Duration':<13} {'View Count':<10} {'Like Count':<10} {'Comment Count':<10}")

for k, v in video_info.items():
    print(
            f"{k:<15} {v["Information"]["Title"]:<80} {v["Information"]["Upload Date"]:<15} {v["Information"]["Duration"]:<13} "
            f"{v["Statistics"]["View Count"]:<10} {v["Statistics"]["Like Count"]:<10} {v["Statistics"]["Comment Count"]:<10}"
          )    
# channel_videos = get_videos(channel_uploads_playlist, 5, 300)
"""
for k, v in channel_videos:
    print(f'Video ID: {k} | {v}')"""