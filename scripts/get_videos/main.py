from channel_id_getter import get_channel_id
from uploads_playlist_getter import get_uploads_playlist_id
from playlist_to_vids import get_videos
from video_id_getter import get_video_ids
from video_info_getter import get_videos_info
from info_outputter import output_info


handle = "maxthemeatguy"
max_secs = 120

channel_id = get_channel_id(handle)

channel_uploads_playlist = get_uploads_playlist_id(channel_id)

video_ids = get_video_ids(channel_uploads_playlist, 50)

video_info = get_videos_info(video_ids, max_secs)

output_info(video_info, max_secs)
