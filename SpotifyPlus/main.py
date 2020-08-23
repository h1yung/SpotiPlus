from future.moves import tkinter as tk
from tkinter import messagebox
from GetPlaylist import GetPlaylist
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from collections import Counter
import numpy as np

OptionList = [
    "User's playlists will be displayed here"
]

playlist = GetPlaylist("foo")
variable = None

### function

def callback():
    global OptionList
    global playlist
    global variable

    def get_current_pl(value):
        global variable
        variable = value

    # ERROR: Username not found
    try:
        playlist = GetPlaylist(username_entry.get())
        OptionList = list(playlist.get_user_playlists_api().keys())
        OptionList.append("All Playlists")

    except:
        messagebox.showerror(title="Username Error", message="Username not found. Your Spotify username can be found in the upper-right hand corner of the desktop app and in the settings menu in the mobile app.")
    variable = tk.StringVar(window)

    opt = tk.OptionMenu(frame, variable, *OptionList, command=get_current_pl)
    opt.config(width=90, font=('Helvetica', 12))
    opt.place(relx=0.5, relwidth=0.5, relheight=1)

def determine():
    global playlist
    global variable

    # Reset genre composition dictionary
    playlist.all_genres = {'rock': 0,
                  'electronic': 0,
                  'acoustic': 0,
                  'rnb': 0,
                  'country': 0,
                  'blues': 0,
                  'alternative': 0,
                  'classical': 0,
                  'rap': 0,
                  'hip-hop': 0,
                  'indie': 0,
                  'jazz': 0,
                  'reggae': 0,
                  'pop': 0,
                  'punk': 0,
                  'metal': 0,
                  'ballad': 0
                  }

    # ERROR: Username not found
    if (username_entry.get() == "" or username_entry.get() == None):
        messagebox.showerror(title="Username Error",
                             message="Username not found. Your Spotify username can be found in the upper-right hand corner of the desktop app and in the settings menu in the mobile app.")
    else:
        # QUERY
        playlist_found = False


        for k, v in playlist.get_user_playlists_api().items():
            if k == variable or variable == "All Playlists":
                playlist_found = True
                # 1 playlist
                if k == variable:
                    song_apis = playlist.get_playlist_song_apis(v)
                    for api in song_apis:
                        song_artist = playlist.get_song_artist(api)
                        queried_genres = playlist.get_genres((song_artist))
                        for genre in queried_genres:
                            if genre.lower() in playlist.all_genres.keys():
                                playlist.all_genres[genre.lower()] += 1;
                # All playlist
                else:
                    song_apis = playlist.get_playlist_song_apis(v)
                    for song_api in song_apis:
                        song_artist = playlist.get_song_artist(song_api)
                        queried_genres = playlist.get_genres((song_artist))
                        for genre in queried_genres:
                            if genre.lower() in playlist.all_genres.keys():
                                playlist.all_genres[genre.lower()] += 1;
                # PIE CHART AND RANKING
        if playlist_found:
            # RANKING
            frame2 = tk.Frame(window, bg='#66ff66')
            frame2.place(relx=0.75, rely=0.35, relwidth=0.3, relheight=0.5, anchor='n')

            label = tk.Label(frame2, text="Top 5 Genres", bg='#737373', fg='#ffffff')
            label.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')

            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']
            explode = (0.1, 0, 0, 0, 0)  # explode 1st slice

            # Drop genres with 0 count
            null_genres = []
            for k, v in playlist.all_genres.items():
                if v == 0:
                    null_genres.append(k)
            for null_genre in null_genres:
                del playlist.all_genres[null_genre]

            # if more than 5 genres pick the top 5
            if len(playlist.all_genres) > 5:
                genre_count = dict(Counter(playlist.all_genres).most_common(5))
                # print(genre_count)
                # print(playlist.all_genres)

                label = tk.Label(frame2, text="(1) {}".format(list(genre_count.keys())[0]), bg='#66ff66',
                                 fg='#000000',
                                 borderwidth=2,
                                 relief="groove")
                label.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.18, anchor='n')
                label = tk.Label(frame2, text="(2) {}".format(list(genre_count.keys())[1]), bg='#66ff66',
                                 fg='#000000',
                                 borderwidth=2,
                                 relief="groove")
                label.place(relx=0.5, rely=0.28, relwidth=1, relheight=0.18, anchor='n')
                label = tk.Label(frame2, text="(3) {}".format(list(genre_count.keys())[2]), bg='#66ff66',
                                 fg='#000000',
                                 borderwidth=2,
                                 relief="groove")
                label.place(relx=0.5, rely=0.46, relwidth=1, relheight=0.18, anchor='n')
                label = tk.Label(frame2, text="(4) {}".format(list(genre_count.keys())[3]), bg='#66ff66',
                                 fg='#000000',
                                 borderwidth=2,
                                 relief="groove")
                label.place(relx=0.5, rely=0.64, relwidth=1, relheight=0.18, anchor='n')
                label = tk.Label(frame2, text="(5) {}".format(list(genre_count.keys())[4]), bg='#66ff66',
                                 fg='#000000',
                                 borderwidth=2,
                                 relief="groove")
                label.place(relx=0.5, rely=0.82, relwidth=1, relheight=0.18, anchor='n')
            # if less than or equal to 5 genres pick only that amount
            else:

                label = tk.Label(frame2, text="", bg='#66ff66', fg='#000000', borderwidth=2,
                                 relief="groove")
                label.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.18, anchor='n')
                label = tk.Label(frame2, text="", bg='#66ff66', fg='#000000', borderwidth=2,
                                 relief="groove")
                label.place(relx=0.5, rely=0.28, relwidth=1, relheight=0.18, anchor='n')
                label = tk.Label(frame2, text="", bg='#66ff66', fg='#000000', borderwidth=2,
                                 relief="groove")
                label.place(relx=0.5, rely=0.46, relwidth=1, relheight=0.18, anchor='n')
                label = tk.Label(frame2, text="", bg='#66ff66', fg='#000000', borderwidth=2,
                                 relief="groove")
                label.place(relx=0.5, rely=0.64, relwidth=1, relheight=0.18, anchor='n')
                label = tk.Label(frame2, text="", bg='#66ff66', fg='#000000', borderwidth=2,
                                 relief="groove")
                label.place(relx=0.5, rely=0.82, relwidth=1, relheight=0.18, anchor='n')

                genre_count = dict(Counter(playlist.all_genres).most_common(len(playlist.all_genres)))
                colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']
                explode = np.repeat(0, len(genre_count))  # explode 1st slice
                explode[len(explode) - 1] = 0
                colors = colors[:len(genre_count)]

                for i in range(len(genre_count)):
                    label = tk.Label(frame2, text="({}) {}".format(i + 1, list(genre_count.keys())[i]),
                                     bg='#66ff66', fg='#000000', borderwidth=2,
                                     relief="groove")
                    label.place(relx=0.5, rely=0.1 + 0.18 * i, relwidth=1, relheight=0.18, anchor='n')

                # print(explode)
                # print(genre_count)
                # print(playlist.all_genres)

            fig = Figure(figsize=(5, 4), dpi=100)
            plot = fig.add_subplot(111)
            plot.pie(list(genre_count.values()), explode=explode, labels=list(genre_count.keys()),
                     colors=colors,
                     autopct='%1.1f%%', shadow=True, startangle=140)

            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(relx=0.05, rely=0.3, relwidth=0.5, relheight=0.5)

            fig.patch.set_facecolor("lightgray")

            # Top Genre Report
            messagebox.showinfo(title="Top Genre",
                                message="Top genre is {}.".format(list(genre_count.keys())[0]))
            print(genre_count)

        # ERROR: Playlist not found
        else:
            messagebox.showerror(title="Playlist Error", message="Select your playlist!")


