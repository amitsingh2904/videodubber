from pydub import AudioSegment
from pydub.utils import which

# Manually set the ffmpeg path for pydub
ffmpeg_path = which("ffmpeg")
print(f"FFmpeg path detected by pydub: {ffmpeg_path}")

# Set ffmpeg path in pydub
AudioSegment.converter = ffmpeg_path

# Test by loading an MP3 file
try:
    sound = AudioSegment.from_mp3("translated_audio.mp3")
    print("FFmpeg is properly linked to pydub!")
except Exception as e:
    print(f"Error: FFmpeg is not linked properly. Details: {e}")

