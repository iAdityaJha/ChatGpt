# Define OpenAI API key
#go to Google and search 'openai api key' then signup
#in profile dropdown go to views api key ,
# Create your key copy and paste in apikey here

import openai
openai.api_key = "your_API_key"
# Set up the model and prompt
while True:
    model_engine = "text-davinci-003"
    prompt = input('Enter New Question :')
    if 'exit' in prompt or 'quit' in prompt:
        break
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5, )
    response = completion.choices[0].text
    print(response)
