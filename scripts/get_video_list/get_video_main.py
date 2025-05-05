import sys
import os

from channel_id_getter import get_channel_id
from uploads_playlist_getter import get_uploads_playlist_id
from video_id_getter import get_video_ids
from new_info_getter import get_videos_info

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from output.video_lists.console_outputter import output_info
from output.video_lists.dict_to_csv import create_video_csv

# Channel to scrape
handle = "maxthemeatguy"
# videos (long form), shorts, all_uploads 
video_type = "shorts"

# Get channel ID
channel_id = get_channel_id(handle)

# Get playlist ID of the channel's videos
channel_uploads_playlist = get_uploads_playlist_id(channel_id, video_type)

# Get the information of all the videos in the playlist(s)
video_ids = get_video_ids(channel_uploads_playlist)

# Get the information for each video
video_info = get_videos_info(video_ids)

# Sorting videos by date uploaded
videos_by_date = dict(sorted(video_info.items(), key = lambda item: item[1]['Numeric Date'], reverse=True))


# Output the dictionary to the console (in a table)
output_info(videos_by_date)

# Create CSV file for dictionary
create_video_csv(videos_by_date, handle, video_type)
