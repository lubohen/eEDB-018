import requests
from config import SPOT_CLIENT_SECRET, SPOT_CLIENT_ID

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': SPOT_CLIENT_ID,
    'client_secret': SPOT_CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'
track_name = "Bulldog Down in Sunny Tennessee"
artist_name = "Charlie Poole"

# make the API request
r = requests.get(BASE_URL + 'search?q=track:' + track_name + '+artist:' + artist_name + '&type=track', headers=headers)

# get the first track from the results
track = r.json()['tracks']['items'][0]
track_id = track['id']

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
audio_features = r.json()

for feature, value in audio_features.items():
    print(f"{feature}: {value}")