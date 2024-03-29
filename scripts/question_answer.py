import openai
import dotenv
import os
import argparse


dotenv.load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--transcription_path', required=False, type=str, default="../data/transcription.txt")
    parser.add_argument('--questions_path', required=False, type=str)
    parser.add_argument('--answers_path', required=False, type=str, default="../data/answers.txt")
    args = parser.parse_args()
    return args.transcription_path, args.questions_path, args.answers_path


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

def read_questions(filepath):
    with open(filepath, "r") as f:
        questions = f.readlines()
    return questions


def save_answers(answers, output_path):
    with open(output_path, "a") as f:
        if os.path.exists(output_path):
            f.write("\n" + "\n".join(answers))
        else:
            f.write("\n".join(answers))
            
        
def main():    
    transcription_path, questions_path, answers_path = parse_args()
    client, context = setup_openai_client(transcription_path)
    
    if questions_path:
        questions = read_questions(questions_path)
        answers = [ask_question(client, context, question) for question in questions]
        save_answers(answers, answers_path)

    else:
        stop = False
        while not stop:
            question = input("Write your question: ")
            if question == "stop":
                stop = True
                break
            question = input("Ask a question: ")
            answer = ask_question(client, context, question)
            print(answer)
            save_answers([answer], answers_path)


if __name__=='__main__':
    main()
