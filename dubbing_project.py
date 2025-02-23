import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip
import os
from pydub import AudioSegment  # Library to handle audio conversion

# Function to Transcribe Audio
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    return text

# Function to Translate the Transcribed Text
def translate_text(text, target_language='hi'):  # 'hi' is the language code for Hindi
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Function to Convert Text to Speech (TTS)
def text_to_speech(text, output_audio_file):
    tts = gTTS(text, lang='hi')  # Use 'hi' for Hindi or other language codes
    tts.save(output_audio_file)
    print(f"Speech saved as {output_audio_file}")

# Function to Convert MP3 to WAV
def convert_mp3_to_wav(mp3_file, wav_file):
    try:
        if not os.path.exists(mp3_file):
            print(f"Error: {mp3_file} not found!")
            return
        sound = AudioSegment.from_mp3(mp3_file)
        sound.export(wav_file, format="wav")
        print(f"Converted {mp3_file} to {wav_file}")
    except Exception as e:
        print(f"Error converting MP3 to WAV: {e}")

# Function to Replace Audio in the Video
def replace_audio_in_video(video_file, new_audio_file, output_video_file):
    try:
        video = VideoFileClip(video_file)
        new_audio = AudioFileClip(new_audio_file)

        # Check if audio and video are properly loaded
        print(f"Video duration: {video.duration} seconds")
        print(f"Audio duration: {new_audio.duration} seconds")

        # Ensure that audio duration matches the video duration
        new_audio = new_audio.set_duration(video.duration)

        # Replace the audio in the video
        final_video = video.set_audio(new_audio)

        # Export the final video with audio
        final_video.write_videofile(output_video_file, codec='libx264', audio_codec='aac')
        print(f"Final video saved as {output_video_file}")
    except Exception as e:
        print(f"Error replacing audio: {e}")

# Step 1: Transcribe the Audio
transcript = transcribe_audio('output_audio.wav')
print("Original Transcript:", transcript)

# Step 2: Translate the Transcript
translated_text = translate_text(transcript, 'hi')
print("Translated Text:", translated_text)

# Step 3: Convert Translated Text to Speech (MP3)
text_to_speech(translated_text, 'translated_audio.mp3')

# Step 4: Check if the MP3 file exists before conversion
if os.path.exists('translated_audio.mp3'):
    print("MP3 file exists. Proceeding with conversion...")
else:
    print("Error: translated_audio.mp3 does not exist!")

# Step 5: Convert MP3 to WAV
convert_mp3_to_wav('translated_audio.mp3', 'translated_audio.wav')

# Step 6: Check if the WAV file exists before replacing audio in the video
if os.path.exists('translated_audio.wav'):
    print("WAV file exists. Proceeding with audio replacement...")
    replace_audio_in_video('video.mp4', 'translated_audio.wav', 'final_output_video.mp4')
else:
    print("Error: translated_audio.wav does not exist!")