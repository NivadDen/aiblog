import openai

from dotenv import dotenv_values

config = dotenv_values('test.env')

openai.api_key = config['API_KEY']

def generate_blog(p_topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + p_topic,
    max_tokens = 350,
    temperature = 1
  )
  retrieve_blog = response.choices[0].text
  return retrieve_blog

print(generate_blog('Is Coding Everday Good?'))

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False
