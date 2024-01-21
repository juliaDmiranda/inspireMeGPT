# InspireMeGPT

InspireMeGPT is a Django project developed during the Web Programming course.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Development](#development)
    - [Technologies Used](#technologies-used)
    - [Setup](#setup)
- [Acknowledgments](#acknowledgments)

## Project Overview

The primary objective of this project was to build a web application based on ChatGPT. Instead of relying on an API for ChatGPT responses during prompted interaction, InspireMeGPT takes a different approach by displaying motivational quotes.

## Features
- **User Authentication:**
  - Provide user authentication system with login and registration functionality.
- **Motivational Quotes:**
  - The core feature of InspireMeGPT is to provide users with motivational quotes in response to their interactions.
  - Utilizes the [ZenQuote](https://zenquotes.io/) API to dynamically fetch and display motivational quotes based on user input.

## How It Works

1. **User Input:**
   - Users interact with the web application by providing input.

2. **Motivational Quote Display:**
   - Instead of generating responses through an API-driven chat interface, InspireMeGPT uses the ZenQuote API to fetch and display random motivational quotes.

3. **ZenQuote API Integration:**
   - The application communicates with the ZenQuote API to ensure that, regardless of user input, a motivational quote is presented as a response. It was chosen use random quotes, however it is possiple to set differents variables (e.g: author).

## Development

### Technologies Used

- Django: The web framework for building the application.
- ZenQuote API: Integrated to provide a random range of motivational quotes.

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/inspireMeGPT.git
    cd inspireMeGPT/django_project
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Visit `http://localhost:8000` in your web browser.**

## Acknowledgments

- This project was developed as part of the Web Programming course.
- Motivational quotes provided by the ZenQuote API.
