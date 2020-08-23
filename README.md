# SpotiPlus
Retrieve and visualize the top 5 music genres found in a selected public Spotify playlist or a user's entire playlist library.

<img width="600" alt="titlescreen" src="https://user-images.githubusercontent.com/54069717/90970449-395f4a00-e4d3-11ea-8b7b-ce3e7ff6fadb.png">

# What it is
A common question that we ask within one another is "what music do you like to listen to?" With SpotiPlus, you can scan all your or someone else's public Spotify playlists and determine what your favorite music genres are. 
Do you ever have a Spotify playlist full of songs and wonder: what would be the genre of this collection? find out with SpotiPlus!

Once the application completes its analysis, you get the top 5 music genres of a user's playlist(s) and a pie chart visualization of the playlist's music genre composition.

[![download](https://user-images.githubusercontent.com/54069717/71476026-fcf71500-27b0-11ea-8027-5eb0df3fe527.png)](https://www.youtube.com/watch?v=5r0NLp4A5c0)

# How it works
SpotiPlus uses **Python** and the Spotify and Live.fm **APIs**. With the Spotify API, it reads in the user's Spotify playlists, obtains the songs within, and then finds the artists of each song. Since Spotify's API does not consistently record the genres of songs and artists, I decided to use the Live.fm API, which has the "tag" element for storing genres that the artists belong to. I looked up the list of artists through live.fm and queried the genres into a dictionary.

With this data, I created a **Matplotlib** pie chart as well as a list of the top 5 genres. The GUI was made through **Tkinter**.

# How to use

1. Download the files in the repo
2. On terminal, switch to the file's directory
3. Run the following<br/>
  export CLIENT_ID="(your spotify developer client id)"<br/>
  export CLIENT_SECRET="(your spotify developer client secret)"<br/>
  export LASTFM_APIKEY="(your lastfm api key)"<br/>
  
  python main.py
