import requests
import json
import sys
import base64
from secrets import user_id, client_id, client_secret

class CreatePlaylist:

    def __init__(self):
        self.user_id = user_id
        self.token = ""
        self.playlist_id = ""
        self.song_uri = ""

    # create a playlist on my account 
    def create_playlist(self, name, description, public=False):
        data = json.dumps({
            "name": name,
            "description": description,
            "public": public
        })
        url = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }
        try:
            res = requests.post(url, data=data, headers=headers)
            res_json = res.json()
            self.playlist_id = res_json["id"]
            print("Playlist_ID: ", res_json["id"])
            return res_json["id"]
        except Exception as e: 
            print("ERROR ",e)

    #  search for a song on spotify
    def search_spotify(self,query):
        self.get_new_token()
        
        url = f"https://api.spotify.com/v1/search?q={query}&type=track&market=us&limit=1"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }

        try:
            res = requests.get(url, headers=headers)
            res_json = res.json()
            song = res_json["tracks"]["items"][0]
            song_uri = song["uri"]
            song_info = "Song: {}\n Artist: {}".format(song["name"], song["artists"][0]["name"])
            self.song_uri = song_uri
            print("\n")
            print("Found:{ \n",song_info, "\n}")
            return song_uri
        except Exception as e: 
            print("Searching ERROR  ",e)

    # add song to playlist on spotify 
    def add_song_to_playlist(self):
        url = "https://api.spotify.com/v1/playlists/{}/tracks".format(self.playlist_id)
        data = json.dumps([self.song_uri])
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }
        res = requests.post(url, data=data, headers=headers)
        print(res.json())
        
    # refresh OAuth Token - https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow
    def get_new_token(self):
        client_cred=client_id+":"+client_secret
        encoded_bytes = base64.b64encode(client_cred.encode("utf-8")) #base64 encoded client_id:client_secret. https://www.base64encoder.io/python/
        encoded_client = str(encoded_bytes, "utf-8")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic {}".format(encoded_client)
        }
        url = "https://accounts.spotify.com/api/token/"
        try:
            res = requests.post(url, data="grant_type=client_credentials", headers=headers)
            self.token = res.json()["access_token"]
        except Exception as e:
            print("TOKEN ERROR: ", e)


new_list = CreatePlaylist()

if sys.argv[1] == "cp":
    description = ' '.join(sys.argv[3:])
    new_list.create_playlist(sys.argv[2], description)
elif sys.argv[1] == "s":
    query = ' '.join(sys.argv[2:])
    new_list.search_spotify(query)

# new_list.add_song_to_playlist()

print(new_list.playlist_id)