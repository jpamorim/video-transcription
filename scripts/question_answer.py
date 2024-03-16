import openai
import dotenv
import os
import argparse


dotenv.load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--transcription_path', required=False, type=str, default="../data/transcription.txt")
    args = parser.parse_args()
    return args.transcription_path


def ask_question(client, context, question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
            {"role": "assistant", "content": context}
        ]
    )
    return completion.choices[0].message.content


def setup_openai_client(filepath):
    client = openai.OpenAI(api_key=API_KEY)
    with open(filepath, "r") as f:
        context = f.read()
    return client, context


def main():    
    transcription_path = parse_args()
    client, context = setup_openai_client(transcription_path)
    question = input("Ask a question: ")
    answer = ask_question(client, context, question)
    print(answer)


if __name__=='__main__':
    main()
