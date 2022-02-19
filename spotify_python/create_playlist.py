import requests
import webbrowser
import json
import sys
import base64
from secret import user_id, client_id, client_secret, redirect_uri


class Playlist:

    def __init__(self):
        self.token = ""
        self.song_uri = ""
        self.playlists = []

    # create a playlist on my account 
    def create_playlist(self, name, description, public):    
        data = json.dumps({
            "name": name,
            "description": description,
            "public": public
        })
        url = "https://api.spotify.com/v1/users/{}/playlists".format(user_id)
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
            song_info = "Song: {}\n Artist: {}\n SongURI: {}".format(song["name"], song["artists"][0]["name"], song_uri)
            self.song_uri = song_uri
            print("\n")
            print("Found:{ \n",song_info, "\n}")
            return song_uri
        except Exception as e: 
            print("Searching ERROR  ",e)

    # add song to playlist on spotify 
    def add_song_to_playlist(self, playlist_idx):
        playlist = self.playlists[int(playlist_idx)-1]
        url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist["id"])
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
                    "name": playlist["name"],
                    "public": playlist["public"],
                    "id": playlist["id"],
                }
            playlists = map(get_properties, res_json["items"])
            print("\n====== Playlists ======\n")
            count = 1
            for p in playlists:
                self.playlists.append(p)
                print(f'idx:{count}',p)
                count += 1
            print("\n")

        except Exception as e:
            self.run_user_auth_process()
            print("Get Playlists Error: ", e)

    # play currently paused song on user's active player
    def play(self):
        url = "https://api.spotify.com/v1/me/player/play"
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }
        try: 
            requests.put(url, headers=headers)
        except Exception as e:
            self.run_user_auth_process()
            print("PLAY Error: ", e)

    # play a specific song on user's active player
    def play_a_song(self):
        url = "https://api.spotify.com/v1/me/player/play"
        data = json.dumps({
            "uris": [self.song_uri]
        })
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }   
        try:
            requests.put(url, data=data, headers=headers)
        except Exception as e:
            self.run_user_auth_process()
            print("Play specific song: ", e)

    # pause user's spotify player on running device
    def pause(self):
        url = "https://api.spotify.com/v1/me/player/pause"
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }
        try: 
            requests.put(url, headers=headers)
        except Exception as e:
            self.run_user_auth_process()
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
        data = "grant_type=authorization_code&code={}&redirect_uri={}".format(refresh_code, redirect_uri)
        try:
            res = requests.post(url, data=data, headers=headers)
            res_json = res.json()
            self.token = res_json["access_token"]
            auth_file = open('./access_token.txt', 'w')
            auth_file.write(self.token)
            auth_file.close()
        except Exception as e:
            print("Get Token ERROR: ", e)

    # get User Approval - authorization flow - https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow
    def get_user_approval(self):
        client_query = "client_id={}".format(client_id)
        response_query = "response_type=code"
        redirect_uri_param = "redirect_uri={}".format(redirect_uri)
        scopes = "scope=user-read-private playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state"
        url = "https://accounts.spotify.com/authorize?{}&{}&{}&{}".format(client_query, response_query, redirect_uri_param, scopes)
        
        try:
            res = requests.get(url)
            webbrowser.open(res.url)
        except Exception as e:  
            print('Refresh: ', e)

    def run_user_auth_process(self):
        self.get_user_approval()
        self.get_user_auth_token(input("Enter auth code: "))
    

new_list = Playlist()


def get_auth_token_from_store():
  with open("./access_token.txt", "r") as f:
    auth_token = f.read() ##Assume the sample file has 3 lines
    new_list.token = auth_token
    
if sys.argv[1] == "cp":
    description = ' '.join(sys.argv[3:])
    public = input("Is {} Public? (Y)".format(sys.argv[2]))
    if public == "Y": public = True
    else: public = False
    get_auth_token_from_store()
    new_list.create_playlist(sys.argv[2], description, public)
elif sys.argv[1] == "s":
    query = ' '.join(sys.argv[2:])
    new_list.search_spotify(query)
    play_it = input("\nPlay this song (Y or N)? ")
    if play_it.upper() == "Y":
        get_auth_token_from_store()
        new_list.play_a_song()
    continue_ = input("\nAdd to Playlist (Y or N)? ")
    print("")
    if continue_.upper() == "Y":
        new_list.get_playlists()
        playlist_idx = input("\nEnter <Playlist_IDX>: ")
        new_list.add_song_to_playlist(playlist_idx)
elif sys.argv[1] == "list":
    get_auth_token_from_store()
    new_list.get_playlists()

elif sys.argv[1] == "play":
    get_auth_token_from_store()
    new_list.play()

elif sys.argv[1] == "pause":
    get_auth_token_from_store()
    new_list.pause()