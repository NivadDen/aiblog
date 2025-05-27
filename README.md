# AI Blog Generator

A simple Python script that generates blog paragraphs on any topic using OpenAI's GPT-3.5-turbo model.

## Overview

This project uses the OpenAI API to create paragraphs based on user input topics. It securely loads the API key from a `.env` file and interacts with the user via the command line to generate content dynamically.

## Features

- Generates blog paragraphs on any topic.
- Command-line interface prompts for new paragraphs.
- Securely loads API key from `.env`.
- Lightweight and easy to run.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name


2. Create and Activate Virtual Enviroment

    python -m venv .venv
    source .venv/bin/activate

3. Install Dependencies:

    pip install -r requirements.txt

4. Create a .env file in the project root with your OpenAI API key:

    API_KEY=your_openai_api_key_here

    Run The Script:

    python main.py
