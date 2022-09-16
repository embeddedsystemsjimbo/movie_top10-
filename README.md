# Movie Top10 web app. 
“Top 10 Movie List “web application created using the Flask framework, Flask-Bootstrap framework, Wtforms library, SQLAlchemy (ORM) and "The Movie Database" (TMDB) API.

(The HTML frontend template is borrowed from Dr. Angela Yu's 100 Days of Code: Python Bootcamp course, however the backend is my own.)

This is a web application created using Python and the Flask framework that automates some of the user inputs required when creating a “Top 10 Movie List”. For instance, the movie poster image URL, date of release and overview are retrieved automatically using the “The Movie Database" API (https://www.themoviedb.org). Furthermore, the movies are displayed on the homepage dynamically based on user review and saved locally on server with a SQL based database. 

Movies on the list are displayed on flip cards, where one side displays the movie poster with a superimposed movie list rank and the other side displays the movie title, user rating, movie overview and user review (See Figure 1). The movie card order and the rank label are determined by the movie rating where cards are displayed from highest to lowest movie rating. Consequently, as movies are added to the movie list, the movie list order is dynamically changed in ordered to reflect the ranking system. 

A user can add a movie by first selecting the “add movie” button at the bottom of the homepage to switch to the movie search page.  Once on the movie search page, the user can search for a movie of interest by entering a movie to search in the text field and by selecting the “add movie” button. The user will be transfer to the movie selection page, where a list of movie search results matches is presented (See Figure 4). The user can select a movie, by selecting the desired movie link to add the movie to the movie list. 

After the movie title of choice has been selected by the user, they will be transferred to the review page where they can input a movie rating and write a movie review in the provided text fields (See Figure 5). By selecting the “Done” button, the addition of the new movie to the movie list is complete, and the user will be transferred to the home page (See Figure 6 & 7). 

Movie cards can be deleted or updated by selecting the appropriate “update” or “delete” button found on each movie card. 

***

![image](https://user-images.githubusercontent.com/76194492/190506634-f23fbf5f-ce25-405d-a10a-52f0d8a33f40.png)
Figure 1: Home page.

![image](https://user-images.githubusercontent.com/76194492/190506716-9f0e6494-563c-4f15-ac78-20670ac3e21d.png)
Figure 2: Movie card once flipped reveals a movie title, user rating, description and user review.


![image](https://user-images.githubusercontent.com/76194492/190507396-d50abc7c-af17-4d07-a693-eb57cf12566c.png)
Figure 3: Search page. 

![image](https://user-images.githubusercontent.com/76194492/190507443-7342c1d7-cf94-4e94-87d5-e603677e63f9.png)
Figure 4: Select page.

![image](https://user-images.githubusercontent.com/76194492/190507571-17f42c7d-25c5-4b2d-a942-834271efbbe3.png)
Figure 5: Rating/Review page.

![image](https://user-images.githubusercontent.com/76194492/190507638-a4984bef-3950-4f65-a4cb-c70bd42e8b89.png)
Figure 6: Updated home page.

![image](https://user-images.githubusercontent.com/76194492/190507673-54f156a7-42d1-4bf6-9fbd-a33caa4d5d09.png)
Figure 7: Newly created movie card.
