import csv
import datetime
import os
import re
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

MAX_TOKENS = 1300

def get_language_code(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Please identify the language of the following text: '{text}'",
        max_tokens=250,
        n=1,
        stop=None,
        temperature=0.5,
    )
    language = response['choices'][0]['text'].strip()
    return language

def get_ai_response(prompt, language_code):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Converse naturally in {language_code} and keep the conversation in the same language as the user input. Maintain context and provide relevant responses:\n\n{prompt}\n\nAI: ",
        max_tokens=600,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def get_feedback(conversation, language_code):
    """
    Generates feedback for the given conversation and language code using OpenAI's text-davinci-003 model.
    """
    # Generate a prompt for feedback on vocabulary, grammar, and coherence
    prompt = f"""Please provide feedback in English on the user's vocabulary, grammar, and coherence. 
    Are there any words or phrases that they used correctly or incorrectly? 
    Are there any errors in their sentence structure or verb conjugation? 
    Were they able to maintain the context of the conversation and understand/respond to the AI's prompts appropriately? 
    Assume the identity of a caring language tutor.
    Please provide at least 3 specific examples from the conversation in {language_code}.
    Remember to keep the response in English! Limit feedback to 1000 characters.
    In addition, be sure to strive for linguistic accuracy when providing feedback."""

    # Generate feedback using the prompt
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt + '\n' + '\n'.join(conversation),
        max_tokens=MAX_TOKENS,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Return the feedback
    return response.choices[0].text.strip()

def save_conversation_and_feedback(conversation, feedback, language_code):
    """
    Saves the conversation and feedback as separate CSV files with timestamps.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{language_code}Conversation{timestamp}.csv"
    feedback_filename = f"{language_code}Feedback{timestamp}.csv"

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Role', 'Text'])
        for line in conversation:
            role, text = line.split(': ', 1)
            if role == 'AI':
                writer.writerow([f"{role}: {text}"])
            else:
                writer.writerow([f"{role}: {text}"])

    with open(feedback_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Feedback'])
        writer.writerow([feedback])

    print("\nConversation transcript and feedback files have been saved.")


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

        ai_response = get_ai_response('\n'.join(conversation), language_code)
        conversation.append(f"AI: {ai_response}")
        print(ai_response)

    feedback = get_feedback(conversation, language_code)

    save_conversation_and_feedback(conversation, feedback, language_code)

if __name__ == "__main__":
    main()

