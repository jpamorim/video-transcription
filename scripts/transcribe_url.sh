#!/bin/bash

python video_downloader.py --url $1
python audio_from_video.py --filepath download/video --output_path download/audio.wav
python audio_transcription.py --audio_path download/audio.wav --transcription_path download/transcription.json --timestamps True --language portuguese
python question_answer.py --transcription_path download/transcription.txt --questions_path download/questions.txt --answers_path download/answers.txt