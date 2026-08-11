# LLM Question-Answering Application

A lightweight Large Language Model (LLM) question-answering application developed to explore the integration of LLM APIs into both command-line and web-based interfaces.

The project demonstrates how a Python application can accept natural-language questions, preprocess user input, send requests to an LLM through an OpenAI-compatible API, and return generated responses through either a terminal interface or a Flask web application.

## Project Overview

This project was developed as a practical exploration of building applications around Large Language Models.

Rather than limiting the implementation to a single interface, the project provides two ways to interact with the system:

1. **Command-Line Interface (CLI)** — allows users to ask questions directly from the terminal.
2. **Flask Web Application** — provides a browser-based interface for submitting questions and viewing generated answers.

The application uses **OpenRouter's OpenAI-compatible API interface**, allowing the model to be configured through environment variables rather than being hard-coded into the application.

## Key Features

### Command-Line Question Answering

The CLI application provides an interactive terminal-based question-answering experience.

Users can:

* Enter natural-language questions.
* View the preprocessed version of their question.
* Receive an LLM-generated response.
* Continue asking questions until they choose to exit.

### Web-Based Question Answering

The Flask application provides a browser-based interface for the same core question-answering functionality.

The application:

1. Receives a question through a web form.
2. Preprocesses the input.
3. Sends the processed question to the configured LLM.
4. Retrieves the generated response.
5. Displays the processed question and answer through the web interface.

### Input Preprocessing

User questions are normalized before being sent to the model.

The current preprocessing pipeline:

* converts text to lowercase;
* removes punctuation and non-word characters;
* removes surrounding whitespace.

This provides a simple example of preparing user input before passing it to an LLM API.

### Configurable LLM

The model is not permanently hard-coded into the application.

The project uses environment variables to configure:

* the API key;
* the model to use.

A default model is provided when no alternative model is specified.

This makes it easier to experiment with different compatible models without modifying the application code.

### Reasoning-Enabled Requests

The API request enables the provider's reasoning option, allowing the application to experiment with models that support reasoning capabilities.

## Architecture

```text
                    User
                     |
          +----------+----------+
          |                     |
          v                     v
    Command Line            Flask Web App
          |                     |
          +----------+----------+
                     |
                     v
             Input Preprocessing
                     |
                     v
             OpenAI-Compatible
                API Client
                     |
                     v
                OpenRouter
                     |
                     v
                 LLM Model
                     |
                     v
              Generated Answer
                     |
          +----------+----------+
          |                     |
          v                     v
       Terminal             Web Interface
```

## Technology Stack

### Programming Language

* Python

### AI / LLM

* Large Language Models (LLMs)
* OpenRouter API
* OpenAI-compatible API client

### Web Development

* Flask
* HTML
* CSS

### Supporting Libraries

* `python-dotenv`
* Python `re` module

## Project Structure

```text
LLM_QA_Project_Nwamata_Ogochukwu_22CG031890/
│
├── static/
│   └── ...
│
├── templates/
│   └── ...
│
├── LLM_QA_CLI.py
├── app.py
├── requirements.txt
├── LLM_QA_hosted_webGUI_link.txt
├── TERMINAL_REPORT_OF_WEBSITE.txt
└── .gitignore
```

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/chr454/LLM_QA_Project_Nwamata_Ogochukwu_22CG031890.git
cd LLM_QA_Project_Nwamata_Ogochukwu_22CG031890
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it according to your operating system.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and provide the API credentials required by the application.

The application reads the API key and model configuration from environment variables rather than storing credentials directly in the source code.

### 5. Run the CLI application

```bash
python LLM_QA_CLI.py
```

### 6. Run the Flask application

```bash
python app.py
```

The Flask application can then be accessed through the local address displayed by Flask.

## Engineering Considerations

One of the key design decisions in this project was separating application logic from API credentials and model configuration.

The API key is loaded through environment variables, while the model can also be changed without modifying the core application logic.

The project also demonstrates the difference between developing an LLM capability and exposing that capability through different interfaces: the same underlying question-answering workflow can be accessed through a terminal or a web application.

## What I Learned

This project strengthened my practical understanding of:

* integrating LLM APIs into Python applications;
* working with OpenAI-compatible APIs;
* managing API credentials using environment variables;
* preprocessing natural-language input;
* building interactive CLI applications;
* exposing AI functionality through Flask;
* separating application configuration from implementation;
* designing simple interfaces around LLM capabilities.

It also helped me move from simply experimenting with LLMs to thinking about how they can be incorporated into usable software applications.

## Future Improvements

Potential directions for extending the project include:

* conversation history and multi-turn context;
* streaming model responses;
* stronger input validation;
* structured error handling;
* configurable model selection through the user interface;
* retrieval-augmented generation (RAG);
* document-based question answering;
* evaluation of response quality;
* logging and monitoring;
* deployment using a production WSGI server.

## Project Status

This project represents an exploratory implementation of an LLM-powered question-answering application and provides a foundation for experimenting with more advanced LLM application patterns.

## Author

**Ogochukwu (Christiana) Nwamata**

Computer Science | Data Science | AI/ML | AI Engineering | Research

[LinkedIn](https://www.linkedin.com/in/ogochukwu-nwamata-39a620235/)
