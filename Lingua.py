import openai
import csv
import datetime
import os
import re
from dotenv import load_dotenv

# Set your OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_language_code(text):
    language_response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Please identify the language of the following text: '{text}'",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    language = language_response['choices'][0]['text'].strip()
    return language

def get_response(prompt, language_code):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Converse naturally in {language_code} and keep the conversation in the same language as the user input. Maintain context and provide relevant responses:\n\n{prompt}\n\nAI: ",
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

def get_feedback(conversation, language_code):
    feedback_prompt = f"""Please provide a detailed, kind, and encouraging feedback in English for the following conversation in {language_code} language. 
    Evaluate the user's vocabulary, sentence structure, grammar, overall language use, and their ability to maintain the context. 
    Highlight what the user did well and suggest areas for improvement. When providing feedback, assume the identity of a language tutor.
    The feedback should cover at least 3 specific points:\n\n"""
    feedback_prompt += '\n'.join(conversation)

    feedback_response = openai.Completion.create(
        model="text-davinci-002",
        prompt=feedback_prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return feedback_response.choices[0].text.strip()

def main():
    print("Hello! It is so nice to meet you! My name is Lingua, your language learning assistant. Please start speaking to me in your target learning language of choice.")

    conversation = []

    for i in range(5):
        user_text = input()
        conversation.append(f"User: {user_text}")

        if user_text.lower() == 'exit':
            break

        language_code = get_language_code(user_text)
        if language_code == "Unknown":
            print("I'm sorry, but I currently do not understand this language enough to provide feedback in a respectful way.")
            break

        ai_response = get_response('\n'.join(conversation), language_code)
        conversation.append(f"AI: {ai_response}")
        print(ai_response)

    feedback = get_feedback(conversation, language_code)

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{language_code}Conversation{timestamp}.csv"
    feedback_filename = f"{language_code}Feedback{timestamp}.csv"

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Role', 'Text'])
        for line in conversation:
            role, text = line.split(': ', 1)
            writer.writerow([role, text])

    with open(feedback_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Feedback'])
        writer.writerow([feedback])

    print("\nConversation transcript and feedback files have been saved.")

if __name__ == "__main__":
    main()
