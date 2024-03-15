import argparse
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


def transcribe_audio(audio_path):
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

    result = pipe(audio_path)
    return result  


def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--audio_path', required=False, type=str,  default="../data/test.wav")
    parser.add_argument('--transcription_path', required=False, type=str,  default="../data/transcription.txt")
    args = parser.parse_args()
    return args.audio_path, args.transcription_path


def save_transcription(transcription, transcription_path):
    # Save transcription to text file
    transcription = transcription["text"]
    transcription.encode('utf-8', "ignore").decode('utf-8')
    with open(transcription_path,"w") as f:
        f.write(transcription)

 
def main():
    audio_path, transcription_path = parse_args()
    transcription = transcribe_audio(audio_path)
    save_transcription(transcription, transcription_path)


if __name__=='__main__':
    main()