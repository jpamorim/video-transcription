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

5. Run the audio from video script with the filepath of the video and the output path of the audio file as arguments

```bash
python scripts/audio_from_video.py --filepath download/video --output_path download/audio.wav
```

6. Transcribe the audio file using the OpenAI whisper-large-v3 model

```bash
python scripts/audio_transcription.py --audio_path download/audio.wav --transcription_path download/transcription.json --timestamps True
```

7. Add OPENAI_API_KEY to the environment variables

```bash
export OPENAI_API_KEY=<API_KEY>
```

8. Ask question based on context of the transcription using ChaGPT API

```bash
python scripts/question_answer.py --transcription_path download/transcription.txt --questions_path download/questions.txt --answers_path download/answers.txt
```