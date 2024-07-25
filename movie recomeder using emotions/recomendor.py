import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import ttk, messagebox

# Dictionary to map emotions to IMDb URLs
URLS = {
    "Drama": 'https://www.imdb.com/search/title/?title_type=feature&genres=drama',
    "Action": 'https://www.imdb.com/search/title/?title_type=feature&genres=action',
    "Comedy": 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy',
    "Horror": 'https://www.imdb.com/search/title/?title_type=feature&genres=horror',
    "Crime": 'https://www.imdb.com/search/title/?title_type=feature&genres=crime',
}

def fetch_movie_titles(emotion):
    url = URLS.get(emotion)
    if not url:
        return []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")

    # Extract movie titles
    titles = [a.get_text() for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/'))]
    return titles

def on_submit():
    emotion = emotion_var.get()
    if not emotion:
        messagebox.showwarning("Input Error", "Please select an emotion.")
        return

    movie_titles = fetch_movie_titles(emotion)
    if not movie_titles:
        messagebox.showinfo("No Titles", "No titles found.")
    else:
        max_titles = 14 if emotion in ["Drama", "Action", "Comedy", "Horror", "Crime"] else 12
        movie_listbox.delete(0, tk.END)
        for title in movie_titles[:max_titles]:
            movie_listbox.insert(tk.END, title)

def show_recommender():
    login_frame.pack_forget()
    recommender_frame.pack(pady=10)

def authenticate_user():
    username = username_entry.get()
    password = password_entry.get()

    # Simple authentication check (for demonstration purposes)
    if username == "2303" and password == "12345":
        show_recommender()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Movie Recommender")
root.configure(bg='light green')

# Style
style = ttk.Style()
style.configure("TLabel", background='light green')
style.configure("TButton", background='white', foreground='black', font=('Helvetica', 10, 'bold'))
style.configure("TCombobox", font=('Helvetica', 10))

# Login Frame
login_frame = tk.Frame(root, bg='light green')
login_frame.pack(pady=10)

header_label = tk.Label(login_frame, text="Login", font=("Helvetica", 20, "bold"), bg='light green')
header_label.grid(row=0, column=0, columnspan=2, pady=20)

username_label = ttk.Label(login_frame, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=5)
username_entry = ttk.Entry(login_frame)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5)
password_entry = ttk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

login_button = ttk.Button(login_frame, text="Login", command=authenticate_user)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# Recommender Frame
recommender_frame = tk.Frame(root, bg='light green')

header_label = tk.Label(recommender_frame, text="Movie Recommendation", font=("Helvetica", 20, "bold"), bg='light green')
header_label.pack(pady=20)

frame = tk.Frame(recommender_frame, bg='light green')
frame.pack(pady=10)

emotion_label = ttk.Label(frame, text="Select an emotion:")
emotion_label.grid(row=0, column=0, padx=10, pady=5)

emotion_var = tk.StringVar()
emotion_combobox = ttk.Combobox(frame, textvariable=emotion_var, state="readonly")
emotion_combobox['values'] = list(URLS.keys())
emotion_combobox.grid(row=0, column=1, padx=10, pady=5)

submit_button = ttk.Button(recommender_frame, text="Get Movies", command=on_submit)
submit_button.pack(pady=10)

movie_listbox = tk.Listbox(recommender_frame, width=50, height=15, font=('Helvetica', 10))
movie_listbox.pack(pady=10)

# Start the GUI event loop
root.mainloop()
