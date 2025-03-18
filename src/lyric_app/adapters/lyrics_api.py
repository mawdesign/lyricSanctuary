# lyric_sanctuary/adapters/lyrics_api.py - Lyrics API adapter

import requests

class LyricsApiAdapter:
    def get_lyrics(self, artist, title):
        try:
            url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            data = response.json()
            return data.get("lyrics")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching lyrics: {e}")
            return None
        except KeyError:
            print("Lyrics not found in API response.")
            return None