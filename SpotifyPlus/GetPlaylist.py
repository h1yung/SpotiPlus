import requests
import os

class GetPlaylist:
    spotify_user_id = ""
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    LASTFM_APIKEY = os.environ.get('LASTFM_APIKEY')
    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']

    all_genres = {'rock': 0,
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
                  'ballad':0
                  }

    def __init__(self, username):
        self.spotify_user_id = username

    # (1) Get user's playlists
    def get_user_playlists_api(self):
        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.spotify_user_id)
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.access_token)
            }
        )
        response_json = response.json()
        # print(response_json)
        name_api_dict = {}
        for playlist in response_json['items']:
            name_api_dict[playlist['name']] = playlist['href']

        return name_api_dict



    # (2) Get the tracks of a playlist
    def get_playlist_song_apis(self, playlist_api):
        query = playlist_api
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.access_token)
            }
        )
        response_json = response.json()
        api_list = []
        for playlist in response_json['tracks']['items']:
            api_list.append(playlist['track']['href'])

        return api_list

    # (3) Get song's name and artist
    def get_song_artist(self, song_api):
        """Description"""
        global access_token
        query = song_api
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.access_token)
            }
        )
        response_json = response.json()
        return response_json['album']['artists'][0]['name']

    # (4) Get album's genre
    def get_genres(self, artist):
        headers = {'user-agent': "SpotiPlus"}
        url = 'http://ws.audioscrobbler.com/2.0/'

        payload = {'api_key':self.LASTFM_APIKEY,
                   'format':'json',
                   'artist':artist,
                   'autocorrect[0 | 1]':1,
                   'method':'artist.getInfo'
        }
        response = requests.get(url, headers=headers, params=payload)
        genre_list = []
        for genre in response.json()['artist']['tags']['tag']:
            genre_list.append(genre['name'])
        return genre_list