<!-- Find and Replace All [repo_name] -->
<!-- Replace [product-screenshot] [product-url] -->
<!-- Other Badgets https://naereen.github.io/badges/ -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- [![License][license-shield]][license-url] -->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/h1yung/SpotiPlus">
    <img src="https://user-images.githubusercontent.com/54069717/71475766-a806cf00-27af-11ea-9aff-4b0500bf2951.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SpotiPlus</h3>

  <p align="center">
    Retrieve and visualize the top 5 music genres found in a selected public Spotify playlist or a user's entire playlist library.
    <br />
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#youtube">YouTube Demo</a></li>
    <li><a href="#description">Description</a></li>
    <li><a href="#usage">Usage</a></li>
	<!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## YouTube

[![download](https://user-images.githubusercontent.com/54069717/71476026-fcf71500-27b0-11ea-8027-5eb0df3fe527.png)](https://www.youtube.com/watch?v=5r0NLp4A5c0)

## Description

<img width="600" alt="titlescreen" src="https://user-images.githubusercontent.com/54069717/90970449-395f4a00-e4d3-11ea-8b7b-ce3e7ff6fadb.png">

A common question that we ask within one another is "what music do you like to listen to?" With SpotiPlus, you can scan all your or someone else's public Spotify playlists and determine what your favorite music genres are. 
Do you ever have a Spotify playlist full of songs and wonder: what would be the genre of this collection? find out with SpotiPlus!

Once the application completes its analysis, you get the top 5 music genres of a user's playlist(s) and a pie chart visualization of the playlist's music genre composition.

SpotiPlus uses **Python** and the Spotify and Live.fm **APIs**. With the Spotify API, it reads in the user's Spotify playlists, obtains the songs within, and then finds the artists of each song. Since Spotify's API does not consistently record the genres of songs and artists, I decided to use the Live.fm API, which has the "tag" element for storing genres that the artists belong to. I looked up the list of artists through live.fm and queried the genres into a dictionary.

With this data, I created a **Matplotlib** pie chart as well as a list of the top 5 genres. The GUI was made through **Tkinter**.

## Usage

1. Download the files in the repo
2. On terminal, switch to the file's directory
3. Run the following<br/>
  export CLIENT_ID="(your spotify developer client id)"<br/>
  export CLIENT_SECRET="(your spotify developer client secret)"<br/>
  export LASTFM_APIKEY="(your lastfm api key)"<br/>
  
  python main.py
  
## Contact

Daniel Park - [@h1yung][linkedin-url] - h1yungpark@gmail.com

Project Link: [https://github.com/h1yung/SpotiPlus](https://github.com/h1yung/SpotiPlus)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/h1yung/SpotiPlus.svg?style=for-the-badge
[contributors-url]: https://github.com/h1yung/SpotiPlus/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/h1yung/SpotiPlus.svg?style=for-the-badge
[forks-url]: https://github.com/h1yung/SpotiPlus/network/members
[stars-shield]: https://img.shields.io/github/stars/h1yung/SpotiPlus.svg?style=for-the-badge
[stars-url]: https://github.com/h1yung/SpotiPlus/stargazers
[issues-shield]: https://img.shields.io/github/issues/h1yung/SpotiPlus.svg?style=for-the-badge
[issues-url]: https://github.com/h1yung/SpotiPlus/issues
[linkedin-url]: https://www.linkedin.com/in/fifadaniel
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
