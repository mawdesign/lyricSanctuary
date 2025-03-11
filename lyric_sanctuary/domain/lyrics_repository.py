# lyric_sanctuary/domain/lyrics_repository.py - Domain repository

import uuid
import couchdb

class LyricsRepository:
    def __init__(self, couchdb_server_url, database_name):
        self.server = couchdb.Server(couchdb_server_url)
        try:
            self.db = self.server[database_name]
        except couchdb.http.ResourceNotFound:
            self.db = self.server.create(database_name)

    def create_song(self, song_data):
        song_id = str(uuid.uuid4())[:8]  # Generate a short GUID
        song_data["_id"] = song_id
        self.db[song_id] = song_data
        return song_id

    def get_song(self, song_id):
        try:
            return self.db[song_id]
        except couchdb.http.ResourceNotFound:
            return None

    def update_song(self, song_id, updated_song_data):
        try:
            doc = self.db[song_id]
            doc.update(updated_song_data)
            self.db[song_id] = doc
            return True
        except couchdb.http.ResourceNotFound:
            return False

    def delete_song(self, song_id):
        try:
            doc = self.db[song_id]
            self.db.delete(doc)
            return True
        except couchdb.http.ResourceNotFound:
            return False

    def search_songs(self, query):
        mango_query = {
            "selector": query,
            "fields": ["_id"]
        }
        try:
            results = self.db.find(mango_query)
            return [result["_id"] for result in results]
        except Exception as e:
            print(f"Error during search: {e}")
            return []

    def get_all_songs(self):
        all_ids = []
        for id in self.db:
            all_ids.append(id)
        return all_ids