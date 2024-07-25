Overview
This application is a movie recommender tool with a graphical user interface (GUI) built using tkinter. It allows users to login and get movie recommendations based on the selected emotion. The recommendations are fetched from IMDb based on the chosen genre (e.g., Drama, Action, Comedy, etc.).

Components
Libraries Used
requests: For sending HTTP requests to fetch movie data from IMDb.
BeautifulSoup (from bs4): For parsing HTML content and extracting movie titles.
re: For regular expressions to match movie title URLs.
tkinter: For creating the GUI components of the application.
ttk (from tkinter): For additional styling of GUI components.
messagebox: For displaying popup messages to users.
URL Mapping
The URLS dictionary maps genre names (emotions) to their corresponding IMDb search URLs:

python
Copy code
URLS = {
    "Drama": 'https://www.imdb.com/search/title/?title_type=feature&genres=drama',
    "Action": 'https://www.imdb.com/search/title/?title_type=feature&genres=action',
    "Comedy": 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy',
    "Horror": 'https://www.imdb.com/search/title/?title_type=feature&genres=horror',
    "Crime": 'https://www.imdb.com/search/title/?title_type=feature&genres=crime',
}
Functions
fetch_movie_titles(emotion)
Fetches movie titles based on the selected emotion:

Parameters: emotion (str) - The genre of movies to fetch.
Returns: A list of movie titles.
Description: Sends a GET request to the IMDb URL corresponding to the selected genre. Parses the HTML to extract movie titles and returns them as a list. Displays an error message if the request fails.
on_submit()
Handles the submission of the genre selection:

Description: Retrieves the selected genre from the dropdown menu. Calls fetch_movie_titles() to get the movie titles and displays them in the listbox. Limits the number of displayed titles to 14 for certain genres.
show_recommender()
Displays the movie recommender frame after successful login:

Description: Hides the login frame and shows the movie recommender frame.
authenticate_user()
Handles user authentication:

Description: Checks if the entered username and password match the predefined values ("2303" and "12345"). If the credentials are correct, it calls show_recommender(). Otherwise, it displays an error message.
GUI Components
Main Window: The root window with the title "Movie Recommender" and a light green background.

Login Frame:

Header Label: Displays "Login" in a large, bold font.
Username and Password Entries: Fields for entering username and password.
Login Button: Authenticates the user and displays the recommender frame if credentials are correct.
Recommender Frame:

Header Label: Displays "Movie Recommendation" in a large, bold font.
Emotion Selection:
Label: Prompts the user to select an emotion.
Combobox: Dropdown menu for selecting a genre.
Submit Button: Fetches and displays movie titles based on the selected genre.
Movie Listbox: Displays the list of movie titles.
Running the Application
Execute: Run the script to start the GUI application.
Login: Enter username ("2303") and password ("12345") to access the movie recommender.
Select Genre: Choose a genre from the dropdown menu.
Get Movies: Click the "Get Movies" button to fetch and display movie titles.
Additional Notes
Ensure the requests, beautifulsoup4, and lxml packages are installed in your Python environment.
The authentication check is simplistic and intended for demonstration purposes only. For a real-world application, use a secure authentication mechanism.
The list of movie titles displayed is limited to 14 for the specified genres. Adjust this number based on requirements.
