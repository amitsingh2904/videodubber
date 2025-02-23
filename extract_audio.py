from moviepy.editor import VideoFileClip

def extract_audio(video_file, output_audio_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(output_audio_file)

extract_audio('video.mp4', 'output_audio.wav')
