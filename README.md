# Project: City Cinema Website
[Working Demo](https://afishakino.info.gf/)
# Project Description:
For this engaging project, I had the pleasure of developing a dynamic and user-friendly website for a city cinema. The goal was to provide visitors with a seamless platform to explore a wide range of information about films, including showtimes, synopses, reviews, and more.

Key Features and Achievements:

🎥 Film Information: I designed the website to showcase comprehensive information about films. Visitors can easily find details about movie plots, cast, and crew.

📅 Showtimes: To enhance user convenience, I integrated a showtimes feature, allowing users to check movie schedules and book tickets online.

🌟 User Reviews: Movie enthusiasts can share their thoughts and experiences by posting reviews and ratings on the platform.

📆 Events Calendar: I implemented an events calendar to keep users informed about special screenings, premieres, and film-related events.

🎨 Attractive Design: The website boasts an attractive and intuitive design, making it visually appealing and user-friendly.

🔒 Security: Security was a top priority. I ensured that user data and payment information are handled securely to provide a safe online booking experience.

📱 Responsive Design: The website is fully responsive, adapting seamlessly to various devices, including desktops, tablets, and smartphones.

Technologies Used:

Frontend: HTML5, CSS3, JavaScript
Backend: Django
Database: PostgreSQL
Deployment: AWS


How to use:
1. Edit .env.prod file add your site ip or domain name to allowed host variable
2. Enable docker
  ```
   docker compose build
   docker compose up
   ```
4. Then you need to create a volume for postgres to implement this run this command
  ```
    docker exec your_container_id python manage.py migrate
    docker exec your_container_id python manage.py loaddata db.json
  ```
  This will create data for database from db.json file.  
5. Enable search 
  ```
   psql -U yourusername -d yourdatabase
  ```
6. Inside psql shell run
  ```
 CREATE EXTENSION pg_trgm;
  ```
Now set up is done

