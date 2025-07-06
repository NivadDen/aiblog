AI Blog Generator
A simple Python script that generates blog paragraphs on any topic using OpenAI's GPT-3.5-turbo-instruct model.

Overview
This project uses the OpenAI API to generate blog paragraphs based on user input topics. It securely loads the API key from a .env file and provides an interactive command-line interface to create dynamic content.

Features
Generate blog paragraphs on any user-defined topic.

Interactive command-line prompts for continuous writing.

Secure loading of API key from .env file.

Lightweight and easy to set up.

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Create and Activate Virtual Enviroment
   On macOS/Linux:
      python3 -m venv .venv
      source .venv/bin/activate
   On Windows:
      python -m venv .venv
      .\.venv\Scripts\activate

3. Install Dependencies:

    pip install -r requirements.txt

4. Create a .env file in the project root with your OpenAI API key:

    API_KEY=your_openai_api_key_here

    Run The Script with:

    python main.py

   Follow the prompts to input your blog topic and continue generating paragraphs interactively.

  # Notes
  This script uses OpenAI Python SDK version 0.28 to maintain compatibility with the current code syntax.
  
  To upgrade to newer SDK versions, code modifications are required.
