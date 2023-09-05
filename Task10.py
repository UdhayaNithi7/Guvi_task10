#Q-3 Create Music Palyer class and add songs to it make playlist & also make rating for the songs.

class Music_Player:
    def __init__(self, user):
        self.user = user
        self.playlist_data = {}  # Dictionary to store playlists by genre

    def playlist(self, genre, audio):
        if genre not in self.playlist_data:
            self.playlist_data[genre] = []  # Create a new playlist for the genre
        self.playlist_data[genre].extend(audio)
        return f"The {self.user}'s Playlist contains {genre} songs of {audio}"

    def search(self, v):
        for genre in self.playlist_data.keys():
            if v in self.playlist_data[genre]:
                return f"The song is found in the {genre} playlist."
        if v in self.playlist_data.keys():
            return f"The genre is found."

    def rating(self, genre, rate):
        if genre in self.playlist_data:
            audio_count = len(self.playlist_data[genre])
            if audio_count == len(rate):
                rate_avg = sum(rate) / audio_count
                return f"The average rating for {genre} songs is {rate_avg:.2f}"
            else:
                return "Number of ratings does not match the number of songs in the playlist."
        else:
            return f"No playlist found for {genre}."

s_system = Music_Player("John")
print(s_system.playlist("Melody", ["song1", "song2", "song3", "song4", "song5", "song6"]))
print(s_system.search("song1")) 
result = s_system.rating("Melody", [1.5, 2.5, 3, 5, 4, 5])
print(result)





