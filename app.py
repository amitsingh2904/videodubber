from flask import Flask, render_template, request, send_file
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip
import os
from pydub import AudioSegment

# Initialize the Flask app
app = Flask(__name__)

# Set upload folder paths
UPLOAD_FOLDER = 'uploaded_videos'
TRANSLATED_AUDIO_FOLDER = 'translated_audio'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TRANSLATED_AUDIO_FOLDER, exist_ok=True)

# Function to transcribe audio
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    return text

# Function to translate the transcribed text
def translate_text(text, target_language='hi'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Function to convert text to speech (TTS)
def text_to_speech(text, output_audio_file):
    tts = gTTS(text, lang='hi')  # Use 'hi' for Hindi or change to target language code
    tts.save(output_audio_file)
    print(f"Speech saved as {output_audio_file}")

# Function to convert MP3 to WAV
def convert_mp3_to_wav(mp3_file, wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")
    print(f"Converted {mp3_file} to {wav_file}")

# Function to replace audio in video
def replace_audio_in_video(video_file, new_audio_file, output_video_file):
    video = VideoFileClip(video_file)
    new_audio = AudioFileClip(new_audio_file)

    # Ensure the new audio does not exceed the video duration
    if new_audio.duration > video.duration:
        new_audio = new_audio.subclip(0, video.duration)  # Trim the audio
    else:
        silence = AudioSegment.silent(duration=(video.duration - new_audio.duration) * 1000)  # Create silence
        new_audio_segment = AudioSegment.from_wav(new_audio_file) + silence  # Add silence to match duration
        new_audio_segment.export(new_audio_file, format="wav")  # Save the modified audio
        new_audio = AudioFileClip(new_audio_file)

    final_video = video.set_audio(new_audio)
    final_video.write_videofile(output_video_file, codec='libx264', audio_codec='aac')
    print(f"Final video saved as {output_video_file}")


# Home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')


# Processing route
@app.route('/process', methods=['POST'])
def process():
    try:
        if 'videoFile' not in request.files:
            return 'No file part', 400

        video_file = request.files['videoFile']
        
        if video_file.filename == '':
            return 'No selected file', 400

        # Save the uploaded video file
        video_path = os.path.join(UPLOAD_FOLDER, video_file.filename)
        video_file.save(video_path)
        
        # Step 1: Extract audio from the video
        audio_output_path = os.path.join(TRANSLATED_AUDIO_FOLDER, 'output_audio.wav')
        video_clip = VideoFileClip(video_path)
        video_clip.audio.write_audiofile(audio_output_path)
        
        # Step 2: Transcribe the audio
        transcript = transcribe_audio(audio_output_path)
        print("Original Transcript:", transcript)

        # Step 3: Translate the transcript
        target_language = request.form['language']  # Get the selected language from the form
        translated_text = translate_text(transcript, target_language)
        print("Translated Text:", translated_text)

        # Step 4: Convert translated text to speech (MP3)
        mp3_audio_path = os.path.join(TRANSLATED_AUDIO_FOLDER, 'translated_audio.mp3')
        text_to_speech(translated_text, mp3_audio_path)

        # Step 5: Convert MP3 to WAV
        wav_audio_path = os.path.join(TRANSLATED_AUDIO_FOLDER, 'translated_audio.wav')
        convert_mp3_to_wav(mp3_audio_path, wav_audio_path)

        # Step 6: Replace audio in the video
        output_video_path = os.path.join(TRANSLATED_AUDIO_FOLDER, 'final_output_video.mp4')
        replace_audio_in_video(video_path, wav_audio_path, output_video_path)

        # Step 7: Return the dubbed video for download
        return send_file(output_video_path, as_attachment=True)
    
    except Exception as e:
        return f"Error during processing: {str(e)}", 500

# Run the Flask app
if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(debug=True)
