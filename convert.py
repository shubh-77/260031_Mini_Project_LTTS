import os
import ffmpeg
from generate import generate_master_m3u8

formats = [
            {'name': '720p', 'resolution': '1280x720', 'bitrate': '2500k', 'audiorate': '128k'},
            {'name': '1080p', 'resolution': '1920x1080', 'bitrate': '4500k', 'audiorate': '192k'},
        ]

def convert_to_hls(input_file,segment_format='%03d.ts',output_dir='HLS-video-output'):
        
        ffmpeg_input_stream = ffmpeg.input(input_file)
        ffmpeg_output_streams = []

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for format in formats:
            ffmpeg_params = {
                'vf': "scale=w={}:h={}:force_original_aspect_ratio=decrease".format(
                    format['resolution'].split('x')[0], format['resolution'].split('x')[1]),
                'c:a': 'aac',
                'ar': '48000',
                'c:v': 'h264',
                'profile:v': 'main',
                'crf': '20',
                'sc_threshold': '0',
                'g': '48',
                'keyint_min': '48',
                'hls_time': '4',
                'hls_playlist_type': 'vod',
                'b:v': f"{format['bitrate']}",
                'maxrate': '856k',
                'bufsize': '1200k',
                'b:a': f"{format['audiorate']}",
                'hls_segment_filename': f"{output_dir}/{format['resolution'].split('x')[1]}p_{segment_format}"
            }

            ffmpeg_output_streams.append(
                ffmpeg.output(
                    ffmpeg_input_stream,
                    f"{output_dir}/{format['resolution'].split('x')[1]}p.m3u8",
                    **ffmpeg_params
                )
            )

            output_streams = ffmpeg.merge_outputs(*ffmpeg_output_streams)
            ffmpeg.run(output_streams)
        generate_master_m3u8(output_dir)