# Transcription and QA based on video
Scripts designed to download video based on the URL and transcribe the video using a LLM audio-to-text transcription model to be defined. 
The transcribed text is then used to generate questions and answers using a LLM to be defined - probably ChatGPT. 
The QA model is then used to answer questions based on the video content.

# Setup

1. Create conda environment

```bash
conda create -n video-transcription python=3.12
```

2. Activate conda environment

```bash
conda activate video-transcription
```

3. Install requirements

```bash
pip install -r requirements.txt
```

4. Run the video download script with the URL of the video as an argument

```bash
python scripts/video_downloader.py --url <URL>
```