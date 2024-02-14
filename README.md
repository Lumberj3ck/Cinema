# City Cinema Website

![City Cinema Website](https://github.com/Lumberj3ck/Cinema/blob/main/FilmLibrary/static/favicons/android-chrome-192x192.png)

## Description

The City Cinema Website is a dynamic and user-friendly platform designed to provide comprehensive information about films, showtimes, reviews, and events for a city cinema. It offers movie enthusiasts a seamless experience to explore and engage with their favorite films and upcoming screenings.

## Motivation

The motivation behind creating the City Cinema Website was to enhance the moviegoing experience for the audience by providing a centralized platform where they can easily access all necessary information about films and showtimes. Personaly, I didn't like our city cinema websites, so it motivated me to build up better version.

## Quick Start

To quickly set up and deploy the City Cinema Website on your own server, follow these steps:

1. Edit .env.prod file add your site ip or domain name to allowed host variable
2. Enable docker
  ```
   docker compose build
   docker compose up
   ```
4. Then you need to create a volume for postgres to implement this run this command. This code bellow will create data for database from db.json file.  
  ```
    docker exec your_container_id python manage.py migrate
    docker exec your_container_id python manage.py loaddata db.json
  ```
5. Enable search, Inside postgres shell 
  ```
   psql -U yourusername -d yourdatabase
    # psql -U lumberjack -d cinema_project
  ```
6. Inside psql shell run
  ```
 CREATE EXTENSION pg_trgm;

## Usage
Key Features and Achievements:

Film Information: I designed the website to showcase comprehensive information about films. Visitors can easily find details about movie plots, cast, and crew.

Showtimes: To enhance user convenience, I integrated a showtimes feature, allowing users to check movie schedules and book tickets online.

User Reviews: Movie enthusiasts can share their thoughts and experiences by posting reviews and ratings on the platform.

Events Calendar: I implemented an events calendar to keep users informed about special screenings, premieres, and film-related events.

Attractive Design: The website boasts an attractive and intuitive design, making it visually appealing and user-friendly.

Security: Security was a top priority. I ensured that user data and payment information are handled securely to provide a safe online booking experience.

Responsive Design: The website is fully responsive, adapting seamlessly to various devices, including desktops, tablets, and smartphones.
  ```
Now set up is done
