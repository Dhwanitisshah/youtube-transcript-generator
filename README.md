# YouTube Transcript Generator

A Streamlit application that generates transcripts from YouTube videos using OpenAI's Whisper model.

## Features

- Download audio from YouTube videos
- Convert audio to WAV format
- Transcribe audio using Whisper models (tiny, base, small, medium, large)
- Save transcripts as text files

## Requirements

- Python 3.8+
- FFmpeg installed on your system
- GPU recommended for larger Whisper models

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/youtube-transcript-generator.git
cd youtube-transcript-generator
```

2. Create a virtual environment and activate it:
```
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Install FFmpeg if not already installed:
   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - macOS: `brew install ffmpeg`
   - Linux: `sudo apt install ffmpeg`

## Usage

1. Run the Streamlit app:
```
streamlit run youtube_transcript.py
```

2. Enter a YouTube URL in the input field
3. Select the Whisper model size (larger models are more accurate but slower)
4. Click "Generate Transcript"
5. The transcript will be displayed and saved as `transcript.txt`

## Notes

- Larger Whisper models require more memory and processing power
- The application downloads and processes audio locally
- Transcripts are saved in the same directory as the script

## License

MIT License