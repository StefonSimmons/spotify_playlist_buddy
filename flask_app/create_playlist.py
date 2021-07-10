import requests
import webbrowser
import json
import sys
import base64
from secret import user_id, client_id, client_secret


class Playlist:

    def __init__(self):
        self.token = ""
        self.user_id = user_id
        self.song_uri = ""

    # create a playlist on my account 
    def create_playlist(self, name, description, public):    
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
            print("\nPlaylist_ID: ", res_json["id"])
        except Exception as e: 
            print("Create Playlist ERROR ",e)

    #  search for a song on spotify
    def search_spotify(self,query):
        self.get_client_flow_token()
        
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
    def add_song_to_playlist(self, playlist_id):
        url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
        data = json.dumps([self.song_uri])
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }
        try:
            res = requests.post(url, data=data, headers=headers)
            print("\nAdded to playlist: ",res.json())
        except Exception as e:
            print("Add Song ERROR: ", e)

    # get a list of playlists
    def get_playlists(self):
        url = "https://api.spotify.com/v1/me/playlists"
        headers ={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }
        try:
            res = requests.get(url, headers=headers)
            res_json = res.json()
            def get_properties(playlist):
                return {
                    "id": playlist["id"],
                    "name": playlist["name"],
                    "public": playlist["public"]
                }
            playlists = map(get_properties, res_json["items"])
            print("\n====== Playlists ======\n")
            for p in playlists:
                print(p)
            print("\n")

        except Exception as e:
            print("Get Playlists Error: ", e)

    def play(self):
        url = "https://api.spotify.com/v1/me/player/play"
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }
        try: 
            requests.put(url, headers=headers)
        except Exception as e:
            print("PLAY Error: ", e)

    def pause(self):
        url = "https://api.spotify.com/v1/me/player/pause"
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }
        try: 
            requests.put(url, headers=headers)
        except Exception as e:
            print("PAUSE Error: ", e)

    # get OAuth Token for Searching
    def get_client_flow_token(self):
        client_cred=client_id+":"+client_secret
        encoded_bytes = base64.b64encode(client_cred.encode("utf-8")) #base64 encoded client_id:client_secret. https://www.base64encoder.io/python/
        encoded_client = str(encoded_bytes, "utf-8")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic {}".format(encoded_client)
        }
        url = "https://accounts.spotify.com/api/token/"
        data = "grant_type=client_credentials"
        
        try:
            res = requests.post(url, data=data, headers=headers)
            res_json = res.json()
            self.token = res_json["access_token"]
        except Exception as e:
            print("Get Token ERROR: ", e)

    # get OAuth Token for User Acct Access- https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow
    def get_user_auth_token(self,refresh_code):
        client_cred=client_id+":"+client_secret
        encoded_bytes = base64.b64encode(client_cred.encode("utf-8")) #base64 encoded client_id:client_secret. https://www.base64encoder.io/python/
        encoded_client = str(encoded_bytes, "utf-8")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic {}".format(encoded_client)
        }
        url = "https://accounts.spotify.com/api/token/"
        data = "grant_type=authorization_code&code={}&redirect_uri=http://127.0.0.1:5500/".format(refresh_code)
        try:
            res = requests.post(url, data=data, headers=headers)
            res_json = res.json()
            self.token = res_json["access_token"]
        except Exception as e:
            print("Get Token ERROR: ", e)

    # get User Approval - authorization flow - https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow
    def get_user_approval(self):
        client_query = "client_id={}".format(client_id)
        response_query = "response_type=code"
        redirect_uri = "redirect_uri=http://127.0.0.1:5500/"
        scopes = "scope=user-read-private playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state"
        url = "https://accounts.spotify.com/authorize?{}&{}&{}&{}".format(client_query, response_query, redirect_uri, scopes)
        
        try:
            res = requests.get(url)
            webbrowser.open(res.url)
        except Exception as e:  
            print('Refresh: ', e)

    

new_list = Playlist()

def run_user_auth_process():
    new_list.get_user_approval()
    new_list.get_user_auth_token(input("Enter refresh code: "))

if sys.argv[1] == "cp":
    description = ' '.join(sys.argv[3:])
    private = input("Is {} Public? (Y)".format(sys.argv[2]))
    if private == "Y": private = True
    else: private = False
    run_user_auth_process()
    new_list.create_playlist(sys.argv[2], description, private)
elif sys.argv[1] == "s":
    query = ' '.join(sys.argv[2:])
    new_list.search_spotify(query)
    continue_ = input("\nAdd to Playlist (Y or N)? ")
    print("")
    if continue_.upper() == "Y":
        run_user_auth_process()
        new_list.get_playlists()
        playlist_id = input("\nEnter <Playlist_ID>: ")
        new_list.add_song_to_playlist(playlist_id)
elif sys.argv[1] == "list":
    run_user_auth_process()
    new_list.get_playlists()

elif sys.argv[1] == "play":
    run_user_auth_process()
    new_list.play()

elif sys.argv[1] == "pause":
    run_user_auth_process()
    new_list.pause()