### GUI

window = tk.Tk()
window.geometry("700x700")
window.configure(bg='lightgray')
window.title('SpotiPlus')
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='spotify.png'))
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='spotify.png'))

# Background color
background_color = tk.Frame(window, bg="#ebadad")
background_color.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

# Border outline
border = tk.Frame(window, borderwidth=2, relief='groove', bg="lightgray")
border.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.9, anchor='n')

# Header
label = tk.Label(window, text="SpotiPlus by h1yung", bg='#737373', fg='#ffffff', borderwidth=2, relief="groove", font=("Courier", 44))
label.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.1, anchor='n')
label = tk.Label(window, text="Find out the genre of your playlist", bg='#66ff66', borderwidth=2, relief="groove", font=("Courier", 20))
label.place(relx=0.5, rely=0.15, relwidth=0.9, relheight=0.05, anchor='n')


# Entry row
frame = tk.Frame(window, bg='lightgray', borderwidth=2, relief="groove")

frame.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.04, anchor='n')
username_entry = tk.Entry(frame, font=40)
username_entry.place(relwidth=0.3, relheight=1)

button = tk.Button(frame, text="Search User", command=callback)
button.place(relx=0.3, relheight=1, relwidth=0.2)

variable = tk.StringVar(window)
variable.set(OptionList[0])
opt = tk.OptionMenu(frame, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.place(relx=0.5, relwidth=0.5, relheight=1)
variable.trace("w", callback)

button = tk.Button(window, text=">>> Analyze Playlist <<<", command=determine, bg='lightgray')
button.place(relx=0.05, rely=0.24, relheight=0.05, relwidth=0.9)

# Results

frame2 = tk.Frame(window, bg='lightgray')
frame2.place(relx=0.75, rely=0.35, relwidth=0.3, relheight=0.5, anchor='n')
label = tk.Label(frame2, text="Top 5 Genres", bg='#737373', fg='#ffffff')
label.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
label = tk.Label(frame2, text="", bg='#66ff66', fg='#000000', borderwidth=2, relief="groove")
label.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.18, anchor='n')
label = tk.Label(frame2, text="", bg='#66ff66', fg='#000000', borderwidth=2, relief="groove")
label.place(relx=0.5, rely=0.28, relwidth=1, relheight=0.18, anchor='n')
label = tk.Label(frame2, text="", bg='#66ff66', fg='#000000', borderwidth=2, relief="groove")
label.place(relx=0.5, rely=0.46, relwidth=1, relheight=0.18, anchor='n')
label = tk.Label(frame2, text="", bg='#66ff66', fg='#000000', borderwidth=2, relief="groove")
label.place(relx=0.5, rely=0.64, relwidth=1, relheight=0.18, anchor='n')
label = tk.Label(frame2, text="", bg='#66ff66', fg='#000000', borderwidth=2, relief="groove")
label.place(relx=0.5, rely=0.82, relwidth=1, relheight=0.18, anchor='n')

if __name__ ==  "__main__":
    window.mainloop()
