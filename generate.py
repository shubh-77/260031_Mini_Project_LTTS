
import os

import ffmpeg

formats = [
            {'name': '720p', 'resolution': '1280x720', 'bitrate': '2500k', 'audiorate': '128k'},
            {'name': '1080p', 'resolution': '1920x1080', 'bitrate': '4500k', 'audiorate': '192k'},
        ]

def generate_master_m3u8(output_dir,filename="playlist.m3u8"):
    m3u8_content = '#EXTM3U\n#EXT-X-VERSION:3'
    for format in formats:
         m3u8_content += f"\n#EXT-X-STREAM-INF:BANDWIDTH={str(format['bitrate']).replace('k', '000')}," \
                f"RESOLUTION={format['resolution']}\n"\
                    f"{format['name']}.m3u8"

    with open(f'{output_dir}/{filename}', "w") as file:
            file.write(m3u8_content)