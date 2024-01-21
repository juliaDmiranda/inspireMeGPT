# InspireMeGPT

InspireMeGPT is a Django project developed during the Web Programming course.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Media](#media)
- [How It Works](#how-it-works)
- [Development](#development)
    - [Technologies Used](#technologies-used)
- [Acknowledgments](#acknowledgments)

## Project Overview

The primary objective of this project was to build a web application based on ChatGPT. Instead of relying on an API for ChatGPT responses during prompted interaction, InspireMeGPT takes a different approach by displaying motivational quotes.

## Features
- **User Authentication:**
  - Provide user authentication system with login and registration functionality.
- **Motivational Quotes:**
  - The core feature of InspireMeGPT is to provide users with motivational quotes in response to their interactions.
  - Utilizes the [ZenQuote](https://zenquotes.io/) API to dynamically fetch and display motivational quotes based on user input.
 
## Media
### Login page
![Alt Login Page](https://media.discordapp.net/attachments/1198437251907080244/1198438091598348288/Screenshot_from_2024-01-20_22-15-27.png?ex=65bee772&is=65ac7272&hm=a075d6ba21274d3aca55406ffa4017c6f8bb48bb63ca3f14a07615c7df72d7b2&=&format=webp&quality=lossless&width=811&height=444)
### Sign up page
![Alt Sign Page](https://cdn.discordapp.com/attachments/1198437251907080244/1198438091178913832/Screenshot_from_2024-01-20_22-15-40.png?ex=65bee772&is=65ac7272&hm=7fe43a7902f4dbe6e1a71b103f1eae94b4344e05e904ea3e13678f61415cbec8&)

### Chat page
![Alt Chat Page 1](https://cdn.discordapp.com/attachments/1198437251907080244/1198438090100985977/Screenshot_from_2024-01-20_22-15-59.png?ex=65bee772&is=65ac7272&hm=cdfcbeefc9e76337cc501fce04c83efe7cb1a8defc7c67d4852adbf23708b4dc&)
![Alt Chat Page 2](https://cdn.discordapp.com/attachments/1198437251907080244/1198438089211789485/Screenshot_from_2024-01-20_22-16-24.png?ex=65bee772&is=65ac7272&hm=f8b844d1d8721354374d16508d86d22d60fab11d1e4ceafc1436617bb858c8fe&)

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

## Acknowledgments

- This project was developed as part of the Web Programming course.
- Motivational quotes provided by the [ZenQuote API](https://zenquotes.io/).
