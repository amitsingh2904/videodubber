# 🎬 AI Video Dubbing Website (Flask)

A Python–Flask based web application that automatically dubs videos into different languages by extracting audio, translating speech, generating new voice audio, and optionally adding subtitles.

---

## 🚀 Features

- Upload video files
- Automatic speech recognition
- Language translation
- Text-to-speech audio generation
- Replace original audio in video
- Optional subtitles support
- Download final dubbed video

---

## 🧠 Project Description

The AI Video Dubbing Website is designed to convert the spoken language of a video into another language automatically.  
The system extracts audio from the uploaded video, converts speech to text, translates it into the selected target language, generates new audio using text-to-speech, and replaces the original audio in the video.

This project demonstrates real-world usage of Python for multimedia processing and AI-based language translation.

---

## 👨‍💻 Contribution

This is a **group project**.  
My contribution is approximately **40%**, mainly focused on backend development, including:

- Flask backend development
- Video upload and file handling
- Audio extraction from video
- Speech-to-text processing
- Language translation logic
- Text-to-speech generation
- Audio–video synchronization
- Subtitle rendering using OpenCV
- Error handling and backend workflow

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Libraries & Tools
- SpeechRecognition
- googletrans
- gTTS
- MoviePy
- OpenCV
- Pydub
- Pillow (PIL)
- NumPy

### Frontend
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

AI-Video-Dubbing-Website/
│
├── main.py
├── uploaded_videos/
├── translated_audio/
├── templates/
│ ├── index.html
│ ├── upload.html
│ └── text_to_speech.html
├── static/
│ └── fonts/
└── README.md



---

## ▶️ Getting Started

### Prerequisites

- Python 3.8 or above
- pip
- Internet connection (required for speech recognition and translation APIs)

1. Clone the repository:
git clone https://github.com/your-username/ai-video-dubbing-website.git
cd ai-video-dubbing-website

2.Install required dependencies:
pip install flask moviepy speechrecognition googletrans gtts pydub opencv-python pillow numpy

3.Run the Flask application:
python main.py

4.Open the application in your browser:
bash
http://127.0.0.1:5000/



🔄 Application Workflow

-User uploads a video file
-Audio is extracted from the video
-Speech is converted into text
-Text is translated into the selected language
-Translated text is converted into speech
-New audio replaces the original video audio
-Optional subtitles are added to the video
-Final dubbed video is generated and downloaded


⚠️ Limitations

-Processing time increases for large video files
-Uses third-party APIs, so an internet connection is required
-Not optimized for large-scale production use
-No user authentication or database integration

