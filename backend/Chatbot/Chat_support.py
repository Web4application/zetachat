import openai

# Set your OpenAI API key
openai.api_key = "qusDmXVuflS2UgVbtNoxT3BlbkFJdB1IU0OFhSmKkTfBQpAo"

# Send a user's message to the GPT model
def chatbot_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": user_message}
        ]
    )
    return response['choices'][0]['message']['content']

# Test the chatbot
user_input = "Hello, how can I use Zetachat?"
print(chatbot_response(user_input))
