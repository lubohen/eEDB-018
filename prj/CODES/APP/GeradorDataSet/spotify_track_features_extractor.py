# Importação das bibliotecas utilizadas

import requests
import pandas as pd
import base64
from config import SPOT_CLIENT_ID as client_id 
from config import SPOT_CLIENT_SECRET as client_secret

#Variáveis Constantes

AUTH_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1/"
DATA_SOURCE_DIR = r"C:\Users\luboh\OneDrive\Área de Trabalho\USP\EngDadosBigData\eEDB-018_REPO\DEVELOPER\eEDB-018\prj\DATA"
DATA_SOURCE_FILE = r"\panda_dataset_taffc_metadata.csv"
DATA_FILE_PATH = DATA_SOURCE_DIR + DATA_SOURCE_FILE
SPOTIFY_DATASET_CSV = "spotify_dataset.csv"
NOT_FOUND_SPOTIFY_CSV = "not_found_spotify_dataset.csv"

def get_spotify_token(client_id, client_secret):
    """Obtém um token de acesso ao Spotify usando as credenciais do cliente."""
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode('utf-8')).decode('utf-8')
    headers = {"Authorization": f"Basic {auth_header}"}
    data = {"grant_type": "client_credentials"}

    try:
        response = requests.post(AUTH_URL, headers=headers, data=data)
        response.raise_for_status()  # Levanta um erro para respostas com erro
        return response.json().get('access_token')
    except requests.RequestException as e:
        raise SystemExit(f"Erro ao obter token de acesso: {e}")

def get_audio_features(track_name, artist_name, headers):
    """Busca características de áudio de uma faixa específica na API do Spotify."""
    search_url = f"{BASE_URL}search"
    query = f"q=track:{track_name}+artist:{artist_name}&type=track"
    try:
        search_response = requests.get(f"{search_url}?{query}", headers=headers)
        search_response.raise_for_status()
        tracks = search_response.json()['tracks']['items']
        
        if not tracks:
            return None  # Faixa não encontrada
        
        track_id = tracks[0]['id']
        features_response = requests.get(f"{BASE_URL}audio-features/{track_id}", headers=headers)
        features_response.raise_for_status()
        return features_response.json()
    except requests.RequestException:
        return None  # Falha na busca ou ao obter características

def load_data_from_csv(file_path):
    """Carrega dados de faixas musicais de um arquivo CSV."""
    return pd.read_csv(file_path)

def process_tracks(data_source):
    """Processa cada faixa musical para obter suas características de áudio."""
    tracks_info = data_source[['Title', 'Artist', 'GenresStr', 'Quadrant']].values
    found_tracks = []
    not_found_tracks = []
    
    for track in tracks_info:
        track_name, artist_name, genre, quadrant = track
        audio_features = get_audio_features(track_name, artist_name, headers)
        
        if audio_features:
            found_tracks.append([
                track_name, artist_name, genre, quadrant,
                *map(audio_features.get, ['acousticness', 'danceability', 'energy', 'instrumentalness',
                                          'key', 'liveness', 'loudness', 'mode', 'speechiness', 
                                          'tempo', 'time_signature', 'valence'])
            ])
        else:
            not_found_tracks.append([track_name, artist_name])
    
    return found_tracks, not_found_tracks

def save_to_csv(data, file_path, columns):
    """Salva os dados em um arquivo CSV."""
    pd.DataFrame(data, columns=columns).to_csv(file_path, index=False)

# Obter as credenciais do ambiente ou arquivo de configuração
CLIENT_ID = client_id
CLIENT_SECRET = client_secret

# Obter o token de acesso
token = get_spotify_token(CLIENT_ID, CLIENT_SECRET)
headers = {"Authorization": f"Bearer {token}"}

# Carregar e processar dados
data_source = load_data_from_csv(DATA_FILE_PATH)
found_tracks, not_found_tracks = process_tracks(data_source)

# Colunas para os DataFrames de saída
columns = [
    'Nome da Faixa', 'Cantor ou Compositor', 'Gênero', 'Quadrante',
    'Acousticness', 'Danceability', 'Energy', 'Instrumentalness',
    'Key', 'Liveness', 'Loudness', 'Mode', 'Speechiness', 'Tempo',
    'Time Signature', 'Valence'
]

# Salvar os resultados
save_to_csv(found_tracks, SPOTIFY_DATASET_CSV, columns)
save_to_csv(not_found_tracks, NOT_FOUND_SPOTIFY_CSV, ['Nome da Faixa', 'Cantor ou Compositor'])