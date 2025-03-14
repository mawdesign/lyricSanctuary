# lyricSanctuary.py - Main application entry point

from lyric_sanctuary.adapters.cli_ui import CliUI
from lyric_sanctuary.adapters.lyrics_api import LyricsApiAdapter
from lyric_sanctuary.application.lyrics_service import LyricsService
from lyric_sanctuary.domain.lyrics_repository import LyricsRepository

def main():
    # Infrastructure layer (Adapters)
    lyrics_api = LyricsApiAdapter()
    lyrics_repository = LyricsRepository(lyrics_api) #could also be a db

    # Application layer (Service)
    lyrics_service = LyricsService(lyrics_repository)

    # Presentation layer (UI)
    cli_ui = CliUI(lyrics_service)
    cli_ui.run()

if __name__ == "__main__":
    main()
