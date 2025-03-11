# lyric_sanctuary/application/lyrics_service.py - Application service

from lyric_sanctuary.domain.lyrics_repository import LyricsRepository

class LyricsService:
    def __init__(self, couchdb_server_url, database_name):
        self.repository = LyricsRepository(couchdb_server_url, database_name)

    def create_song(self, song_data):
        return self.repository.create_song(song_data)

    def get_song(self, song_id):
        return self.repository.get_song(song_id)

    def update_song(self, song_id, updated_song_data):
        return self.repository.update_song(song_id, updated_song_data)

    def delete_song(self, song_id):
        return self.repository.delete_song(song_id)

    def search_songs(self, query):
        return self.repository.search_songs(query)

    def get_all_songs(self):
        return self.repository.get_all_songs()
