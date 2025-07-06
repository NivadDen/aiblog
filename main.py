import openai
from dotenv import dotenv_values

# Load API key from .env file
config = dotenv_values('test.env')
openai.api_key = config['API_KEY']

# Function to generate a blog paragraph using new SDK syntax
def generate_blog(p_topic):
    response = openai.Completion.create(
        model='gpt-3.5-turbo-instruct',
        prompt='Write a paragraph about the following topic: ' + p_topic,
        max_tokens=350,
        temperature=1
    )
    retrieve_blog = response.choices[0].text.strip()
    return retrieve_blog

# Ask the user for the first blog topic
first_topic = input("What do you want your first blog paragraph to be about? ")
print("\nGenerated Blog Paragraph:\n")
print(generate_blog(first_topic))

# Ask the user if they want to keep writing
keep_writing = True
while keep_writing:
    answer = input('\nWrite another paragraph? (Y for yes, anything else for no): ')
    if answer.strip().upper() == 'Y':
        paragraph_topic = input('What should this paragraph talk about? ')
        print("\nGenerated Blog Paragraph:\n")
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False
