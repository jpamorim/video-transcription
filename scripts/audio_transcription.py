import argparse
import json
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


def transcribe_audio(audio_path, language):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = "openai/whisper-large-v3"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=30,
        batch_size=16,
        torch_dtype=torch_dtype,
        device=device,
    )

    result = pipe(audio_path, return_timestamps=True, generate_kwargs={"language": language})
    return result  


def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--audio_path', required=False, type=str,  default="../data/test.wav")
    parser.add_argument('--transcription_path', required=False, type=str,  default="../data/transcription.txt")
    parser.add_argument('--timestamps', required=False, type=bool,  default=False)
    parser.add_argument('--language', required=False, type=str,  default="english")
    args = parser.parse_args()
    return args.audio_path, args.transcription_path, args.timestamps, args.language


def save_transcription_txt(transcription, transcription_path):
    # Save transcription to text file
    transcription = transcription["text"]
    transcription.encode('utf-8', "ignore").decode('utf-8')
    with open(transcription_path,"w") as f:
        f.write(transcription)


def save_transcription_json(transcription, transcription_path):
    # Save transcription to json file
    with open(transcription_path, "w") as f:
        json.dump(transcription, f, indent=4)      

 
def main():
    audio_path, transcription_path, timestamps, language = parse_args()
    transcription = transcribe_audio(audio_path, language)
    
    if timestamps:
        save_transcription_json(transcription, transcription_path)
    else:
        save_transcription_txt(transcription, transcription_path)


if __name__=='__main__':
    main()