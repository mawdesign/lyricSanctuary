import pytest
from src.lyric_app.domain.lyrics_repository import LyricsRepository


def test_song_creation_valid():
    """Tests successful creation of a Song object."""
    data = {
        "title": "Amazing Grace",
        "author": "John Newton",
        "lyrics": {"verse1": "Amazing grace how sweet the sound"},
        # ... other fields
    }
    song_id = LyricsRepository.create_song(**data)
    song = LyricsRepository.get_song(song_id)
    assert song.title == "Amazing Grace"
    assert song.author == "John Newton"
    assert "verse1" in song.lyrics


# Add more tests for edge cases, validation (if any), methods on the Song object
# Example: Test creation with missing required fields if you have validation
# def test_song_creation_missing_title_raises_error():
#     with pytest.raises(ValueError): # Or your custom exception
#         Song(author="Test", lyrics={})
