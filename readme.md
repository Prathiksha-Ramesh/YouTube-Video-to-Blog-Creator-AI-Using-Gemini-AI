# YouTube Video to Blog Creator AI

This project utilizes an AI agent to convert YouTube video content into structured blog posts. The system automatically extracts video transcripts, processes the content, and generates blog articles using natural language processing techniques.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)
- [Contributing](#contributing)

## Overview

The YouTube Video to Blog Creator AI automates the creation of blog posts from YouTube videos. This tool is designed to help content creators expand their reach by repurposing video content as text-based articles, optimizing content for different platforms and audiences.

## Features

- **Transcript Extraction**: Automatically extracts transcripts from YouTube videos.
- **Content Processing**: Utilizes advanced NLP tools to refine and structure the extracted text.
- **Blog Generation**: Converts processed text into well-formatted blog posts.
- **SEO Optimization**: Enhances the generated text to be SEO-friendly, increasing its visibility on search engines.

## Installation

### Prerequisites

- Python 3.8+
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/youtube-to-blog-ai.git
   cd youtube-to-blog-ai
````

2. Create a virtual environment:
``` bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:
``` 
pip install -r requirements.txt
``` 
4. Configure environmental variables: Copy the `.env.example` file to create a `.env` file and adjust the variables accordingly.

## Usage
To start the application:

- Ensure all configurations in .env are set.
- Run the main script to initiate the content generation
``` bash 
python main.py

``` 
## Project Structure

- agents.py: Defines AI agents handling specific tasks like transcription and writing.
- tasks.py: Task definitions for the agents.
- tools.py: Utilities and helper functions.
- crew.py: Manages the workflow of different agents.
requirements.txt: Lists all project dependencies.
- .env: Contains environment variables (not tracked by Git).
- .gitignore: Specifies intentionally untracked files to ignore.

## Dependencies
Listed in requirements.txt, key dependencies include:

- crewai: For managing AI agents.
- langchain-huggingface: For NLP operations.
Additional dependencies for environment management and data handling.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! If you have suggestions for improvements or have encountered issues, please open an issue or submit a pull request.

