# lyric_sanctuary/adapters/cli_ui.py - Command-line interface adapter

class CliUI:
    def __init__(self, lyrics_service):
        self.lyrics_service = lyrics_service

    def run(self):
        while True:
            print("\nLyrics App")
            print("1. Search Lyrics")
            print("2. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                artist = input("Enter artist: ")
                title = input("Enter song title: ")
                lyrics = self.lyrics_service.get_lyrics(artist, title)
                if lyrics:
                    print("\nLyrics:")
                    print(lyrics)
                else:
                    print("Lyrics not found.")
            elif choice == "2":
                break
            else:
                print("Invalid choice.")