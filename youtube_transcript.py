import streamlit as st
import subprocess
import os
import yt_dlp
import whisper

# -----------------------------
# Helper Functions (same as script)
# -----------------------------
def download_audio(youtube_url, output_file="audio.mp4"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_file,
        'quiet': True,
        'noplaylist': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        return output_file
    except Exception as e:
        st.error(f"❌ Error downloading YouTube video: {e}")
        return None

def convert_to_wav(input_file, output_file="audio.wav"):
    if input_file is None:
        return None
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", input_file, "-ar", "44100", "-ac", "1", output_file],
            check=True
        )
        return output_file
    except subprocess.CalledProcessError as e:
        st.error(f"❌ FFmpeg conversion failed: {e}")
        return None

def transcribe_audio(wav_file, model_size="base"):
    if wav_file is None:
        return ""
    try:
        model = whisper.load_model(model_size)
        result = model.transcribe(wav_file)
        return result["text"]
    except Exception as e:
        st.error(f"❌ Error transcribing audio: {e}")
        return ""

# -----------------------------
# Streamlit Frontend
# -----------------------------
st.title("YouTube Transcript Generator 🎙️")
st.write("Upload a YouTube video URL to get a transcript using local Whisper model.")

youtube_url = st.text_input("YouTube Video URL:")

model_size = st.selectbox(
    "Choose Whisper Model Size:",
    ["tiny", "base", "small", "medium", "large"],
    index=1
)

if st.button("Generate Transcript"):
    if not youtube_url.strip():
        st.warning("Please enter a YouTube URL!")
    else:
        st.info("Downloading audio...")
        mp4_file = download_audio(youtube_url)
        st.success("Download complete ✅")

        st.info("Converting to WAV...")
        wav_file = convert_to_wav(mp4_file)
        st.success("Conversion complete ✅")

        st.info("Transcribing audio...")
        transcript_text = transcribe_audio(wav_file, model_size)
        
        if transcript_text:
            st.success("Transcription complete ✅")
            st.text_area("Transcript", transcript_text, height=300)

            # Save transcript locally
            with open("transcript.txt", "w", encoding="utf-8") as f:
                f.write(transcript_text)
            st.info("Transcript saved as transcript.txt")
        else:
            st.error("❌ Failed to generate transcript.")
