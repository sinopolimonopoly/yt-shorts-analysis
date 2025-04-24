from channel_id_getter import get_channel_id
from uploads_playlist_getter import get_uploads_playlist_id
from playlist_to_vids import get_videos


handle = "curtisdoingthings"

channel_id = get_channel_id(handle)

channel_uploads_playlist = get_uploads_playlist_id(channel_id)

channel_videos = get_videos(channel_uploads_playlist, 10, 300)

for k, v in channel_videos:
    print(f'Video ID: {k} | {v}')