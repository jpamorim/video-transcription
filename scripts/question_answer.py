import openai
import dotenv
import os


dotenv.load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")


def ask_question(client, question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
        ]
    )
    return completion.choices[0].message.content


def setup_openai_client():
    client = openai.OpenAI(api_key=API_KEY)
    return client


def main():    
    client = setup_openai_client()
    question = input("Ask a question: ")
    answer = ask_question(client, question)
    print(answer)


if __name__=='__main__':
    main()
